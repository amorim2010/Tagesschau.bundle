NAME = 'Tagesschau'
ART = 'art-default.jpg'
ICON = 'icon-default.png'

####################################################################################################
def Start():

	ObjectContainer.art = R(ART)
	ObjectContainer.title1 = NAME
	VideoClipObject.thumb = R(ICON)

####################################################################################################
@handler('/video/tagesschau', NAME, thumb=ICON, art=ART)
def MainMenu():

	oc = ObjectContainer()

	for item in XML.ElementFromURL('http://www.tagesschau.de/export/video-podcast/webl/tagesschau').xpath('//item'):
		url = item.xpath('./enclosure/@url')[0]
		title = item.xpath('./title/text()')[0]
		summary = item.xpath('./description/text()')[0]
		originally_available_at = Datetime.ParseDate(item.xpath('./pubDate/text()')[0])

		oc.add(CreateVideoClipObject(url=url, title=title, summary=summary, originally_available_at=originally_available_at))

	return oc

####################################################################################################
def CreateVideoClipObject(url, title, summary, originally_available_at, include_container=False):

	videoclip_obj = VideoClipObject(
		key = Callback(CreateVideoClipObject, url=url, title=title, summary=summary, originally_available_at=originally_available_at, include_container=True),
		rating_key = url,
		title = title,
		summary = summary,
		originally_available_at = originally_available_at,
		items = [
			MediaObject(
				parts = [
					PartObject(key=url)
				],
				container = Container.MP4,
				video_codec = VideoCodec.H264,
				video_resolution = '544',
				audio_codec = AudioCodec.AAC,
				audio_channels = 2,
				optimized_for_streaming = True
			)
		]
	)

	if include_container:
		return ObjectContainer(objects=[videoclip_obj])
	else:
		return videoclip_obj

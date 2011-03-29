# Code by Tom Rothe (motine)

NAME = "Tagesschau"
ART = "art-default.jpg"
ICON = "icon-default.png"

####################################################################################################

def Start():
  Plugin.AddPrefixHandler('/video/tagesschau', VideoMainMenu, NAME, ICON, ART)
  Plugin.AddViewGroup("InfoList", viewMode="InfoList", mediaType="items")

  MediaContainer.art = R(ART)
  MediaContainer.title = NAME
  MediaContainer.viewGroup = "InfoList"
  DirectoryItem.thumb = R(ICON)
  VideoItem.thumb = R(ICON)
  WebVideoItem.thumb = R(ICON)

####################################################################################################

def VideoMainMenu():
  dir = MediaContainer()
  for item in XML.ElementFromURL('http://www.tagesschau.de/export/video-podcast/webl/tagesschau', errors='ignore').xpath('//item'):
    title       = item.find('title').text.strip()
    date        = item.find('pubDate').text.strip()
    description = item.find('description').text.strip()
    url         = item.find('enclosure').get('url').strip()

    dir.Append(VideoItem(url, title=title, subtitle=date, summary=description))

  return dir

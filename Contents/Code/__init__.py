# PMS plugin framework
from PMS import *
from PMS.Objects import *
from PMS.Shortcuts import *

####################################################################################################

# Code by Tom Rothe (motine)

VIDEO_PREFIX = "/video/tagesschau"

NAME = 'Tagesschau'

####################################################################################################

def Start():
    #Plugin.AddPrefixHandler(VIDEO_PREFIX, VideoMainMenu, 'Tagesschau')

    Plugin.AddViewGroup("InfoList", viewMode="InfoList", mediaType="items")
    Plugin.AddViewGroup("List", viewMode="List", mediaType="items")

    #MediaContainer.art = R(ART)
    MediaContainer.title = NAME
    #DirectoryItem.thumb = R(ICON)


@handler(VIDEO_PREFIX, 'Tagesschau')
def VideoMainMenu():
  dir = MediaContainer(mediaType="video", viewGroup="Details")
  for item in XML.ElementFromURL('http://www.tagesschau.de/export/video-podcast/webl/tagesschau', False, errors='ignore').xpath('//item'):
    title       = item.find('title').text.strip()
    date        = item.find('pubDate').text.strip()
    description = item.find('description').text.strip()
    url         = item.find('enclosure').get("url").strip()

    dir.Append(VideoItem(url, title=title, summary=description, subtitle=date, thumb=R('icon-default.png'), art=R('art-default.png')))  # [GoWoon] - remove comment symbol (7.12)
    # Above you see how it should work, but it does not since plex does not play the audio
    # subsequentially, this workaround which heavily relies on info of the internal server structure of ard
    '''
    tmpurl = url.split('video')[1]
    tmpurl = tmpurl.split('.h264')[0]
    playerurl = 'http://www.plexapp.com/player/player.php?url='
    playerurl += 'rtmpt://tagesschau.fcod.llnwd.net/a3705/d1&clip='
    playerurl += tmpurl
    playerurl += '.hi'
    #playerurl += 'rtmpt://tagesschau.fcod.llnwd.net/a3705/d1&id='
    #playerurl += '&clip=/2009/1110/TV-20091110-2134-5001.hi'
    dir.Append(WebVideoItem(playerurl, title=title, summary=description, subtitle=date, thumb=R('icon-default.png'), art=R('art-default.png')))
    #dir.Append(WebVideoItem('http://www.plexapp.com/player/player.php?url=rtmpt://tagesschau.fcod.llnwd.net/a3705/d1&id=&clip=/2009/1110/TV-20091110-2134-5001.hi', title=title, summary=description, subtitle=date, thumb=ICON, art=ART))
    '''
  return dir

import xbmcgui
import xbmcplugin
import sys
import urllib.parse
import json
import xbmc
import xbmcaddon
import get_category
import os
import xbmcvfs
import soud as sond 
class folderQraa:
  #  import channels_Qkareem as Qkareem
 def Qraa():
    
    channels=sond.Listnames()
   # channels= [{"name":"عبد الباسط-  ","kind":"القارئ" ,"country":"فلسطين" ,"url":"","logo":"https://img.youm7.com/large/201903251226322632.jpg"}]
    window=xbmcgui.Window(10000)
    xbmcplugin.setContent(int(sys.argv[1]), "qraa")
    for conuter, channel in enumerate(channels):
         channel_list = xbmcgui.ListItem(label=channel["name"])
         channel_list.setInfo(type="video", infoLabels={"Title": channel["name"], "Genre":  channel["name"]})
        # channel_list.setArt({'fanart':channel["logo"]})
       #  channel_list.setArt({'thumb':channel["logo"]})
       #  channel_list.setProperty("IsPlayable", "true")
         xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url= sys.argv[0] +"?href=" +  channel["href"], listitem=channel_list, isFolder=True)
         
    xbmcplugin.endOfDirectory(int(sys.argv[1]))  
   
  
   








def sour_folder_click(url):
   channels=sond.list_sour(url)
   # channels= [{"name":"عبد الباسط-  ","kind":"القارئ" ,"country":"فلسطين" ,"url":"","logo":"https://img.youm7.com/large/201903251226322632.jpg"}]
   window=xbmcgui.Window(10000)
   xbmcplugin.setContent(int(sys.argv[1]), "qraa")
   for conuter, channel in enumerate(channels):
         channel_list = xbmcgui.ListItem(label=channel["name"])
         channel_list.setInfo(type="video", infoLabels={"Title": channel["name"], "Genre":  channel["name"]})
         channel_list.setArt({'fanart':"https://tinyurl.com/2jr9txg6"})
         channel_list.setArt({'thumb':"https://tinyurl.com/2fdbj5qh"})
         
       #  channel_list.setProperty("IsPlayable", "true")
         xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=  channel["href"], listitem=channel_list, isFolder=False)
         
   xbmcplugin.endOfDirectory(int(sys.argv[1]))  
    # Perform actions when a subfolder is clicked
    # Customize this function based on your requirements
  #  print("Clicked subfolder URL:", url)
 #  xbmcgui.Dialog().ok("", channels[1])
   pass







def handle_navigation():
    # Check if a subfolder is clicked
   
    args = dict(urllib.parse.parse_qsl(sys.argv[2][1:]))
    if "href" not in args:
        pass
  
  
    else:
        # Get the URL of the clicked subfolder
      clicked_url =args["href"]
        # Call the handling function
      sour_folder_click(clicked_url)
        


# Call the function to handle navigation and subfolder clicks
  
handle_navigation()

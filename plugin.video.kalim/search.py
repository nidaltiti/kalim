import xbmc
import xbmcgui
import xbmcplugin
import sys
import soud as sond 

class  search :

   
 def show_keyboard(self): #open kodi "s keyboard  
  
   keyboard = xbmcgui.Dialog()
   keyboard_input = keyboard.input("Sreach", type=xbmcgui.INPUT_ALPHANUM)
   text=keyboard_input.split()
   return text
 #!

 def Search_List_names(self): # filter names qraa
      sreach_word = self.show_keyboard() 
      listnames=sond.Listnames()
      filter_list=[]
      for  index,name in enumerate(listnames):
       if any(word.lower() in name['name'].lower() for word in sreach_word):
        filter_list.append(name)
      self. output_list_names(filter_list) 
   
    
      

 def output_list_names(self,filter_list): # output filter on kodi
    channels=filter_list
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
 #  if filter_list:
 #       xbmcgui.Dialog().ok("User Input", "You entered: " + filter_list[0]['name'])
 #  else:
 #       xbmcgui.Dialog().ok("No Matches", "No names found containing the search words.")
    pass
   


# Display the entered text
##
 # if text:
  #  xbmcgui.Dialog().ok("User Input", "You entered: " + text)
  #else:
  #  xbmcgui.Dialog().ok("User Input", "No input provided.")
       
       
        
      

    
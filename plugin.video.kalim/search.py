import xbmc
import xbmcgui
import xbmcplugin
import sys
import soud as sond 
import urllib.parse
class  search ():

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
      self.output_list_names(filter_list,'?href=')
   
    
      

  def output_list_names(self,filter_list,link): # output filter on kodi
    channels=self.list=filter_list
 #   xbmcgui.Dialog().ok(" سورة", channels [0]["name"])
   # channels= [{"name":"عبد الباسط-  ","kind":"القارئ" ,"country":"فلسطين" ,"url":"","logo":"https://img.youm7.com/large/201903251226322632.jpg"}]
    window=xbmcgui.Window(10000)
    xbmcplugin.setContent(int(sys.argv[1]), "qraa")
    for conuter, channel in enumerate(channels):
         channel_list = xbmcgui.ListItem(label=channel["name"])
         channel_list.setInfo(type="video", infoLabels={"Title": channel["name"], "Genre":  channel["name"]})
        # channel_list.setArt({'fanart':channel["logo"]})
       #  channel_list.setArt({'thumb':channel["logo"]})
         channel_list.setProperty("IsPlayable", "true")
         xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url= sys.argv[0] +link +  channel["href"], listitem=channel_list, isFolder=True)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))  
  
 #  if filter_list:
 #       xbmcgui.Dialog().ok("User Input", "You entered: " + filter_list[0]['name'])
 #  else:
 #       xbmcgui.Dialog().ok("No Matches", "No names found containing the search words.")
    pass
   
  def search_sora(self):
    search_words = self.show_keyboard()
    

    filter_list = []
    listnames = sond.search_sor()

    for index, name in enumerate(listnames):
     #listSour=sond.list_sour( name['href'])
   #  for index_sour,sour in enumerate(listSour):
       if any(word.lower() in name['name'].lower() for word in search_words):
          filter_list.append(name)
  
          pass
    self.output_sour_folder(filter_list)
   # xbmcgui.Dialog().ok("User Input", "You entered: " + filter_list[0]['name'])
  
  def output_sour_folder(self,filter_list):
      channels=filter_list
   # channels= [{"name":"عبد الباسط-  ","kind":"القارئ" ,"country":"فلسطين" ,"url":"","logo":"https://img.youm7.com/large/201903251226322632.jpg"}]
      window=xbmcgui.Window(10000)
      xbmcplugin.setContent(int(sys.argv[1]), "qraa")
      for conuter, channel in enumerate(channels):
         channel_list = xbmcgui.ListItem(label=channel["name"])
         channel_list.setInfo(type="video", infoLabels={"Title": channel["name"], "Genre":  channel["name"]})
        # channel_list.setArt({'fanart':channel["logo"]})
       #  channel_list.setArt({'thumb':channel["logo"]})
         channel_list.setProperty("IsPlayable", "true")
         
         xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url= sys.argv[0] +"?SearchSoura=" +  channel["name"], listitem=channel_list, isFolder=True)
         
      xbmcplugin.endOfDirectory(int(sys.argv[1]))  
  def Listnames(self, sourra):
        self. fiter=[]
        self.list = sond.Listnames()  # Assuming sond is defined elsewhere
       # xbmcgui.Dialog().ok("User Input", sourra)
        self.soura = sourra
        for name in self.list:
            name["href"] = name["href"] + "@" + sourra
            self.fiter.append(name)
     
  #      xbmcgui.Dialog().ok("User Input",  self.fiter[0]["href"])
       # self.output_list_names(self.fiter,"?sreachX=")
        return  self. fiter
  #def find_sora(self,soura,url):
  def get_soura(sel,list,getsoura):  #get soura form  folder  shachick الشيخ  folder  (البحث عن سورة))
   
    #  xbmcgui.Dialog().ok("User Input", "You entered: " +getsoura)
    
       
      for index, souraName in enumerate(list):
     #listSour=sond.list_sour( name['href'])
   #  for index_sour,sour in enumerate(listSour):
       if any(word.lower() in souraName['name'].lower() for word in getsoura.split()):
         # xbmcgui.Dialog().ok("User ", "go: " +item["href"])
          return souraName
      return  None
 #     xbmcgui.Dialog().ok("User Input",  soura )
  def player(self,player):
       playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
       window = xbmcgui.Window(10000)
       xbmcplugin.setContent(int(sys.argv[1]), ".mp3" )

  
       channel_list = xbmcgui.ListItem(label=player[0]["title"])
       channel_list.setInfo(type="video", infoLabels={"Title": player[0]["title"], "Genre": "تلاوة القرآن الكريم"})
       channel_list.setArt({'fanart': "https://tinyurl.com/2jr9txg6"})
       channel_list.setArt({'thumb': "https://tinyurl.com/2fdbj5qh"})
       channel_list.setProperty("IsPlayable", "true")
       url = f"{sys.argv[0]}?action=play&channel_url={urllib.parse.quote(player[0]['link'])}"
       xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=channel_list, isFolder=False)
       playlist.add(player[0]['link'], channel_list)
       xbmcplugin.endOfDirectory(int(sys.argv[1]))  
       xbmc.Player().play(playlist)
       playlist.clear()
     
       pass
  #    pass
   
class handly :

 _search=search()
 def handle_search (self):
   self. findsura= ""
   args = dict(urllib.parse.parse_qsl(sys.argv[2][1:]))
   if "SearchSoura" not in args:
        pass
  
  
   else:
    #  sour_list=sond.list_sour
   
      list=   self._search.Listnames(args["SearchSoura"])
      self._search.output_list_names(list,"?sreachX=")
      
 #     self. findsura=  args['SearchSoura']
   #   self. _search.find_sora(args["SearchSoura"],"")
    #  xbmcgui.Dialog().ok("Selected Item", args['SearchSoura']
   #                    )
    
    

# Get the current window
     

# Get the current window object
   

# Get the current window
   
      #  xbmcgui.Dialog().ok("Selected Item", selected_item_name)
 #    self.findsura = args["SearchSoura"]
     
   #  findsura = findsura.replace("سورة", "").strip()
  
   if"sreachX" not in args:
      pass
   else:
     string= args["sreachX"] 
     arr= string .split("@")
  #   xbmcgui.Dialog().ok("1 Input", arr[1] )
     sour_list=sond.list_sour(arr[0])
     sourastring=arr[1].replace("سورة","")
 #    xbmcgui.Dialog().ok("User Input", "You entered: " + sourastring)
     Get_source= self._search.get_soura(sour_list,sourastring)
   #  xbmcgui.Dialog().ok("User Input", "You : " + Get_source['href'])
     self._search.player(sond.Extract_Media(Get_source['href']))

   #  xbmcgui.Dialog().ok("User Input", "You entered: " + b['name'])

   # self._search.find_sora(self.findsura,"")
     pass
 
 
_handly=handly()
_handly.handle_search()


# Display the entered text
##
 # if text:
  #  xbmcgui.Dialog().ok("User Input", "You entered: " + text)
  #else:
  #  xbmcgui.Dialog().ok("User Input", "No input provided.")
       
       
        
      

    
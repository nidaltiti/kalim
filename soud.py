import xbmcgui
import xbmcaddon
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import os
 #name website quranpedia
def Listnames ():

    url="https://quranpedia.net/reciters"
    client=urlopen(url)
    html=client.read()
    client.close()
    soup=bs(html,"html.parser")
    contians=soup.find_all("a",{"class":"fade-page"})
    sound_Qraa =[]
    for index, name in enumerate(contians, start=1):
     if index>=20:
      Name=name.text
      Name=" ".join(Name.split())
      sound_Qraa.append({"name": Name, "href": name["href"]})
   # channels= [{"name":"عبد الباسط-  ","kind":"القارئ" ,"country":"فلسطين" ,"url":"","logo":"https://img.youm7.com/large/201903251226322632.jpg"}]
    return   sound_Qraa 



def list_sour (sour_url):

  client=urlopen(sour_url)
  html=client.read()
  client.close()
  soup=bs(html,"html.parser")
  contians=soup.find_all("h6",{"class":"mb-0"})
  contians_mp3=soup.find_all("a",{"class":"btn btn-sm btn-primary rounded-circle"})
 
  numberfile=0
  sour =[]
  for index, name in enumerate(contians, start=1):
     
      Name=name.text
     # Name=" ".join(Name.split())
      sour.append({"name": Name, "href":contians_mp3 [numberfile]["href"]})
   # channels= [{"name":"عبد الباسط-  ","kind":"القارئ" ,"country":"فلسطين" ,"url":"","logo":"https://img.youm7.com/large/201903251226322632.jpg"}]
      numberfile=numberfile+2
  return   sour 

  
  pass
  
    
    
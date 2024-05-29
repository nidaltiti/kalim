import xbmcgui
import xbmcaddon
from bs4 import BeautifulSoup as bs
import requests
import os
# source="https://surahquran.com/"
def search_sor():
  url="https://surahquran.com/"
  response = requests.get(url)
  soup = bs(response.content, "html.parser")
  contians = soup.find_all("a", {"class": "button"})
  Sour_quraan = []
  for index, name in enumerate(contians ):
         if "سور" in name.text:
          Name = name.text.strip()
          Sour_quraan .append({"name": Name})
  return Sour_quraan
  pass
 #name website quranpedia
def Listnames():
    url = "https://surahquran.com/qura.html"
    source="https://surahquran.com/"
    response = requests.get(url)
   
    soup = bs(response.content, "html.parser")
    contians = soup.find_all("a", {"class": "button"})
    sound_Qraa = []
    for index, name in enumerate(contians ):
            Name = name.text.strip()
            Name = " ".join(Name.split())
            href = name["href"]
            sound_Qraa.append({"name": Name, "href": source+ href})  # Encode as UTF-8
    return sound_Qraa
def list_sour(sour_url):

    resp = requests.get(sour_url)
    soup = bs(resp.content, "html.parser")
    content = soup.find_all("td", {"style": "font-size:17px"})
    
    if content:
         pass
     #   print("content is not empty")
    else:
         content = soup.find_all("td")

    
    sour = []
    for index, sorahName in enumerate(content):
        name = sorahName.text # Assuming the text inside td tag is the name
        link = sorahName.find('a')['href'] 
        if "https://surahquran.com/" in link:
             pass
        else:
             link = "https://surahquran.com/"+link
        #xbmcgui.Dialog().ok("", name) # Assuming you want to extract the href attribute of the first <a> tag found
        sour.append({"name": name, "href": link})

    return sour
    #
def Extract_Media(url):
   # xbmcgui.Dialog().ok("", url)
    playerfile = [] 
    resp=requests.get(url)
    soup=bs(resp.content,"html.parser")
    link = soup.find("source")["src"]
    title = soup.find('h1').text
    find="no"
    if link:
         find="yes"
    playerfile.append({"title":title,"link":link})
   # xbmcgui.Dialog().ok("", title)
    return playerfile

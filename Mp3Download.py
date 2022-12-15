import requests
from bs4 import BeautifulSoup
import re
import os
import urllib.parse

def get_url(url):    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    global links
    links = soup.find_all("a")
    
def access_to_link(links):
    for link in links:
        Url_Music = link.get("href")
        if "mp3/" in Url_Music:
            music_add.append(Url_Music)
  
music_add  = []


def access_to_music(music_add):
    for link in music_add:
        response = requests.get(link)
        soup = BeautifulSoup(response.content, "html.parser")
        global music_file       
        music_file = soup.find_all("source")
        music_file = str(music_file)
        match = re.search(r'src="(https://.*?/128/.*?.mp3)"', music_file)
        if match:
            match = str(match.group(1))
            parts = match.split(',')
            if len(parts) > 1:
                result = ''.join(parts[1:])
                result = result.replace('<source src="', '')
                music = result 
                print('Descargando',music)
                music = music.replace(" ", urllib.parse.quote(" "))
                url = music.replace("%20", "", 1)
                path = 'D:\\'
                print(url)
                status = os.system(f'wget.exe -P {path} {url}')
                if status == 0:
                    print('The file was downloaded successfully.')
                else:
                    print('There was an error downloading the file.')
                #urllib.request.urlretrieve(music, os.path.join(path))

def run():
    get_url(artist_url)
    access_to_link(links)
    access_to_music(music_add)


if __name__ == '__main__':
    artist_url = input("Enter MP3teca Artist URL: ")
    run()

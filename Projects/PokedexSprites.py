import requests
import os
from bs4 import BeautifulSoup as bs

sprite_dir = os.path.dirname(__file__)+"/Sprites"

def get_all():
    r = requests.get("https://pokemondb.net/pokedex/all")
    src = bs(r.content,"lxml")
    allpk = src.find_all("a",attrs={"class","ent-name"})
    return allpk

def get_name(url):
    r = requests.get(url)
    src = bs(r.content,"lxml")
    name = src.find("h1").text
    return name

def get_sprites(url):
    r = requests.get(url)
    src = bs(r.content,"lxml")
    sprt = src.find_all("a",attrs={"class","sprite-share-link"})
    return sprt

print(sprite_dir)
try:
    os.mkdir(sprite_dir)
except OSError:
    pass

pkmns = get_all()

for pkmn in pkmns:
    sprites = get_sprites("https://pokemondb.net/"+pkmn["href"])
    print("https://pokemondb.net/"+pkmn["href"])
    i = 1
    for sprite in sprites:
        img_r = requests.get(sprite["href"])
        print(sprite["href"])
        with open(sprite_dir+"/"+get_name("https://pokemondb.net/"+pkmn["href"])+str(i)+".png","wb") as img:
            img.write(img_r.content)
            img.close()
            i+=1
        

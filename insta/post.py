import requests
import time
from PIL import Image, ImageDraw, ImageFont
import textwrap
import sys
import schedule
from operator import itemgetter
from instagrapi import Client
from instagrapi import LocationMixin
from instagrapi.types import Usertag, Location
import config

# Create image and with text from quote.
def image_create():
   # to get a daily quote from awsome zenquotes.
    response = requests.get('https://zenquotes.io/api/random')
    data = response.json()
    quote = data[0]['q']
    author = data[0]['a']
    #author = 'Amjad Majeed Dader Hafthrada'
    #print(str(quote))
    #print(str(author))

    astr = quote
    para = textwrap.wrap(astr, width=30)

    MAX_W, MAX_H = 1080, 1080
    im = Image.open('bg.jpg')
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('arial.ttf', 70)
    font2 = ImageFont.truetype('arial.ttf', 30)

    current_h, pad = 350, 10
    for line in para:
        w, h = draw.textsize(line, font=font)
        draw.text(((MAX_W - w) / 2, current_h), line, font=font, fill=(255, 255, 255))
        current_h += h + pad

    draw.multiline_text((700, 880), author, align="center", font=font2, fill=(255, 66, 255))

    im.save('upload.jpg')

image_create()




 #Instagram login and upload...
cl = Client()
cl.login(config.username, config.password)

media = cl.photo_upload(
    path="upload.jpg",
    caption="#quote #Kashmir #instagood #Kupwara #quotes #quotes #Srinagar #inspire #hafthrada #inspiration #love #life #music #dance #follow #trending #hot #boys #girls #happy",
    #location=LocationMixin(name="Srinagar"),
    location=Location(name='Srinagar', lat=34.06, lng=74.81)

)



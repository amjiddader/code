# Post an image on twitter using tweepy ...
import tweepy
import requests
import time
from PIL import Image, ImageDraw, ImageFont
import textwrap
import sys
import schedule
from operator import itemgetter
#import config

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


# Twitter API credentials
consumer_key = "yZw99hENBdkgThveinfhV3Q0b"
consumer_secret = "cvNSW1DEJgvfPzPOYvr55kamSQgPPcGpbQix7hUpfin9MCxJb9"
access_token = "341403663-FqUhkY9rADHs8eSwUp4sskfzHTKBHr9Y6hF1Tt0u"
access_token_secret = "hQoFXmMmGIMX6iNf8fCI1HM98eFtGvf8YNpe1vrqnmCTy"

# Path to the image file you want to post
image_path = "upload.jpg"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Post the image
try:
    media = api.media_upload(image_path)
    api.update_status(status="motivational inspirational quotes! #kashmir #kupwara #follow #srinagar #india #retweet", media_ids=[media.media_id])
    print("Image posted successfully.")
except tweepy.TweepError as e:
    print(f"Error posting image: {e}")


# assign the values accordingly

from The_Tva.events import register
from The_Tva import OWNER_ID
from The_Tva import telethn as tbot
import os 
from PIL import Image, ImageDraw, ImageFont
import shutil 
import random, re
import glob
import time
from telethon.tl.types import InputMessagesFilterPhotos



ANIMEPHOTO_MEDIA_LINK = ["./The_Tva/resources/photo_2021-10-14_16-20-43.jpg", 
                         "./The_Tva/resources/photo_2021-10-14_16-20-44.jpg",
                         "./The_Tva/resources/photo_2021-10-14_16-20-46.jpg",
                         "./The_Tva/resources/photo_2021-10-14_16-20-48.jpg",    
                         "./The_Tva/resources/photo_2021-10-14_16-20-50.jpg", 
                         "./The_Tva/resources/photo_2021-10-14_16-20-52.jpg",
                         "./The_Tva/resources/photo_2021-10-14_16-20-53.jpg",
                         "./The_Tva/resources/photo_2021-10-14_16-20-58.jpg",
                         "./The_Tva/resources/photo_2021-10-14_16-21-01.jpg",
                         "./The_Tva/resources/photo_2021-10-14_16-21-03.jpg",
                         "./The_Tva/resources/photo_2021-10-14_16-21-05.jpg",
                         "./The_Tva/resources/photo_2021-10-14_16-20-07.jpg",
                         ]

TELEGRAPH_MEDIA_LINKS = ["./The_Tva/resources/photo_2021-10-14_15-26-26.jpg", 
                         "./The_Tva/resources/photo_2021-10-14_15-26-27.jpg", 
                         "./The_Tva/resources/photo_2021-10-14_16-20-41.jpg",
                         "./The_Tva/resources/photo_2021-10-14_16-21-08.jpg",
                         "./The_Tva/resources/photo_2021-10-14_16-21-09.jpg",    
                         "./The_Tva/resources/photo_2021-10-14_16-21-10.jpg", 
                         "./The_Tva/resources/photo_2021-10-14_16-21-12.jpg",
                         "./The_Tva/resources/photo_2021-10-14_16-21-14.jpg",
                         "./The_Tva/resources/photo_2021-10-14_16-21-15.jpg",
                         "./The_Tva/resources/photo_2021-10-14_16-21-16.jpg",
                         "./The_Tva/resources/photo_2021-10-14_16-21-17.jpg",
                         "./The_Tva/resources/photo_2021-10-14_16-21-19.jpg",
                         "./The_Tva/resources/shelap1.jpg", 
                         "./The_Tva/resources/shelap2.jpg",
                         "./The_Tva/resources/images.jpeg",
                        ]

@register(pattern="^/logo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:

    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('Wait..now ok!')
 try:
    text = event.pattern_match.group(1)
    img = Image.open(random.choice(TELEGRAPH_MEDIA_LINKS))
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 25
    fillcolor = "gold"
    shadowcolor = "blue"
    font = ImageFont.truetype("./The_Tva/resources/font.otf",40)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="black", stroke_width=2, stroke_fill="red")
    fname2 = "Logo.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Made By @The_Tva")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Join with us ~ @The_TVA to use this, {e}')


@register(pattern="^/wlogo ?(.*)")
async def logo(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:

    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('Creating your logo...wait!')
 try:
    text = event.pattern_match.group(1)
    img = Image.open('./The_Tva/resources/shelap3.jpg')
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "white"
    shadowcolor = "blue"
    font = ImageFont.truetype("./The_Tva/resources/Maghrib.ttf", 1000)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="white", stroke_width=0, stroke_fill="white")
    fname2 = "Logo.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Made By @The_Tva")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Join with us ~ @The_TVA to use this, {e}')

  

@register(pattern="^/pandalogo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:

    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('Creating your logo...wait!')
 try:
    text = event.pattern_match.group(1)
    img = Image.open('./The_Tva/resources/pandabg.png')
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 25
    fillcolor = "gold"
    shadowcolor = "blue"
    font = ImageFont.truetype("./The_Tva/resources/font.otf", 100)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="black", stroke_width=25, stroke_fill="yellow")
    fname2 = "Logo.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Made By @The_Tva")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Join with us ~ @The_TVA to use this, {e}')
  
  
  
@register(pattern="^/animelogo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:

    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('Wait..now ok!')
 try:
    text = event.pattern_match.group(1)
    img = Image.open(random.choice(ANIMEPHOTO_MEDIA_LINK))
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 25
    fillcolor = "gold"
    shadowcolor = "blue"
    font = ImageFont.truetype("./The_Tva/resources/font.otf",40)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="black", stroke_width=2, stroke_fill="yellow")
    fname2 = "Logo.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Made By @The_Tva")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Join with us ~ @The_TVA to use this, {e}')

  
file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")


__help__ = """

 ☉ /logo text :  Create your logo with your name
 ☉ /wlogo text :  Create your logo with your name
 ☉ /pandalogo :  Create your logo with your name
 ☉ /animelogo :  Create your logo with your name
 
 """
__mod_name__ = "Logo Maker"

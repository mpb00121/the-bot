from The_Tva import pbot as app
from The_Tva.pyrogramee.errors import capture_err
from The_Tva.pyrogramee.json_prettify import json_prettify
from The_Tva.pyrogramee.fetch import fetch
from pyrogram import filters

@app.on_message(filters.command("covid") & ~filters.edited)
@capture_err
async def covid(_, message):
    if len(message.command) == 1:
        data = await fetch("https://corona.lmao.ninja/v2/all")
        data = await json_prettify(data)
        await app.send_message(message.chat.id, text=data)
        return
    if len(message.command) != 1:
        country = message.text.split(None, 1)[1].strip()
        country = country.replace(" ", "")
        data = await fetch(f"https://corona.lmao.ninja/v2/countries/{country}")
        data = await json_prettify(data)
        await app.send_message(message.chat.id, text=data)
        return
    
__help__ = """
 ☉ /covid - To Get Global Stats of Covid.
 ☉ /covid <country> - To Get Stats of A Single Country.
 
 @The_Tva
"""

__mod_name__ = "COVID"

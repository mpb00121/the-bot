import os
from pyrogram import Client, filters
from pyrogram.types import *

from The_Tva.config import get_str_key
from The_Tva import pbot

TEXT = """👋 Hey My name is The_TVA ✨ - A powerful group management bot which can help you to manage your groups effectively as possible With   Advanced AI . 
Click `menu` button for more information.
Join my [news channel](https://t.me/The_TVA) to get information on all the latest updates.  """

MENU = [
    [
        InlineKeyboardButton(
            text="↪️ Main menu ", callback_data="aboutmanu_back"),
    ],
]

@pbot.on_message(filters.command(["tart"]))
async def tart(pbot, update):
    await update.reply_text(
        text=TEXT,
        reply_markup=MENU,
        disable_web_page_preview=True,
        quote=True
    ) 
    

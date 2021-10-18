import os
from pyrogram import Client, filters
from pyrogram.types import *

from The_Tva.config import get_str_key
from The_Tva import pbot

REPO_TEXT = "**A Powerful BOT to Make Your Groups Secured and Organized ! \n\n↼ Øwñêr ⇀ : 『 @The_Tva 』\n╭──────────────\n┣─ » Python ~ 3.8.6\n┣─ » Update ~ Resently\n╰──────────────\n\n»»» @The_Tva «««"
  
BUTTONS = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("Developer", url=f"https://t.me/The_Tva"),
        InlineKeyboardButton("Video info ", url=f"https://youtube.com/channel/UC7_CMjBK-pmQB3e-DetIr6g"),
      ],[
        InlineKeyboardButton("Channel✨ ", url="https://t.me/The_TVA"),
        InlineKeyboardButton("Group✨", url="https://t.me/The_TVA"),
      ]]
    )
  
  
@pbot.on_message(filters.command(["repo"]))
async def repo(pbot, update):
    await update.reply_text(
        text=REPO_TEXT,
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )

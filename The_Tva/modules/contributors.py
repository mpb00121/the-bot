import github  # pyGithub
from pyrogram import filters

from The_Tva.services.pyrogram import pbot as client

  
    
@client.on_message(filters.command("contributors") & ~filters.edited)
async def give_cobtribs(c, m):
    g = github.Github()
    co = ""
    n = 0
    repo = g.get_repo("CGS-TEAM/The_Tva")
    for i in repo.get_contributors():
        n += 1
        co += f"{n}. [{i.login}](https://github.com/{i.login})\n"
    t = f"**The_TVA Contributors**\n\n{co}\n\n\nA Powerful BOT to Make Your Groups Secured and Organized ! ✨"
    await m.reply(t, disable_web_page_preview=True)
    
__help__ = """
Contributor
 ☉ /contributors : contributors using this bot  
 
 @The_Tva
"""
__mod_name__ = "Contributors"

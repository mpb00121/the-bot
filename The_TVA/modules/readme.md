## The_TVA Example plugin format
```python3
from The_Tva.decorator import register
from .utils.disable import disableable_dec
from .utils.message import get_args_str

@register(cmds="rose")
@disableable_dec("rose")
async def _(message):
    j = "Hello there my name is The_TVA"
    await message.reply(j)
    

__help__ = """
<b>Hi</b>
- /hi: Hello there my name is The_TVA
"""
__mod_name__ = "The_TVA"
```

<a href="https://t.me/The_TVA"><img src="https://img.shields.io/badge/support%20group-blue.svg?style=for-the-badge&logo=Telegram">
</a> <a href="https://t.me/The_TVA"><img src="https://img.shields.io/badge/Join-Updates%20Channel-blue.svg?style=for-the-badge&logo=Telegram"></a>
<a href="https://t.me/The_TVA"><img src="https://img.shields.io/badge/Foundbot%20on-blue.svg?style=for-the-badge&logo=Telegram">

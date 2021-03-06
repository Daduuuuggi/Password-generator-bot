# Author Dday Nasser
# Email : dadynasser89@gmail.com

import random, os
from pyrogram import  Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


Bot = Client(
    "Password Generator Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)


@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    TEXT = "Hai {} \n\n**I Am Password Generator Bot. I Can Generate Strong Passwords At Your Wish Length (Max. 84).** \n\nFor Know More /help"
    BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton("Channel š°", url = "https://telegram.me/EKBOTZ_UPDATE"),InlineKeyboardButton("Support Group ā­ļø", url = "https://telegram.me/ekbotz_support")],[InlineKeyboardButton("Repo šļø", url = "https://github.com/M-fazin/Password-Generator-Bot"),InlineKeyboardButton("Deploy šļø", url = "https://heroku.com/deploy?template=https://github.com/M-fazin/Password-Generator-Bot")],[InlineKeyboardButton("Developer š”", url = "https://github.com/M-fazin/")]])
    await update.reply_text(
        text=TEXT.format(update.from_user.mention),
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
	
@Bot.on_message(filters.private & filters.command(["help"]))
async def help(bot, update):
    HELP = "Hai {} \n\n**There Is Nothing To Know More.** \n- Send Me The Limit Of Your Password \n- I Will Give The Password Of That Limit. \n\nEx:- `20` \n\n**Note :-**\nā¢ Only Digits Are Allowed \nā¢ Maximum Allowed Digits Till 84 (I Can't Generate Passwords Above The Length 84)"
    HELP_BUTTON = InlineKeyboardMarkup([[InlineKeyboardButton("š§āš» Channel", url = "https://telegram.me/EKBOTZ_UPDATE"),InlineKeyboardButton("šļø Source Code", url = "https://github.com/M-fazin/Password-Generator-Bot")]])
    await update.reply_text(
        text=HELP.format(update.from_user.mention),
        reply_markup=HELP_BUTTON,
        disable_web_page_preview=True,
        quote=True
        )
	
@Bot.on_message(filters.private & filters.command(["about", "source", "repo"]))
async def about(bot, update):
    ABOUT = "**š¤ Bot :** Password Generator Bot\n\n**š§āš» Developer :** [M-fazin](https://github.com/M-fazin)\n\n**š» Channel :** @EKBOTZ_UPDATE\n\n**āļø Support :** @ekbotz_support \n\n**šļø Source Code :** [Password Generator Bot](https://github.com/M-fazin/Password-Generator-Bot)\n\n**āļø Language :** Python 3\n\n**š”ļø Framework :** Pyrogram"
    await update.reply_text(
	text=ABOUT,
	disable_web_page_preview=True,
	quote=True
    )
	
@Bot.on_message(filters.private & filters.text)
async def password(bot, update):
    message = await message.reply_text('`Processing...`')
    password = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+".lower()
    try:
        limit = int(message.text)
    except:
        await message.edit_text('Limit is wrong')
        return
    if limit > 100 or limit <= 0:
        text = "Sorry... Failed To Create Password, Because Limit is 1 to 100."
    else:
        random_value = "".join(random.sample(password, limit))
        text = f"**Limit :-** `{str(limit)}`.\n**Password :-** `{random_value}`**\n\nJoin @EKBOTZ_UPDATE"
    await message.edit_text(text, True)
	

			
Ek.run()

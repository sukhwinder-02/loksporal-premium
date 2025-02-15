#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>╭━━━━━━━━━━━━━━━➣\n┣⪼ 𝗢𝘄𝗻𝗲𝗿 : <a href='tg://user?id={OWNER_ID}'>𝐒𝐀𝐍𝐃𝐇𝐔</a>\n┣⪼ 𝗕𝗮𝗰𝗸𝘂𝗽 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 : <a href='https://t.me/OttSandhu'>𝐎𝐭𝐭 𝐒𝐚𝐧𝐝𝐡𝐮</a>\n┣⪼ 𝗠𝗼𝘃𝗶𝗲 𝗚𝗿𝗼𝘂𝗽 : <a href='https://t.me/+_-9trQQYYFczNTJl'>𝐒𝐞𝐚𝐫𝐜𝐡 𝐆𝐫𝐨𝐮𝐩</a>\n┣⪼ 𝗠𝗼𝘃𝗶𝗲𝘀 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 : <a href='https://t.me/+MbS71p0fCIRhMTA1'>𝐏𝐮𝐧𝐣𝐚𝐛𝐢 𝐌𝐨𝐯𝐢𝐞𝐬</a>\n╰───────────────⍟</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("𝗖𝗹𝗼𝘀𝗲", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

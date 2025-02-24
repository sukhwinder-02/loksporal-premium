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
            text = f"<b><blockquote>◈ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/Baii_Ji>Bᴀɪ Jɪ</a>\n◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/Ott_Sandhu>Sᴀɴᴅʜᴜ</a>\n◈ ᴍᴏᴠɪᴇ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/OttSandhu>ʙᴀᴄᴋᴜᴘ</a>\n◈ ᴘᴜɴᴊᴀʙɪ ᴍᴏᴠɪᴇꜱ : <a href=https://t.me/+MbS71p0fCIRhMTA1>ᴘᴜɴᴊᴀʙɪ ᴍᴏᴠɪᴇꜱ</a>\n◈ ᴀᴅᴜʟᴛ ᴠɪᴅᴇᴏꜱ : <a href=https://t.me/Ott_Sandhu>ᴊᴏɪɴ 💀</a>\n◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/Baii_Ji>Bᴀɪ Jɪ</a></blockquote></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data = "close")
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

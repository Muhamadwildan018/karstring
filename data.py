from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("ᴍᴜʟᴀɪ ᴍᴇᴍʙᴜᴀᴛ sᴛʀɪɴɢ", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="ᴋᴇᴍʙᴀʟɪ", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton(ᴏᴡɴᴇʀ", url="https://t.me/mhmdwldnnnn")],
        [
            InlineKeyboardButton("ʙᴀɴᴛᴜᴀɴ", callback_data="help"),
            InlineKeyboardButton("ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ", callback_data="about")
        ],
        [InlineKeyboardButton("ᴅᴀғᴛᴀʀ ᴘᴘ ᴛᴇʟᴇ", url="https://t.me/Disney_storeDan")],
    ]

    START = """
ʜᴇʟʟᴏ {}
✪ sᴀʏᴀ {} 🤖

ɪɴɪ ᴀᴅᴀʟᴀʜ ʙᴏᴛ sᴛʀɪɴɢ sᴇssɪᴏɴ ʏᴀɴɢ ᴍᴜᴅᴀʜ 
ᴅɪɢᴜɴᴀᴋᴀɴ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ ᴀɴᴅᴀ
    """

    HELP = """
  **𝗟𝗶𝘀𝘁 𝗕𝗮𝗻𝘁𝘂𝗮𝗻**

/about - Cek
/help - Cek
/start - Cek
/generate - Cek
/cancel - Cek
/restart - Cek
"""

    ABOUT = """
**𝗧𝗲𝗻𝘁𝗮𝗻𝗴 𝗦𝗮𝘆𝗮** 

𝗦𝗮𝘆𝗮 𝗗𝗶𝗯𝘂𝗮𝘁 𝗢𝗹𝗲𝗵 [Dan](https://t.me/mhmdwldnnnn)

𝗕𝘂𝗮𝘁 𝗟𝘂 𝗬𝗮𝗻𝗴 𝗕𝗮𝗿𝘂 𝗠𝗮𝗲𝗻 𝗧𝗲𝗹𝗲 𝗬𝗮 𝗔𝗻𝗷𝗲𝗻𝗴..

Cuma Modal Copas Ya Anjeng, Gua Bukan ProDev Ya Bangsat

Maintainer : @mhmdwldnnnn
    """

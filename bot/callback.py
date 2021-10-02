# Copyright (C) 2021 By VeezMusicProject

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import Veez


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ HOW TO USE THIS BOT:

1.) önce beni grubunuza ekleyin.
2.) sonra beni yönetici olarak terfi ettir ve anonim yönetici hariç tüm izinleri ver.
3.) @ { Veez . ASSISTANT_NAME  } grubunuza.
4.) video akışına başlamadan önce sesli sohbeti açın.
5.) akışı başlatmak için /izlet (videoya yanıtla) yazın.
6.) video akışını sonlandırmak için /dur yazın.

📝 **not: akış ve durdurma komutu yalnızca grup yöneticisi tarafından yürütülebilir!**

⚡ __Bakımını KIZILSANCAK Proje Ekibi Yapmaktadır__""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "🏡 Go Back", callback_data="cbstart")
            ]]
        ))


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"✨ **Hello there, I am a telegram group video streaming bot.**\n\n💭 **I was created to stream videos in group "
        f"video chats easily.**\n\n❔ **To find out how to use me, please press the help button below** 👇🏻",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "➕ Add me to your Group ➕", url=f"https://t.me/{Veez.BOT_USERNAME}?startgroup=true")
            ], [
                InlineKeyboardButton(
                    "❔ HOW TO USE THIS BOT", callback_data="cbguide")
            ], [
                InlineKeyboardButton(
                    "🌐 Telegram Geliştiricileri", callback_data="cbinfo")
            ], [
                InlineKeyboardButton(
                    "💬 Group", url=f"https://t.me/{Veez.GROUP_NAME}"),
                InlineKeyboardButton(
                    "📣 Channel", url=f"https://t.me/{Veez.CHANNEL_NAME}")
            ], [
                InlineKeyboardButton(
                    "🧙🏻‍♂️ Owner", url=f"https://t.me/{Veez.OWNER_NAME}")
            ], [
                InlineKeyboardButton(
                    "📚 All Command List", callback_data="cblist")
            ]]
        ))


@Client.on_callback_query(filters.regex("cbinfo"))
async def cbinfo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🌐 **bot bilgisi !**

🤖 __Bu bot, WebRTC'den çeşitli yöntemler kullanılarak telegram grubu görüntülü sohbetlerinde video akışı yapmak için oluşturuldu.__

💡 __Bu botu Gruplarınıza Tam yetkili bir şekilde ekleyebilir veya botun klonunu yapmak için klon yöntemini
Kullanabilirsiniz.__

👨🏻‍💻 __Bu botun geliştirilmesine katılan geliştiriciler sayesinde geliştiricilerin listesi aşağıda görülebilir:__

👩🏻‍✈️ » [ADSIZ KAPTAN](https://t.me/kizilsancaksahibi)
🤵🏻 » [UYUMSUZ REİS](https://t.me/Gost_193)
🤵🏻 » [KANLI REİS](https://t.me/kanlireis)
🤵🏻 » [EL PATRON](https://t.me/elpatron0009)
🤵🏻 » [BERHAVA](https://t.me/berhosky)
🤵🏻 » [MÜSLÜM](https://t.me/sigara46)

__This bot licensed under GNU-GPL 3.0 License__""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "🏡 Go Back", callback_data="cbstart")
            ]]
        ),
        disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cblist"))
async def cblist(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""📚 komut listesi:

» /izlet (reply to video or yt/live url) - to stream video
» /dur - stop the video streaming
» /ara (song name) - Şarkı arar indirir Sadece Yt
» /bul (video adı) - videoyu arar indirir Sadece Yt
» /lyric (song name) - Şarkı sözü arar
» /gel - Asistanı sohbete davet eder
» /vleave - order assistant leave from your group

🎊 FUN CMD:

» /asupan - check it by yourself
» /chika - check it by yourself
» /wibu - check it by yourself
» /truth - check it by yourself
» /dare - check it by yourself

🔰 EXTRA CMD:

» /tts (reply to text) - text to speech
» /alive - check bot alive status
» /ping - check bot ping status
» /uptime - check bot uptime status
» /sysinfo - check bot system information

💡 SUDO ONLY:

» /rmd - remove all downloaded files
» /rmw - remove all downloaded raw files
» /leaveall - order assistant leave from all group

⚡ __Maintained by Veez Project Team__""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "🏡 Go Back", callback_data="cbstart")
            ]]
        ))


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()

# Copyright (C) 2021 By VeezMusicProject

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import Veez


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ BU BOTU NASIL KULLANABİLİRİM :

1.) VİDEO YAYINLADIKTAN SONRA BAŞKA VİDEO YAYINLAMAK İÇİN LÜTFEN /DUR KOMUTUNU KULLANDIKTAN SONRA YENİ VİDEOYU YAYINLAYINIZ!!!.
2.) önce beni gruba ekleyniz sonra beni yönetici olarak terfi ettir.
3.) @ { Veez . ASSISTANT_NAME  } grubunuza.
4.) video akışına başlamadan önce sesli sohbeti açın.
5.) akışı başlatmak için /izlet (videoya yanıtla) yazın.
6.) video akışını sonlandırmak için /dur yazın.

📝 **not: bu botu sadece grup adminleri kullanabilir!**

⚡ __[FLACKWAR DEV](https://t.me/flackwardev) tarafından geliştirildi__""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "🏡 geri dön", callback_data="cbstart")
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
                    "❔ BU BOTU NASIL KULLANABİLİRİM", callback_data="cbguide")
            ], [
                InlineKeyboardButton(
                    "🌐 GELİŞTİRİCİLER", callback_data="cbinfo")
            ], [
                InlineKeyboardButton(
                    "💬 Group", url=f"https://t.me/{Veez.GROUP_NAME}"),
                InlineKeyboardButton(
                    "📣 Channel", url=f"https://t.me/{Veez.CHANNEL_NAME}")
            ], [
                InlineKeyboardButton(
                    "🧙🏻‍♂️ SAHİP", url=f"https://t.me/{Veez.OWNER_NAME}")
            ], [
                InlineKeyboardButton(
                    "📚 TÜM KOMUT LİSTESİ", callback_data="cblist")
            ]]
        ))


@Client.on_callback_query(filters.regex("cbinfo"))
async def cbinfo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🌐 **bot bilgisi !**

🤖 __Bu bot, WebRTC'den çeşitli yöntemler kullanılarak telegram grubu görüntülü sohbetlerinde video akışı yapmak için oluşturuldu.__


👩🏻‍✈️ » [BURAK](https://t.me/burakizm)
🤵🏻 » [BAY KAOSS](https://t.me/Baykaoss)

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

» /izlet (indirilen dosyayı veya youtube linkini yanıtlayıp yazın) 
» /dur - yayını durdur 
» /ara (şarkı adı) - Şarkı arar indirir Sadece Yt
» /bul (video adı) - videoyu arar indirir Sadece Yt
» /lyric (şarkı adı ) - Şarkı sözü arar
» /gel - Asistanı sohbete davet eder


⚡ __Maintained by Veez Project Team__""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "🏡 geri dön", callback_data="cbstart")
            ]]
        ))


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()

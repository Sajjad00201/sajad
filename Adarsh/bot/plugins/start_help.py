# (c) adarsh-goel 
from Adarsh.bot import StreamBot
from Adarsh.vars import Var
import logging
logger = logging.getLogger(__name__)
from Adarsh.bot.plugins.stream import MY_PASS
from Adarsh.utils.human_readable import humanbytes
from Adarsh.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from Adarsh.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.SESSION_NAME)
from pyrogram.types import ReplyKeyboardMarkup

if MY_PASS:
            buttonz=ReplyKeyboardMarkup(
            [
                ["🔒ورود🔒"],
                ["حمایت💰","📜راهنما"],
                ["پشتیبانی💠","❓درباره ما"],
                ["💹وضعیت ربات💹"]
            ],
            resize_keyboard=True
        )
else:
            buttonz=ReplyKeyboardMarkup(
            [
                ["حمایت💰","📜راهنما"],
                ["پشتیبانی💠","❓درباره ما"],
                ["💹وضعیت ربات💹"]
            ],
            resize_keyboard=True
        )
            buttonser=ReplyKeyboardMarkup(
            [
                ["Ⓜ️وضعیت کلیⓂ️"],
                ["پینگ🅿️","🈳دیتاسنتر"],
                ["↩️منوی اصلی"]
            ],
            resize_keyboard=True
        )
            buttonback=ReplyKeyboardMarkup(
            [
                ["↩️منوی اصلی"],
                     
            ],
            resize_keyboard=True
        )
            
            
@StreamBot.on_message((filters.command("start")) & filters.private & ~filters.edited)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"🔆اطلاعیه\n\n🔰کاربر [{m.from_user.first_name}](tg://user?id={m.from_user.id}) وارد ربات شد."
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await b.send_message(
                    chat_id=m.chat.id,
                    text="⛔️حساب کاربری شما به دلیل تخلف مسدود شده است⛔️",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
             await StreamBot.send_photo(
                chat_id=m.chat.id,
                photo="https://telegra.ph/file/4a12a4478985dc1818f02.jpg",
                caption="📛 برای حمایت از ما و همچنان ربات ابتدا در کانال ما عضو شوید.\n\n✅ پس از عضویت وارد ربات شده و دستور /start را ارسال کنید.",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("💠عضویت در کانال💠", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="HTML"
            )
             return
        except Exception:
            await b.send_message(
                chat_id=m.chat.id,
                text="⚠️یک مشکل وجود دارد. با آیدی @KN7_A در ارتباط باشید.",
                parse_mode="HTML",
                disable_web_page_preview=True)
            return
    await StreamBot.send_photo(
        chat_id=m.chat.id,
        photo ="https://telegra.ph/file/4a12a4478985dc1818f02.jpg",
        caption =f'⚡️خوش آمدید\n\n💥برای استفاده از ربات کافی است فایل خود را ارسال کرده و سپس لینک آن را دریافت کنید.\n\n🆔 @King_Network7',
        reply_markup=buttonz)

@StreamBot.on_message((filters.regex('❓درباره ما')) & filters.private & ~filters.edited)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"🔆اطلاعیه\n\n🔰کاربر [{message.from_user.first_name}](tg://user?id={message.from_user.id}) وارد ربات شد."
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="⛔️حساب کاربری شما به دلیل تخلف مسدود شده است⛔️",
                    parse_mode="HTML",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await StreamBot.send_photo(
                chat_id=message.chat.id,
                photo="https://telegra.ph/file/4a12a4478985dc1818f02.jpg",
                text="📛 برای حمایت از ما و همچنان ربات ابتدا در کانال ما عضو شوید.\n\n✅ پس از عضویت وارد ربات شده و دستور /start را ارسال کنید.",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("💠عضویت در کانال💠", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="⚠️یک مشکل وجود دارد. با آیدی @KN7_A در ارتباط باشید.",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="""
        👤درباره ما

↯طراحی: KingNetwork
↯سرور: <a href='https://t.me/King_network7'>Exclusive</a>
↯ورژن: 1.0.2
↯لینک: نیم بها
↯حمایت: <a href='https://www.payping.ir/d/WiZG'>دونیت</a>

🆔 @King_Network7
        """,parse_mode="HTML",disable_web_page_preview=True,reply_markup=buttonback)

@StreamBot.on_message((filters.regex('📜راهنما')) & filters.private & ~filters.edited)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"🔆اطلاعیه\n\n🔰کاربر [{message.from_user.first_name}](tg://user?id={message.from_user.id}) وارد ربات شد."
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="⛔️حساب کاربری شما به دلیل تخلف مسدود شده است⛔️",
                    parse_mode="HTML",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await StreamBot.send_photo(
                chat_id=message.chat.id,
                photo="https://telegra.ph/file/4a12a4478985dc1818f02.jpg",
                text="📛 برای حمایت از ما و همچنان ربات ابتدا در کانال ما عضو شوید.\n\n✅ پس از عضویت وارد ربات شده و دستور /start را ارسال کنید.",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("💠عضویت در کانال💠", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="⚠️یک مشکل وجود دارد. با آیدی @KN7_A در ارتباط باشید.",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="""
❗️راهنمای ربات

⇇فایل مورد نظر خود ارسال یا فوروارد کنید
⇇قبل از دانلود VPN را خاموش کنید
⇇لینک های ربات نیم بها میباشد
⇇انقضای فایل ها 30 روز است

🆔 @King_Network7
        """,parse_mode="HTML",disable_web_page_preview=True,reply_markup=buttonback)

@StreamBot.on_message((filters.regex('💹وضعیت ربات💹')) & filters.private & ~filters.edited)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"🔆اطلاعیه\n\n🔰کاربر [{message.from_user.first_name}](tg://user?id={message.from_user.id}) وارد ربات شد."
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="⛔️حساب کاربری شما به دلیل تخلف مسدود شده است⛔️",
                    parse_mode="HTML",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await StreamBot.send_photo(
                chat_id=message.chat.id,
                photo="https://telegra.ph/file/4a12a4478985dc1818f02.jpg",
                text="📛 برای حمایت از ما و همچنان ربات ابتدا در کانال ما عضو شوید.\n\n✅ پس از عضویت وارد ربات شده و دستور /start را ارسال کنید.",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("💠عضویت در کانال💠", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="⚠️یک مشکل وجود دارد. با آیدی @KN7_A در ارتباط باشید.",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="""💥گزینه مورد نظر خود را انتخاب کنید💥

🆔 @King_Network7""",parse_mode="HTML",disable_web_page_preview=True,reply_markup=buttonser)

@StreamBot.on_message((filters.regex('↩️منوی اصلی')) & filters.private & ~filters.edited)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"🔆اطلاعیه\n\n🔰کاربر [{message.from_user.first_name}](tg://user?id={message.from_user.id}) وارد ربات شد."
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="⛔️حساب کاربری شما به دلیل تخلف مسدود شده است⛔️",
                    parse_mode="HTML",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await StreamBot.send_photo(
                chat_id=message.chat.id,
                photo="https://telegra.ph/file/4a12a4478985dc1818f02.jpg",
                text="📛 برای حمایت از ما و همچنان ربات ابتدا در کانال ما عضو شوید.\n\n✅ پس از عضویت وارد ربات شده و دستور /start را ارسال کنید.",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("💠عضویت در کانال💠", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="⚠️یک مشکل وجود دارد. با آیدی @KN7_A در ارتباط باشید.",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="""
🔱به منوی اصلی برگشتید.

🆔 @King_Network7
        """,parse_mode="HTML",disable_web_page_preview=True,reply_markup=buttonz)
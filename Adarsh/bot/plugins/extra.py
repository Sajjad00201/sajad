from Adarsh.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
import time
import shutil, psutil
from utils_bot import *
from Adarsh import StartTime


START_TEXT = """🖥دیتاسنتر اکانت شما: `{}`\n\n🆔 @King_Network7"""


@StreamBot.on_message(filters.regex("پشتیبانی💠"))
async def maintainers(b,m):
    try:
       await b.send_message(chat_id=m.chat.id,text="*",quote=True)
    except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="📞برای گزارش مشکل، انتقاد، پیشنهاد و... با آیدی زیر در ارتباط باشید.\n\n🆔 @King_Network7",
                    
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("💡پشتیبانی💡", url=f"https://t.me/KN7_A")
                            ]
                        ]
                    ),
                    parse_mode="markdown",
                    disable_web_page_preview=True)
            
         
@StreamBot.on_message(filters.regex("حمایت💰"))
async def follow_user(b,m):
    try:
       await b.send_message(chat_id=m.chat.id,text="*",quote=True)
    except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="""‼️برای ادامه فعالیت ربات و تامین بخشی از هزینه های سرور میتوانید از طریق لینک زیر از ربات و تیم حمایت کنید.

🆔 @King_Network7""",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🔥لینک دونیت🔥", url=f"payping.ir/d/WiZG")
                            ]
                        ]
                    ),
                    parse_mode="HTML",
                    disable_web_page_preview=True)
        

@StreamBot.on_message(filters.regex("🈳دیتاسنتر"))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.dc_id)
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        quote=True,
)
  
    
@StreamBot.on_message(filters.regex("پینگ🅿️"))
async def ping(b, m):
    start_t = time.time()
    ag = await m.reply_text("....")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await ag.edit(f"📈پینگ ربات هم اکنون:\n\n⏱{time_taken_s:.3f} ms\n\n🆔 @King_Network7")
    
    
    
    
@StreamBot.on_message(filters.private & filters.regex("Ⓜ️وضعیت کلیⓂ️"))
async def stats(bot, update):
  currentTime = readable_time((time.time() - StartTime))
  total, used, free = shutil.disk_usage('.')
  total = get_readable_file_size(total)
  used = get_readable_file_size(used)
  free = get_readable_file_size(free)
  sent = get_readable_file_size(psutil.net_io_counters().bytes_sent)
  recv = get_readable_file_size(psutil.net_io_counters().bytes_recv)
  cpuUsage = psutil.cpu_percent(interval=0.5)
  memory = psutil.virtual_memory().percent
  disk = psutil.disk_usage('/').percent
  botstats = f'⚛️آپ تایم : {currentTime}\n' \
            f'📊فضا سرور: {total}\n' \
            f'📈فضا استفاده شده: {used}\n' \
            f'📉فضا باقی مانده: {free}\n\n' \
            f'⏱CPU: {cpuUsage}%\n' \
            f'⏱RAM: {memory}%\n' \
            f'🗃Disk: {disk}%\n\n 🆔 @King_Network7'
  await update.reply_text(botstats)

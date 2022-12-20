import time
import psutil
import asyncio
import datetime
from config import *
from aiogram.utils import executor
from aiogram import Bot, Dispatcher, types

bot = Bot(token=BOT_TOKEN)

# ps aux | grep mysql

async def send_message(message):
    await bot.send_message(ADMIN_ACCOUNT_ID, message)
    await bot.close()

def get_cpu_usage():
  return psutil.cpu_percent()

def get_memory_usage():
  return psutil.virtual_memory().percent

def get_disk_usage():
  return psutil.disk_usage('/').percent

while True:
  date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  cpu_usage = get_cpu_usage()
  memory_usage = get_memory_usage()
  disk_usage = get_disk_usage()

  print(f"{date} | CPU: {cpu_usage} | Memory: {memory_usage} | Disk: {disk_usage}")
  
  if cpu_usage >= CPU_MAX_PERCENT:
    asyncio.run(send_message(f"պրոցեսորը ծանրաբեռնված է | {cpu_usage}%"))
  
  elif memory_usage >= MEMORY_MAX_PERCENT:
    asyncio.run(send_message(f"օպերատիվ հիշողությունը ծանրաբեռնված է | {memory_usage}%"))

  elif disk_usage >= DISK_MAX_PERCENT:
    asyncio.run(send_message(f"դիսկը լցվել է | {disk_usage}%"))

  time.sleep(UPDATE_INTERVAL)

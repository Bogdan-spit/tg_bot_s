import aiogram
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, ReplyKeyboardRemove


import viivodd
import KNOPOCHKI
import VINTS


import asyncio  
import logging  
from aiogram import Bot, Dispatcher, types  
from aiogram.filters.command import Command  
from configs import Config 
from aiogram.utils.keyboard import ReplyKeyboardBuilder 
from aiogram.utils.keyboard import InlineKeyboardBuilder 
import sqlite3


logging.basicConfig(level=logging.INFO)  
bot = Bot(token="TOKEN")  
dp = Dispatcher()  




async def main():  
    dp.include_router(viivodd.router)
    dp.include_router(KNOPOCHKI.router)
    dp.include_router(VINTS.router)
    await dp.start_polling(bot) 
    

if __name__ == "__main__":  
    asyncio.run(main())

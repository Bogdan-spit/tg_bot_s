import asyncio  
import logging  
from aiogram import Bot, Dispatcher, types  
from aiogram.filters.command import Command  
from configs import Config 
from aiogram import F, Router 
from random import randint 
from aiogram.utils.keyboard import ReplyKeyboardBuilder 
from aiogram.utils.keyboard import InlineKeyboardBuilder 
import sqlite3





router = Router()



@router.message(F.text.lower() == "винт") 
async def argegergerg(message: types.Message): 
    builder = InlineKeyboardBuilder() 
    builder.row( 
        types.InlineKeyboardButton(text="Остановка", callback_data="A1" 
        ), 
    ) 
    builder.row( 
        types.InlineKeyboardButton(text="Накат", callback_data="B1"), 
    )

    builder.row( 
        types.InlineKeyboardButton(text="Оттяжка", callback_data="C1"), 
    )
    await message.answer(text="Ответ в формате текста", reply_markup=builder.as_markup())

@router.message(F.text.lower() == "ближние") 
async def first_aid(message: types.Message): 
    builder = InlineKeyboardBuilder() 
    builder.row( 
        types.InlineKeyboardButton(text="Центр", callback_data="AA1" 
        ), 
    ) 
    builder.row( 
        types.InlineKeyboardButton(text="Угол", callback_data="BB1"), 
    )
    await message.answer(text="Ответ в формате текста", reply_markup=builder.as_markup())




@router.message(F.text.lower() == "классика") 
async def first_aid(message: types.Message): 
    builder = InlineKeyboardBuilder() 
    builder.row( 
        types.InlineKeyboardButton(text="Упражнение №1", callback_data="AA2" 
        ), 
    ) 
    builder.row( 
        types.InlineKeyboardButton(text="Упражнение №2", callback_data="BB2"), 
    )
    await message.answer(text="Ответ в формате текста", reply_markup=builder.as_markup())
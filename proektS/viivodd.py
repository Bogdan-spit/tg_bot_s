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

from ansewrsss import *





router = Router()


@router.message(F.text.lower() == "стойка") 
async def stoyka(message: types.Message): 
    await message.answer(
        text = ansewrsa['A1'])
    



@router.message(F.text.lower() == "сила") 
async def stoyka(message: types.Message): 
    await message.answer(
        text = ansewrsa['A2'])
    



@router.message(F.text.lower() == "остановка") 
async def stoyka(message: types.Message): 
    await message.answer(
        text = ansewrsa['A2'])
    
@router.message(F.text.lower() == "накат") 
async def stoyka(message: types.Message): 
    await message.answer(
        text = ansewrsa['A2'])
    

@router.message(F.text.lower() == "оттяжка") 
async def stoyka(message: types.Message): 
    await message.answer(
        text = ansewrsa['A2'])




@router.message(F.text.lower() == "дальние") 
async def stoyka(message: types.Message): 
    await message.answer(
        text = ansewrsa['A2'])
    

@router.message(F.text.lower() == "центр") 
async def stoyka(message: types.Message): 
    await message.answer(
        text = ansewrsa['A2'])
    

@router.message(F.text.lower() == "угол") 
async def stoyka(message: types.Message): 
    await message.answer(
        text = ansewrsa['A2'])
    

@router.message(F.text.lower() == "от пирамиды") 
async def stoyka(message: types.Message): 
    await message.answer(
        text = ansewrsa['A2'])
    






##############################################################

@router.callback_query(F.data == "A1") 
async def send_random_value(callback: types.CallbackQuery): 
    await callback.message.answer(
        text = ansewrsa['A1'])
    


@router.callback_query(F.data == "B1") 
async def send_random_value(callback: types.CallbackQuery): 
    await callback.message.answer(
        text = ansewrsa['B4'])
    



@router.callback_query(F.data == "C1") 
async def send_random_value(callback: types.CallbackQuery): 
    await callback.message.answer(
        text = ansewrsa['B4'])
    




@router.callback_query(F.data == "AA1") 
async def send_random_value(callback: types.CallbackQuery): 
    await callback.message.answer(
        text = ansewrsa['B4'])
    


@router.callback_query(F.data == "BB1") 
async def send_random_value(callback: types.CallbackQuery): 
    await callback.message.answer(
        text = ansewrsa['B4'])
    


@router.callback_query(F.data == "AA2") 
async def send_random_value(callback: types.CallbackQuery): 
    await callback.message.answer(
        text = ansewrsa['B4'])
    


@router.callback_query(F.data == "BB2") 
async def send_random_value(callback: types.CallbackQuery): 
    await callback.message.answer(
        text = ansewrsa['B4'])
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


@router.message(Command("start")) 
async def cmd_start(message: types.Message): 
    kb = [ 
        [ 
            
            types.KeyboardButton(text="Техника"),
            types.KeyboardButton(text="Удары"),
            
            
        ], 
    ] 
    keyboard = types.ReplyKeyboardMarkup( 
        keyboard=kb, 
        resize_keyboard=True, 
        input_field_placeholder="Текст вместо 'Massage'" 
    ) 
    await message.answer("Опции кнопок клавиатуры?", reply_markup=keyboard) 



@router.message(F.text.lower() == "техника") 
async def cmd_special_buttons(message: types.Message): 
    builder = ReplyKeyboardBuilder() 
    builder.row( 
        types.KeyboardButton(text="Стойка"), 
        types.KeyboardButton(text="Сила"), 
        types.KeyboardButton(text="Винт"),

    ) 

    builder.row( 
        types.KeyboardButton(text="Назад") 
    ) 

    await message.answer( 
        "Выберите действие:", 
        reply_markup=builder.as_markup(resize_keyboard=True), 
    ) 





@router.message(F.text.lower() == "назад") 
async def with_puree(message: types.Message): 
    kb = [ 
        [ 
        types.KeyboardButton(text="Техника"), 
        types.KeyboardButton(text="Удары"), 


        ], 
    ] 
    keyboard = types.ReplyKeyboardMarkup( 
        keyboard=kb, 
        resize_keyboard=True, 
        input_field_placeholder="Текст вместо 'Massage'" 
    ) 
    await message.reply("Мы снова здесь", reply_markup=keyboard) 
















@router.message(F.text.lower() == "удары") 
async def cmd_special_buttons(message: types.Message): 
    builder = ReplyKeyboardBuilder() 
    builder.row( 
        types.KeyboardButton(text="Свои"), 
        types.KeyboardButton(text="Чужие"), 
        types.KeyboardButton(text="Отыгрыш"),


    ) 

    builder.row( 
        types.KeyboardButton(text="Назад1") 
    ) 

    await message.answer( 
        "Выберите действие:", 
        reply_markup=builder.as_markup(resize_keyboard=True), 
    ) 

@router.message(F.text.lower() == "назад1") 
async def with_puree(message: types.Message): 
    kb = [ 
        [ 
        types.KeyboardButton(text="Техника"), 
        types.KeyboardButton(text="Удары"), 


        ], 
    ] 
    keyboard = types.ReplyKeyboardMarkup( 
        keyboard=kb, 
        resize_keyboard=True, 
        input_field_placeholder="Текст вместо 'Massage'" 
    ) 
    await message.reply("Мы снова здесь", reply_markup=keyboard) 



@router.message(F.text.lower() == "свои") 
async def cmd_special_buttons(message: types.Message): 
    builder = ReplyKeyboardBuilder() 
    builder.row( 
        types.KeyboardButton(text="Дальние"), 
        types.KeyboardButton(text="Ближние"), 



    ) 

    builder.row( 
        types.KeyboardButton(text="Назад2") 
    ) 

    await message.answer( 
        "Выберите действие:", 
        reply_markup=builder.as_markup(resize_keyboard=True), 
    ) 


@router.message(F.text.lower() == "назад2") 
async def with_puree(message: types.Message): 
    kb = [ 
        [ 
        types.KeyboardButton(text="Свои"), 
        types.KeyboardButton(text="Чужие"), 
        types.KeyboardButton(text="Отыгрыш"),


        ], 
    ] 
    keyboard = types.ReplyKeyboardMarkup( 
        keyboard=kb, 
        resize_keyboard=True, 
        input_field_placeholder="Текст вместо 'Massage'" 
    ) 
    await message.reply("Мы снова здесь", reply_markup=keyboard) 



@router.message(F.text.lower() == "чужие") 
async def cmd_special_buttons(message: types.Message): 
    builder = ReplyKeyboardBuilder() 
    builder.row( 
        types.KeyboardButton(text="Центр"), 
        types.KeyboardButton(text="Угол"), 



    ) 

    builder.row( 
        types.KeyboardButton(text="Назад2") 
    ) 

    await message.answer( 
        "Выберите действие:", 
        reply_markup=builder.as_markup(resize_keyboard=True), 
    ) 


@router.message(F.text.lower() == "отыгрыш") 
async def cmd_special_buttons(message: types.Message): 
    builder = ReplyKeyboardBuilder() 
    builder.row( 
        types.KeyboardButton(text="От пирамиды"), 
        types.KeyboardButton(text="Классика"), 

    ) 

    builder.row( 
        types.KeyboardButton(text="Назад2") 
    ) 

    await message.answer( 
        "Выберите действие:", 
        reply_markup=builder.as_markup(resize_keyboard=True), 
    ) 
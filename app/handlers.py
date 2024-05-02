from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
import json

import get_weather

r = Router()

@r.message(Command('start'))
async def cmd_start(mes: Message):
    await mes.answer_photo(photo='https://lh3.googleusercontent.com/QdEZqnh_9V3ijSuDirL6DA5M_S7-EjbIv2WhIu5TGm4VjuRyf684HgU9jJPU6Qjx18FH', caption=f'Привет, {mes.from_user.full_name}.\nЭтот бот способен показывать погоду в любом городе/стране/регионе.\nНапишите сюда любой город')

@r.message(F.text)
async def cmd_start(mes: Message):
    get_weather.get_weat(mes.text)
    with open('app/weather.json', 'r') as file:
        data = json.load(file)
        
    try:
        temp = data['main']['temp']
        feels_like_temp = data['main']['feels_like']
        weather =  data['weather'][0]['description'][0].upper() + data['weather'][0]['description'][1:]
        humidity = data['main']['humidity']
    except KeyError:
        await mes.answer(f"""Ошибка. Данного города/региона/странны не существует.\nПопробуйте еще раз.""")
    await mes.answer(f"""
Температура: {temp}°
Чуствуется как: {feels_like_temp}°
Погода: {weather}
Влажность: {humidity}%""")
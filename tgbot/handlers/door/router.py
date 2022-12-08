import requests

from aiogram import Router, types, Bot
from aiogram.filters import Command


door_router = Router()


@door_router.message(Command(commands=["start"]))
async def command_start_handler(message: types.Message) -> None:
    await message.answer('Hello')


@door_router.message()
async def save_video(message: types.Message, bot: Bot):
    # TODO: Добавить обработку неправильных расширений. Поддерживается только mp4
    # TODO: Вынести baseUrl в .env
    file = await bot.get_file(message.video.file_id)
    file_path = file.file_path

    url = 'http://127.0.0.1:8000/video'
    requests.post(url, json={ "file_path": file_path })

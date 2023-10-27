from aiogram import Bot, Dispatcher, executor, types
from random import choice
from string import ascii_lowercase

from aiogram.types import InputFile
from pytube import YouTube


API_TOKEN ="6394051020:AAGXjpqe1Riyqrn04NaIq7k6DFJ3ViEKL1M"
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

def url_checker(text):
    if 'you' in text.lower():
        _type = 'youtube'
    else:
        _type = 'other'
    return _type



def Download(host_type:str,file_name: str, link:str):
    if host_type == 'youtube':
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        try:
            youtubeObject.download(filename=f"{file_name}.mp4")
        except:
            print("Xatolik yuz berdi")
        print("yuklandi")
        data = f"""
    🎞 Video Nomi {youtubeObject.title}\n\n💡 Video Sifati {youtubeObject.resolution} \n\n♻️ Video hajmi {youtubeObject.filesize_mb} mb
    """
        return {"type":data,"hosting":"youtube"}

def rand():
    result_str = ''.join(choice(ascii_lowercase) for i in range(5))
    return result_str
@dp.message_handler(content_types=['text'])
async def save_bot(message: types.Message):
    x = rand()
    host_type = url_checker(text=message.text)
    data =  Download(host_type=host_type, file_name=x, link=message.text)
    if data:
        if data['hosting'] == 'youtube':
            doc = InputFile(path_or_bytesio=f"{x}.mp4")
            await bot.send_video(chat_id=message.chat.id,video=doc,caption=data['type'])

        else:
            await bot.send_message(chat_id=message.from_user.id,text="Xatolik")
    else:
        await bot.send_message(chat_id=message.from_user.id, text="Xatolik")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


import os
import sys

from telethon import TelegramClient
from telethon.tl.types import InputMessagesFilterPhotos
from telethon.tl.types import InputMessagesFilterPhotoVideo
import socks
import async_timeout

api_id = 123456789
api_hash = "17cbxxxxxxxx6ec8d79ba5f1031ee"
client = TelegramClient('anon', api_id, api_hash, proxy=(socks.SOCKS5, "localhost", 1080)).start()


async def video():
    messages = await client.get_messages(url, None, filter=InputMessagesFilterPhotoVideo)
    for video_ in messages:
        filename = video_path + "/" + str(video_.id) + ".mp4"
        await client.download_media(video_, filename)


async def photo():
    messages = await client.get_messages(url, None, filter=InputMessagesFilterPhotos)
    for photos in messages:
        filename = img_path + "/" + str(photos.id) + ".jpg"
        await client.download_media(photos, filename)
    client.disconnect()


if sys.argv[1] == "i":
    url = input("输入TG频道的链接：")
    img_path = "./img"
    os.mkdir("./img")
    with client:
        client.loop.run_until_complete(video())
elif sys.argv[1] == "v":
    url = input("输入TG频道的链接：")
    video_path = "./video"
    os.mkdir("./video")
    with client:
        client.loop.run_until_complete(video())
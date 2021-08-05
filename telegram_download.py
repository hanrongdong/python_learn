import os
import sys
from telethon import TelegramClient
from telethon.tl.types import InputMessagesFilterPhotos
from telethon.tl.types import InputMessagesFilterPhotoVideo
import socks
import async_timeout

proxy = (socks.SOCKS5, "localhost", 7890)

api_id = 79033333
api_hash = "17cb1xa6ec8d79ba5f1031ee"
client = TelegramClient('anon', api_id, api_hash, proxy=proxy).start()


async def video():
    messages = await client.get_messages(url, None, filter=InputMessagesFilterPhotoVideo)
    for video_ in messages:
        filename = video_path + "/" + str(video_.id) + ".mp4"
        if os.path.exists(filename):
            print("文件存在")
            continue
        await client.download_media(video_, filename)
        client.disconnect()


async def photo():
    messages = await client.get_messages(url, None, filter=InputMessagesFilterPhotos)
    for photos in messages:
        filename = img_path + "/" + str(photos.id) + ".jpg"
        if os.path.exists(filename):
            print("文件存在")
            continue
        await client.download_media(photos, filename)
        client.disconnect()


if sys.argv[1] == "i":
    url = input("输入TG频道的链接：")
    img_path = "/Users/zhoupeng/Downloads/img"
    try:
        os.mkdir("/Users/zhoupeng/Downloads/img")
    except Exception:
        print("文件夹存在，无需创建")
    with client:
        client.loop.run_until_complete(photo())
elif sys.argv[1] == "v":
    url = input("输入TG频道的链接：")
    video_path = "/Users/zhoupeng/Downloads/video"
    try:
        os.mkdir("/Users/zhoupeng/Downloads/video")
    except Exception:
        print("文件夹存在，无需创建")
    with client:
        client.loop.run_until_complete(video())
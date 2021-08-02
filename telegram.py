from telethon import TelegramClient
from telethon.tl.types import InputMessagesFilterUrl
import re
import download_tg_blog

api_id = 7907595
api_hash = "17cb117ecb3392a6ec8d79ba5f1031ee"
# 链接服务端
client = TelegramClient('anon', api_id, api_hash).start()


async def main():
    messages = await client.get_messages("https://t.me/AnchorPic", None, filter=InputMessagesFilterUrl)
    for i in messages:
        regex = re.findall(r"([a-zA-z]+://[^\s]*-..)", str(i))
        try:
            with open("url.txt", "a") as f:
                f.write(regex[0] + "\n")
        except Exception:
            continue
with client:
    client.loop.run_until_complete(main())

download_tg_blog.run()
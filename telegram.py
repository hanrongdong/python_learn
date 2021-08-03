from telethon import TelegramClient
from telethon.tl.types import InputMessagesFilterUrl
import re
import download_tg_blog

api_id = 123456
api_hash = "17cb117ecb3392a6ec8d79bfgvbf1031ee"
# 链接服务端
client = TelegramClient('anon', api_id, api_hash).start()

URL = input("输入TG频道链接：")
async def main():
    messages = await client.get_messages(URL, None, filter=InputMessagesFilterUrl)
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

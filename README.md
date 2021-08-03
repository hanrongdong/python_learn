# telegram.py and download_tg_blog.py
1. 首先申请api，api申请地址：https://my.telegram.org/
2. 然后填入telegram.py的`api_id`和`api_hash`中
3. 需要爬不同的频道修改`telegram.py`中下面这一行的频道链接
```python
messages = await client.get_messages("https://t.me/AnchorPic", None, filter=InputMessagesFilterUrl)
```
4. 开始运行
`python3 ./telegram.py`

# telegram_download.py
1. 有两个参数：`i` and `v`
```python
python3 telegram_download.py i # 下载频道的所有图片
python3 telegram_download.py v # 下载频道的所有视频
```

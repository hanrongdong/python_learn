# pyhton_learn
首先申请api
然后填入telegram.py的`api_id`和`api_hash`中
api申请地址：https://my.telegram.org/
需要爬不同的频道修改下面这一行的频道链接
```python
messages = await client.get_messages("https://t.me/AnchorPic", None, filter=InputMessagesFilterUrl)
```

开始运行
`python3 ./telegram.py`

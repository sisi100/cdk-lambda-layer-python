import hello
import requests


def handler(event, context):
    print(requests.get("https://blog.i-tale.jp/").text)
    print(hello.greeting())
    return

import hello
import requests


def handler(event, context):
    print(requests.get("https://blog.i-tale.jp/").status_code)
    print(hello.greeting())
    return

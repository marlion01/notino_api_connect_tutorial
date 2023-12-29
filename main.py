from notion_client import Client
import os
import requests
if __name__=="__main__":
    print("hello world")
    r=requests.get('https://api.notion.com')
    print(r.text)
import requests
from bs4 import BeautifulSoup
from model.screping_yahoo import screping_yahoo


def screping_yahoo_main():
    items=screping_yahoo("sc-1nhdoj2-0")
    
    print(items)

    datas=[]

    for item in items:
        url=item.find("a").get("href")
        title=item.find("a").text
        data={
            "url":url,
            "title":title
        }
        
        datas.append(data)
    
    return datas
   
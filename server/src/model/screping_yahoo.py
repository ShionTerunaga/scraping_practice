import requests
from bs4 import BeautifulSoup

def screping_yahoo(class_name:str):
    r = requests.get("https://news.yahoo.co.jp/")

    soup = BeautifulSoup(r.content, "html.parser")

    items=soup.find_all("li",class_name)

    return items
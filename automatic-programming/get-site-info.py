import requests
from bs4 import BeautifulSoup

url = 'https://mart.baemin.com/goods/list/100067'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser') 
    title = soup.select('div.sc-yEDbz.izOGgw > p.sc-enTqHk.gVANIR')
    for eachTitle in title:
        print(eachTitle.text)
    # print(title)
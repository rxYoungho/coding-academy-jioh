import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
from time import sleep
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager as CM

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup


html = requests.get("https://mart.baemin.com").text

print(html)
# soup = BeautifulSoup(html.read(), "html.parser")

import re
# as per recommendation from @freylis, compile once only
CLEANR = re.compile('<.*?>') 

def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext

def megacoffee_products(keyword, pages, category, fileName):
    
     # Selenium config
    options = webdriver.ChromeOptions()

    mobile_emulation = {
        "userAgent": 'Mozilla/5.0 (Linux; Android 4.0.3; HTC One X Build/IML74K) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/99.0.4844.51 Mobile Safari/535.19'
    }
    # options.add_experimental_option("mobileEmulation", mobile_emulation)

    driver = webdriver.Chrome(executable_path=CM().install(), options=options)
    driver.set_window_position(0, 0)
    driver.set_window_size(1200, 800)

    f = open(f"{fileName}.csv", 'w', encoding='utf-8')
    wr = csv.writer(f)
    baseurl = "https://mart.baemin.com"
    headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
    # cateCd = 카테고리 번호 005 = 시럽
    
    
    for page in range(0, pages+1):
        tot_product_name = []
        tot_product_price = []
        tot_product_link = []    
        url = f"https://mart.baemin.com/goods/list/{keyword}?p={page}"        
        driver.get(url) # 해당 URL로 브라우저 창을 실행
        WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".sc-czETjp.gZEqge"))) #index라는 id를 가진 요소가 로딩될 때 까지 기다림
        html = driver.page_source
        
        soup = BeautifulSoup(html, 'html.parser')

        # 상품 이름 추출하기
        product_name = soup.select('a > div.sc-yEDbz.izOGgw > p.sc-enTqHk.gVANIR')
        # print("P입니다:", product_name)
        for name in product_name:
            tot_product_name.append(name.text)
        # print("P:",tot_product_name)

        # 상품 가격 추출하기
        product_price = soup.select('div.sc-yEDbz.izOGgw > div > p.sc-czETjp.gZEqge')
        
        # 상품 구매 링크 추출하기
        product_link = soup.select('div.sc-hWZktu.eJuFsj > section > div > a')
        for each in product_link:
            # print(each)
            a = each['href']
            
            tot_product_link.append(baseurl+a)

        for product in product_name:
            tot_product_name.append(product.text)
        
        for price in product_price:
            a = price.text.replace("\n", "")
            a = a.replace("\t", "")
            a = a.replace("원", "")
            a = a.replace(" ", "")
            tot_product_price.append(a)

        for name, price, link in zip(tot_product_name, tot_product_price, tot_product_link):
            wr.writerow([name, price, link])
        print(tot_product_name[-1], tot_product_price[-1], tot_product_link[-1])
    # print(category)
    # print(tot_product_price)
    # print(tot_product_name)
    # print(tot_product_link)
    f.close()
    

megacoffee_products('100197', 2, "포장용기", "배민상회_포장용기") # 시럽/소스/파우더/스무디 총 (5,351)개의 상품이 있습니다.
# megacoffee_products('100776', 9, "커피용품", "배민상회_카페용품") # 커피,티용품/모카포트/악세사리 총 (1,081)개의 상품이 있습니다.
# megacoffee_products('100105', 6, "종이용기/박스", "배민상회_종이용기") # 시럽/소스/파우더/스무디 총 (5,351)개의 상품이 있습니다.
# megacoffee_products('100952', 2, "주방잡화", "배민상회_주방잡화") # 커피,티용품/모카포트/악세사리 총 (1,081)개의 상품이 있습니다.
# megacoffee_products('101223', 1, "주방설비", "배민상회_주방설비") # 시럽/소스/파우더/스무디 총 (5,351)개의 상품이 있습니다.
# megacoffee_products('101105', 2, "포장랩/위생백/호일", "배민상회_포장,위생,호일") # 커피,티용품/모카포트/악세사리 총 (1,081)개의 상품이 있습니다.

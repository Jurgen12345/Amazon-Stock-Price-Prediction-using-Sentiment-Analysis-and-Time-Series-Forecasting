#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd
import numpy as np

url = 'https://www.investing.com/equities/amazon-com-inc-news'

path = '/home/smagns/Downloads/chromedriver-linux64/chromedriver'

service = Service(executable_path=path)
options = Options()
options.add_experimental_option('detach',True)
#options.add_argument('--headless')

all_articles = []
page_counter = 1
articles = []


while  page_counter <= 1000 :
    try:
        driver = webdriver.Chrome(service=service,options=options)
        print("Driver eshte krijuar pa problem")
        url_other = "https://www.investing.com/equities/amazon-com-inc-news/{}".format(page_counter)
        if(page_counter > 1):
            driver.get(url_other)
            print("Driveri ka hapur page_counter me te madh se 1")
        elif(page_counter == 1):
            driver.get(url)
            print("Driver ka hapur page_counter te barabarte me 1")
        articles = driver.find_elements(By.XPATH, "//article[@data-test]")
        for article in articles:
            title = article.text.strip()
            all_articles.append(title)
        page_counter +=1
        print(len(all_articles))
        driver.quit()
    except Exception:
        print("Something went wrong")
        break
dataframe = pd.DataFrame(all_articles)

print('\n DATAFRAME \n')
print(len(dataframe.columns))

print('\n DATAFRAME \n')
print(dataframe.head(10))

dataframe.to_csv("AMAZON_NEWS_HEADLINES.csv", index = False)


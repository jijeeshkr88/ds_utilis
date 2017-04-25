import sys
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def get_url(url,modelno):
    driver = webdriver.Firefox()
    url = "https://www.newegg.com/"
    driver.get(url)
    time.sleep(2)
    enter_text = driver.find_element_by_xpath('//*[@id="haQuickSearchBox"]')
    enter_text.send_keys(modelno)
    enter_text.send_keys(Keys.ENTER)
    time.sleep(2)
    first_product_click = driver.find_element_by_xpath('//*[@id="bodyArea"]/section/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/a').click()
    time.sleep(2)
    new_path = driver.current_url
    driver.quit()
    return new_path

def get_details(new_url):
    res = requests.get(new_url)
    html_str = res.content
    bs_obj = BeautifulSoup(res.content, 'html.parser')
    data1 = bs_obj.findAll("div", { "class" : "grpBullet" })
    data2 = bs_obj.findAll("div", { "class" : "itemDesc" })
    return data1[0].contents,data2[0].contents 

if __name__ == '__main__': 
    url = "https://www.newegg.com/"
    modelno = "lenovo thinkpad x1"
    new_url = get_url(url,modelno)
    print(get_details(new_url))



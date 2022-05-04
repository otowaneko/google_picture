#事前準備。
import os
print("請輸入檔案位置")
folder_path = str(input())

all_content = [] 

def show_folder_content(folder_path):
    print(folder_path + '資料夾內容：')

    folder_content = os.listdir(folder_path)
    for item in folder_content:
        if os.path.isdir(folder_path + '/' + item):
            print('資料夾：' + item)

            
            show_folder_content(folder_path + '/' + item) #呼叫自己處理這個子資料夾
        elif os.path.isfile(folder_path + '/' + item):
            print('檔案：' + item)
            all_content.append(str(folder_path + '/' + item)) #將是檔案的檔案位置存放入"all_content"之中
        else:
            print('無法辨識：' + item)

if (os.path.isdir(folder_path)):
    show_folder_content(folder_path) #若使用者輸入為資料夾位置，則用方法"show_folder_content"將檔案位置一一找出
else:
    all_content.append(folder_path) #若為單一檔案直接存入"all_content"以備等等爬蟲

print()
print()

'''
-----------------------------------我是分隔線-----------------------------------
'''

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

#打開瀏覽器
browser=webdriver.Chrome()
browser.implicitly_wait(10)
url="https://images.google.com/"
browser.get(url)

#上傳圖片
for i in all_content:
    browser.implicitly_wait(10)
    browser.find_element_by_css_selector('#sbtc > div > div.dRYYxd > div.ZaFQO').click()
    browser.find_element_by_css_selector('#awyMjb').send_keys(i)

    result = []
    u=[]

#爬是否為網路上的圖片
    soup = BeautifulSoup(browser.page_source,'html.parser')
    
    #找尋頁面中需要的資訊
    for tag in soup.findAll('div',{'class':"tF2Cxc"}):
        if tag.find('div',{'class':'yuRUbf'}):
            uwu=tag.find('a')
            qwq=uwu.get('href')
            u.append(qwq)
        if tag.find('div',{'class':'fWhgmd'}):
            result.append('T')
        else:
            result.append('F')


#判斷函式
    def t(result):
        count1 = 0
        count2 = 0
        for x in result:
            if x == 'F':
                count1 += 1
            else:
                count2 += 1
        if count1 > count2:
            return False
        else:
            return True
    
#印出結果
    if(t(result) == False):
        print("'" + i + "'" + " 不是網路上")
    else:
        print("'" + i + "'" + " 網路上的")
        for i in range(len(result)):
            if result[i]=='T':
                print(u[i])
                
    print()

#延遲後返回前一頁重新繼續。
    browser.implicitly_wait(10)
    browser.back()

browser.close() #關閉瀏覽器

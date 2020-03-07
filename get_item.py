#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Legal Disclaimer
Academic purposes only
This code can ONLY be used to download a small amount of data
with limited speed.
Make sure access to data is authorized,
and do not cause disturbance to the network service.
'''

# Central player here
from selenium import webdriver as wd

# Accessories
import time
import sys
import json
import numpy as np
import pandas as pd

# constants
driver = wd.Chrome()
main_page = "https://www.itjuzi.com/search-pro"

# sleepers
after_open_sleep = 5
login_sleep = 35
search_sleep = 30
page_sleep = 5

def create_cookie():
   '''
   This part is for login and creating cookie
   '''
   # Open the browser
   driver.get(main_page)
   time.sleep(after_open_sleep)
   sys.stdout.write("CHECKER: 初始网页需要已经成功打开\n")

   # Login
   sys.stderr.write("请在{}秒的时间内，在打开的页面中手动登录\n".format(login_sleep))
   time.sleep(login_sleep)

   # Reload main page
   #  driver.get(main_page)
   cookie_items = driver.get_cookies()
   # 获取到的cookies是列表形式，将cookies转成json形式并存入本地名为cookie的文本中
   with open('cookie.json', 'w', encoding='utf-8') as f:
      post = {item['name']: item['value'] for item in cookie_items}
      # Prolong the dictionary
      cookie_str = json.dumps(post)
      f.write(cookie_str)
   sys.stdout.write("CHECKER: cookies信息已保存到本地cookie.json文件\n")
   sys.stdout.write("CHECKER: 登录完毕！\n")

def search_for_items():
   '''
   Function to make the page to the searching area
   '''
   sys.stderr.write("请在{}秒的时间内，在打开的页面中输入搜索内容\n".format(search_sleep))
   time.sleep(search_sleep)
   sys.stdout.write("搜索结果页面已经应该打开，请不要点击任何按钮\n")
   sys.stdout.write("如果没有打开，请立刻终止程序\n")

def next_page():
   '''
   Mark: return false if the "next_page" button is disabled
   '''
   button_xpath = "//button[@class=\'btn-next\']"
   button_next_page = driver.find_element_by_xpath(button_xpath)
   button_next_page.click()
   has_next_page = not button_next_page.get_property("disabled")
   sys.stdout.write("Page Turned\n")
   time.sleep(page_sleep)
   return has_next_page

def save_data():
   table_xpath = "//table[@class=\'el-table__body\']/tbody/tr"
   tr_list = driver.find_elements_by_xpath(table_xpath)
   number_of_cols = len(tr_list)
   if number_of_cols%2!=0:
      sys.stderr.write("ERROR in saving data\n")
      print(text_list)
      return ([],[])
   number_of_cols = number_of_cols // 2
   raw_info = []
   for tr in tr_list:
      grid = tr.find_elements_by_tag_name('td')
      raw_info.append([i.text for i in grid])
   for i in range(number_of_cols):
      raw_info[i][0] = raw_info[i+number_of_cols][0]
   raw_info = raw_info[:number_of_cols]
   time.sleep(page_sleep)
   return raw_info

def main():
   page = 1
   file = 1
   all_data = []
   create_cookie()
   search_for_items()
   all_data.extend(save_data())
   while(next_page()):
      print("-----------NEW page: {}-------------".format(page))
      all_data.extend(save_data())
      if page%18==0:
         temp_data_frame = pd.DataFrame(all_data)
         all_data = []
         temp_data_frame.to_csv("result_{}.csv".format(file))
         file+=1
      page += 1
   temp_data_frame = pd.DataFrame(all_data)
   temp_data_frame.to_csv("result_{}".format(file))
   driver.quit()


if __name__ == '__main__':
   main()

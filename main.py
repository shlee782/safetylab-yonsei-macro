import sys
import os
import time

import pandas as pd
from math import ceil

import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By

from datetime import datetime

def removePopup(browser: webdriver, parent):
    uselessWindows = browser.window_handles
    for winId in uselessWindows:
        if winId != parent:
            browser.switch_to.window(winId)
            browser.close()
    browser.switch_to.window(parent)

def week_of_month(dt):
    """ Returns the week of the month for the specified date."""
    first_day = dt.replace(day=1)

    dom = dt.day
    adjusted_dom = dom + (1 + first_day.weekday()) % 7

    return int(ceil(adjusted_dom/7.0))

def main():
    print('day: ', end='')
    day = input()
    print('check type: ', end='')
    check_type = input()

    f = open('./input.txt', 'r', encoding='UTF-8')

    year = f.readline().split(' ')[1]
    month = f.readline().split(' ')[1]
    id = f.readline().split(' ')[1]
    name = f.readline().split(' ')[1]
    check_list = f.readline().rstrip('\n').split(' ')[1:]
    lab = f.readline().split(' ')[1]

    browser = webdriver.Chrome()
    browser.get('https://safetylab.yonsei.ac.kr/Account/LogOn?ReturnUrl=%2f')
    parent = browser.current_window_handle
    removePopup(browser=browser, parent=parent)
    # browser.implicitly_wait(1)

    elm = browser.find_element(By.NAME, 'UniqueKey')
    elm.send_keys(id)
    elm = browser.find_element(By.NAME, 'UserName')
    elm.send_keys(name)
    #elm.send_keys(Keys.RETURN)``
    elm = browser.find_element(By.XPATH, '//*[@id="whole_wrap"]/div[2]/div/div[2]/div[1]/div/form/div/div/a/img')
    elm.click()
    browser.implicitly_wait(1)
    removePopup(browser=browser, parent=parent)

    time.sleep(1)

    elm = browser.find_element(By.XPATH, '//*[@id="whole_wrap"]/div[1]/div/div[5]/ul/li[1]/a')
    elm.click()
    removePopup(browser=browser, parent=parent)

    elm = browser.find_element(By.XPATH, '//*[@id="ddlMyLabList"]/option[' + lab + ']')
    elm.click()

    check_date = pd.Timestamp(year+'-'+month+'-'+day)

    weeknum = week_of_month(check_date)
    daynum = int(check_date.strftime('%w'))

    check_date_xpath = '//*[@id="dtpicker"]/div/table/tbody/tr[' + str(weeknum) + ']/td[' + str(daynum+1) + ']/a'

    browser.find_element(By.XPATH, check_date_xpath).click()

    browser.find_element(By.ID, 'contents').click()
    if check_type == 'a':
        browser.find_element(By.XPATH, '//*[@id="subCont"]/div/div[2]/a[2]').click()
        browser.find_element(By.XPATH, '//*[@id="25_' + check_list[0] + '"]').click()
        browser.find_element(By.XPATH, '//*[@id="26_' + check_list[1] + '"]').click()
        browser.find_element(By.XPATH, '//*[@id="27_' + check_list[2] + '"]').click()
        browser.find_element(By.XPATH, '//*[@id="28_' + check_list[3] + '"]').click()
        browser.find_element(By.XPATH, '//*[@id="29_' + check_list[4] + '"]').click()
        browser.find_element(By.XPATH, '//*[@id="30_' + check_list[5] + '"]').click()
        browser.find_element(By.XPATH, '//*[@id="31_' + check_list[6] + '"]').click()
        browser.find_element(By.XPATH, '// *[ @ id = "btnSave"] / img').click()        

        alert = browser.switch_to.alert
        alert.accept()       
    elif check_type == 'b':
        browser.find_element(By.XPATH, '//*[@id="subCont"]/div/div[2]/a[1]/img').click()
    
    time.sleep(1)
    browser.refresh()
    time.sleep(5)

if __name__ == "__main__":
    main()
import time
import csv
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.action_chains import ActionChains

# Зайти на https://www.nseindia.com
driver= webdriver.Firefox(service=Service(r'C:\Program Files\Mozilla Firefoxx\geckodriver.exe'))
driver.get('https://www.nseindia.com/')
time.sleep(3)

# Навестись (hover) на MARKET DATA
market_data_menu = driver.find_element('xpath', '//*[@id="link_2"]')
actions = ActionChains(driver)
actions.move_to_element(market_data_menu).perform()
time.sleep(3)

# Кликнуть на Pre-Open Market 
pre_open_market = driver.find_element('xpath', '//*[@id="main_navbar"]/ul/li[3]/div/div[1]/div/div[1]/ul/li[1]/a')
pre_open_market.click()
time.sleep(3)


# Спарсить данные Final Price по всем позициям на странице и вывести их в csv файл.
with open('final_prices.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Price"])

for i in range(1, 51):
    name_element = driver.find_element('xpath', f'//*[@id="livePreTable"]/tbody/tr[{i}]/td[2]')
    price_element = driver.find_element('xpath', f'//*[@id="livePreTable"]/tbody/tr[{i}]/td[7]')
    print("Парсинг строки:", i)

    with open('final_prices.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name_element.text, price_element.text])


# Cымитировать небольшой пользовательский сценарий использования сайта      
driver.find_element('xpath', '//*[@id="link_0"]').click()
time.sleep(2)
driver.find_element('xpath', '//*[@id="tabList_NIFTYBANK"]').click()
time.sleep(2)
driver.execute_script("window.scrollBy(0, 500);")
time.sleep(5)
driver.find_element('xpath', '//*[@id="quickLinkBand"]/ul/li[2]/a').click()
time.sleep(2)
driver.find_element('xpath', '//*[@id="quickLinkBand"]/ul/li[3]/a').click()
time.sleep(4)
driver.find_element('xpath', '//*[@id="quickLinkBand"]/ul/li[3]/a').click()
time.sleep(1)
driver.find_element('xpath', '//*[@id="quickLinkBand"]/ul/li[1]/a').click()

# Закрываем браузер
time.sleep(5)
driver.quit()
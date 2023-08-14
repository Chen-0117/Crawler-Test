# selenium's find_element ways
# find_element(By.XPATH)
# find_element(By.CSS_SELECTOR)
# find_element(By.ID)
# find_element(By.TAG_NAME)

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://www.imooc.com/")
    name = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/div/div[1]/a[1]/p[1]').text
    # print(name)

#foreced to open a website leads to the decrease of crawler speed

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import time

def wifiautonomy():
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    option.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=option)
    driver.get('http://202.195.176.89/')
    sleep(1)

    ok = driver.find_elements(By.ID, 'ballTittle3')


    if len(ok) > 0:
        driver.quit()
        print("已连接")

    else:
        driver.implicitly_wait(1)
        element = driver.find_element(By.ID, "username")
        element.send_keys("21280108")


        pwdtp = driver.find_element(By.ID,'pwd_tip')
        ActionChains(driver).move_to_element(pwdtp).click(pwdtp).perform()

        pwd = driver.find_element(By.ID,"pwd")
        pwd.send_keys("200326")

        selectDisname = driver.find_element(By.ID,"selectDisname")
        ActionChains(driver).move_to_element(selectDisname).click(selectDisname).perform()
        _service_1 = driver.find_element(By.ID,"_service_1")
        ActionChains(driver).move_to_element(_service_1).click(_service_1).perform()


        element.send_keys(Keys.ENTER)
        sleep(1)
        ok = driver.find_elements(By.ID, 'ballTittle3')
        if len(ok) > 0:
            print("链接成功")
        else:
            print("连接失败")

def loop_func(func, second):
    while True:
        func()
        time.sleep(second)

loop_func(wifiautonomy, 120)
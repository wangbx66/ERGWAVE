import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

def close(driver):
    for window in driver.window_handles:
        driver.switch_to_window(window)
        driver.close()

if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path='/home/bxwang/chromedriver', service_log_path='/dev/null')
    driver.get('https://securelogin.wlan.cuhk.edu.hk/upload/custom/CU_Portal/login.html')
    time.sleep(0.5)
    elm = driver.find_element_by_name('user')
    elm.send_keys('s1155055730')
    elm = driver.find_element_by_name('password')
    elm.send_keys('')
    elm = driver.find_element_by_name('Login')
    elm.click()
    close(driver)

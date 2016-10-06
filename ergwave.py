import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

def close(driver):
    windows = driver.window_handles
    for window in windows:
        driver.close()

if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path='/home/wangbx/Tools/ergwave/chromedriver', service_log_path='/dev/null')
    driver.get('http://stackoverflow.com')
    time.sleep(2)
    
    if driver.title == 'Stack Overflow':
        print('No need web login')
    elif 'not available' in driver.title:
            print('Failed')
    else:
        if 'edirect' in driver.page_source:
            time.sleep(5)
        elm = driver.find_element_by_name('user')
        elm.send_keys('bxwang')
        elm = driver.find_element_by_name('password')
        elm.send_keys('123456')
        elm=Select(driver.find_element_by_name('fqdn'))
        elm.select_by_visible_text('CSE')
        driver.set_page_load_timeout(3)
        elm = driver.find_element_by_name('Login')
        try:
            elm.click()
        except TimeoutException: # which should happen
            print('Done web login')
            pass
    close(driver)

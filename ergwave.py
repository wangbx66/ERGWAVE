import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.remote.command import Command
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

def close(driver):
    windows = driver.window_handles
    for window in windows:
        driver.switch_to.window(window)
        driver.close()

# for phantomjs usage
'''
capabilities = webdriver.DesiredCapabilities.PHANTOMJS.copy()
proxy_conf = {
    "httpProxy": os.environ.get('http_proxy', ''),
    "ftpProxy": os.environ.get('ftp_proxy', ''),
    "sslProxy": os.environ.get('https_proxy', ''),
    "noProxy": os.environ.get('no_proxy', ''),
    "socksProxy": os.environ.get('socks_proxy', ''),
    "proxyType": 'MANUAL',
    "autodetect": False,
    }
Proxy(proxy_conf).add_to_capabilities(capabilities)
driver = webdriver.PhantomJS(executable_path=os.path.join('/', 'usr', 'bin', 'phantomjs'), desired_capabilities=capabilities, service_log_path='/dev/null')
'''

driver = webdriver.Chrome(executable_path='/home/wangbx/tools/ergwave/chromedriver', service_log_path='/dev/null')
driver.get("http://stackoverflow.com")
 
if not driver.title == 'Stack Overflow':
    if 'not available' in driver.title:
        print('Failed')
        close(driver)
    if 'edirect' in driver.page_source:
        time.sleep(7)
    elm = driver.find_element_by_name('user')
    elm.send_keys('bxwang')
    elm = driver.find_element_by_name('password')
    elm.send_keys('123456')
    elm=Select(driver.find_element_by_name('fqdn'))
    elm.select_by_visible_text('CSE')
    driver.set_page_load_timeout(6)
    elm = driver.find_element_by_name('Login')
    try:
        elm.click()
    except TimeoutException: # which should happen
        print('Done web login')
        pass
else:
    print('No need web login')
close(driver)



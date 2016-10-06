import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from ergwave import close

if __name__ == '__main__':
    capabilities = webdriver.DesiredCapabilities.PHANTOMJS.copy()
    capabilities.update({
        'phantomjs.page.settings.userAgent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3'
        })
    driver = webdriver.PhantomJS(desired_capabilities=capabilities, service_log_path='/dev/null')
    driver.get('http://stackoverflow.com')
    time.sleep(2)

    if driver.title == 'Stack Overflow':
        print('No need web login')
    elif 'not available' in driver.title:
        print('Failed')
    else:
        if 'edirect' in driver.page_source:
            time.sleep(7)
        elm = driver.find_element_by_name('username')
        elm.send_keys('SMrzkpa7')
        elm = driver.find_element_by_name('password')
        elm.send_keys('UwSLUc')
        elm = driver.find_element_by_name('term')
        elm.click()
        elm = driver.find_element_by_xpath("//input[@type='submit'][@value='login']")
        driver.set_page_load_timeout(6)
        try:
            elm.click()
        except TimeoutException:
            print('Done web login')
            pass
    close(driver)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')

driver = webdriver.Chrome('chromedriver', chrome_options=options)

driver.get('https://www.google.co.jp/search?q=chrome')
driver.save_screenshot('screenshot.png')
driver.quit()

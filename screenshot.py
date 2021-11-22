from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import time

def setup():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  chrome_options.add_argument('--force-dark-mode')
  chrome_options.add_argument("--window-size=2560,1440")
  capabilities = {
  "resolution": "2560X1440"
  }
  driver = webdriver.Chrome(options=chrome_options, desired_capabilities=capabilities)
  return driver

def login(driver, username, password):
  driver.get('https://www.tradingview.com/#signin')
  driver.find_element(By.CLASS_NAME, "i-clearfix").click()
  driver.find_element(By.NAME, "username").send_keys(username)
  driver.find_element(By.NAME, "password").send_keys(password)
  driver.find_element(By.XPATH, "//button[@type='submit']").click()

  driver.find_element(By.XPATH, "//button[@aria-label='Open user menu']").click()

def quit_browser(driver):
  driver.quit()

def capture_chart(chartUrl, loginRequired=False):
  driver = setup()
  if loginRequired:
    username = os.environ['TV_USERNAME']
    password = os.environ['TV_PASSWORD']
    login(driver, username, password)
  driver.get("https://www.tradingview.com/chart/"+chartUrl+"/")
  time.sleep(10)

  actions = ActionChains(driver)
  actions.send_keys(Keys.ESCAPE).perform()

  actions.send_keys(Keys.RIGHT*100).perform()
  time.sleep(5)

  driver.find_element(By.ID, "header-toolbar-screenshot").click()
  driver.find_element(By.XPATH, "//div[@data-name='open-image-in-new-tab']").click()
  time.sleep(5)
  driver.switch_to.window(driver.window_handles[1])
  urlToSend = driver.current_url
  #quit_browser(driver)
  return urlToSend
  
  

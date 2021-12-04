from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import time
from datetime import datetime
from threading import Thread
import telegrambot

chart = ""
loginNeeded = False
def setup():
  print('--->Setup selenium start : '+str(datetime.now()))
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  chrome_options.add_argument('--force-dark-mode')
  chrome_options.add_argument("--window-size=2560,1440")
  capabilities = {
  # "resolution": "2560X1440"
  # "resolution": "1280X720"
    "resolution": "768X432"
  }
  driver = webdriver.Chrome(options=chrome_options, desired_capabilities=capabilities)
  print('Setup selenium complete')
  return driver

def login(driver, username, password):
  print('--->Login start')
  driver.get('https://www.tradingview.com/#signin')
  actions = ActionChains(driver)
  actions.send_keys(Keys.ESCAPE).perform()
  driver.find_element(By.CLASS_NAME, "i-clearfix").click()
  driver.find_element(By.NAME, "username").send_keys(username)
  driver.find_element(By.NAME, "password").send_keys(password)
  driver.find_element(By.XPATH, "//button[@type='submit']").click()

  driver.find_element(By.XPATH, "//button[@aria-label='Open user menu']").click()
  print('Login end')

def open_chart(driver, adjustment=100):
  print('--->Opening Chart '+chart+ ' : '+str(datetime.now()))
  driver.get("https://www.tradingview.com/chart/"+chart+"/")
  print('Sleep for 10 seconds - wait for chart to load')
  time.sleep(10)
  print('Adjusting position by ', adjustment)
  actions = ActionChains(driver)
  actions.send_keys(Keys.ESCAPE).perform()
  actions.send_keys(Keys.RIGHT*adjustment).perform()
  print('Chart is ready for capture')

def screenshot(driver):
  print('--->Starting capture : '+str(datetime.now()))
  driver.find_element(By.ID, "header-toolbar-screenshot").click()
  driver.find_element(By.XPATH, "//div[@data-name='open-image-in-new-tab']").click()
  print('Sleep for 3 seconds post capture')
  time.sleep(3)
  print('Switch tab')
  driver.switch_to.window(driver.window_handles[1])
  print('Capture complete!!')

def quit_browser(driver):
  print('--->Exit browser : '+str(datetime.now()))
  driver.quit()

def send_chart():
  driver = setup()
  if loginNeeded:
    username = os.environ['TV_USERNAME']
    password = os.environ['TV_PASSWORD']
    login(driver, username, password)
  open_chart(driver)
  screenshot(driver)
  telegrambot.sendMessage(driver.current_url)
  quit_browser(driver)

def send_chart_async(chartUrl, loginRequired=False):
  global chart
  global loginNeeded

  chart = chartUrl
  loginNeeded = loginRequired
  try:
    capture = Thread(target=send_chart)
    capture.start()
  except Exception as e:
    print("[X] Capture error:\n>", e)
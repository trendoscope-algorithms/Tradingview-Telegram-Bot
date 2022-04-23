from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import time
from datetime import datetime
from threading import Thread
import telegrambot
from tkinter import Tk

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
  print('-->Signin Console')
  # actions = ActionChains(driver)
  # actions.send_keys(Keys.ESCAPE).perform()
  # print('After Escape')
  driver.find_element(By.CLASS_NAME, "i-clearfix").click()
  driver.find_element(By.NAME, "username").send_keys(username)
  driver.find_element(By.NAME, "password").send_keys(password)
  driver.find_element(By.XPATH, "//button[@type='submit']").click()
  time.sleep(3)
  print('Login end')

def screenshot(driver, chart, adjustment=100):
  print('--->Opening Chart '+chart+ ' : '+str(datetime.now()))
  driver.get("https://www.tradingview.com/chart/"+chart+"/")
  print('Sleep for 10 seconds - wait for chart to load')
  time.sleep(10)
  print('Adjusting position by ', adjustment)
  actions = ActionChains(driver)
  actions.send_keys(Keys.ESCAPE).perform()
  actions.send_keys(Keys.RIGHT*adjustment).perform()
  time.sleep(3)
  print('Chart is ready for capture')
  ActionChains(driver).key_down(Keys.ALT).key_down('s').key_up(Keys.ALT).perform()
  time.sleep(3)
  clipboard = Tk().clipboard_get()
  return clipboard

def quit_browser(driver):
  print('--->Exit browser : '+str(datetime.now()))
  driver.close()
  driver.quit()

def send_chart(chart, loginNeeded):
  driver = setup()
  if loginNeeded:
    username = os.environ['TV_USERNAME']
    password = os.environ['TV_PASSWORD']
    login(driver, username, password)
  screenshot_url = screenshot(driver, chart)
  telegrambot.sendMessage(screenshot_url)
  quit_browser(driver)

def send_chart_async(chartUrl, loginRequired=True):
  try:
    capture = Thread(target=send_chart, args=[chartUrl, loginRequired])
    capture.start()
  except Exception as e:
    print("[X] Capture error:\n>", e)
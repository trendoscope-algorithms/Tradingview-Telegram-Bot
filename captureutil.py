from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
import time
import config
from replit import db
from datetime import datetime
from threading import Thread
import telegrambot
from tkinter import Tk


def setup():
    print('--->Setup selenium start : ' + str(datetime.now()))
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--force-dark-mode')
    chrome_options.add_argument("--window-size=1280,720")
    capabilities = {
        # "resolution": "2560X1440"
        # "resolution": "1280X720"
        "resolution": "768X432"
    }
    driver = webdriver.Chrome(options=chrome_options,
                              desired_capabilities=capabilities)
    print('Setup selenium complete')
    return driver


def screenshot(driver, chart, ticker, adjustment=100):
    print('--->Opening Chart ' + chart + ' : ' + str(datetime.now()))

    chartUrl = config.urls["tvchart"] + chart + '/' + (
        '?symbol=' + ticker) if ticker != 'NONE' else ''

    driver.get(chartUrl)
    print('Sleep for 10 seconds - wait for chart to load')
    time.sleep(10)
    print('Adjusting position by ', adjustment)
    actions = ActionChains(driver)
    actions.send_keys(Keys.ESCAPE).perform()
    actions.send_keys(Keys.RIGHT * adjustment).perform()
    time.sleep(3)
    print('Chart is ready for capture')
    ActionChains(driver).key_down(Keys.ALT).key_down('s').key_up(
        Keys.ALT).perform()
    time.sleep(3)
    clipboard = Tk().clipboard_get()
    return clipboard


def quit_browser(driver):
    print('--->Exit browser : ' + str(datetime.now()))
    driver.close()
    driver.quit()


def send_chart(chart, ticker, message, delivery):
    driver = setup()
    driver.get("https://www.tradingview.com")
    sessionId = db["sessionid"] if 'sessionid' in db.keys() else 'abcd'
    print('Session Id Used :', sessionId)
    driver.add_cookie({
        'name': 'sessionid',
        'value': sessionId,
        'domain': '.tradingview.com'
    })
    screenshot_url = screenshot(driver, chart, ticker)
    if (delivery != 'asap'):
        telegrambot.sendMessage(message)
    telegrambot.sendMessage(screenshot_url)
    quit_browser(driver)


def send_chart_async(chartUrl, ticker='NONE', message='', delivery='asap'):
    try:
        capture = Thread(target=send_chart,
                         args=[chartUrl, ticker, message, delivery])
        capture.start()
    except Exception as e:
        print("[X] Capture error:\n>", e)

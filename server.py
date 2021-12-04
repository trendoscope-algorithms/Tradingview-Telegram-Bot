from flask import Flask, request
from threading import Thread
import telegrambot
import captureutil
import pandas as pd
from tabulate import tabulate

app = Flask('')
@app.route('/webhook', methods=['POST', 'GET'])
def post_message():
  try:
    jsonRequest=request.args.get("jsonRequest")
    chart = request.args.get("chart")
    loginRequired = request.args.get('loginRequired', default=False, type=lambda v: v.lower() == 'true')
    print("[I] Login Required : ",loginRequired)
    print("[I] Chart : ",chart)
    if request.method == 'POST':
      payload = request.data
      if jsonRequest == "true":
        dataframe = pd.DataFrame([request.json])
        payload = '```'+tabulate(dataframe, headers='keys', showindex=False, tablefmt='grid')+'```'
      print("[I] Payload: \n", payload)
      telegrambot.sendMessage(payload)
      if chart != None:
        captureutil.send_chart_async(chart, loginRequired)
      return 'success', 200
    else:
      print("Get request")
      return 'success', 200
  except Exception as e:
    print("[X] Exception Occured : ", e)
    return 'failure', 500

@app.route('/')
def main():
  return 'Your bot is alive!'

def run():
  app.run(host='0.0.0.0', port=5000)


def start_server_async():
  server = Thread(target=run)
  server.start()

def start_server():
  app.run(host='0.0.0.0', port=5000)
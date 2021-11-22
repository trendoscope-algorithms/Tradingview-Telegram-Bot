from flask import Flask, request
from threading import Thread
import json
import telegrambot
import screenshot

app = Flask('')
@app.route('/webhook', methods=['POST', 'GET'])
def get_webhook():
  try:
    jsonRequest=request.args.get("jsonRequest")
    chart = request.args.get("chart")
    if request.method == 'POST':
      payload = request.data
      if jsonRequest == "true":
        payload = json.dumps(request.json, indent=4)
      print("received data: \n", payload)
      telegrambot.sendMessage(payload)
      if chart != None:
        chartUrl = screenshot.capture_chart(chart)
        telegrambot.sendMessage(chartUrl)
      return 'success', 200
    else:
      print("Get request")
      return 'success', 200
  except:
    print("Exception Occured")
    return 'failure', 500

@app.route('/')
def main():
  return 'Your bot is alive!'

def run():
  app.run(host='0.0.0.0', port=8080)


def start_server_async():
  server = Thread(target=run)
  server.start()

def start_server():
  app.run(host='0.0.0.0', port=8080)
[![Trendoscope](https://assets.zyrosite.com/YBg17aEx8BCroqG1/logo-no-background-d95yX4Bp8PhPDxZx.svg)](https://www.trendoscope.au)
# Tradingview-Telegram-Bot
[![CodeFactor](https://www.codefactor.io/repository/github/trendoscope-algorithms/tradingview-telegram-bot/badge/main)](https://www.codefactor.io/repository/github/trendoscope-algorithms/tradingview-telegram-bot/overview/main)
<br>
This project provides simple webhook service which can be used to send tradingview alerts to telegram along with current chart snapshot
<h1>Installation</h1>
Follow below steps to install and run the API service
<h3>Clone repo in replit</h3>
Goto Replit Page:
https://replit.com/@trendoscope/Tradingview-Telegram-Bot

<h3>Update Replit environment variables</h3>
<h4>Mandatory Environment Variables</h4>
<ul>
<li>TOKEN - Telegram Access Token</li>
<li>CHANNEL - Telegram Channel Id</li>
</ul>

<h4>Optional Environment Variables</h4>
These are only required if we are using logged in sessions for chart capture.
<ul>
<li>tvusername - Your tradingview username</li>
<li>tvpassword - Your tradingview password</li>
</ul>

<h3>Run the repl</h3>
Just run the repl and your services are up and running. You will get the hostname on top right part of the project dashboard. Hostname will be of the format, https://Tradingview-Telegram-Bot.<YOUR_REPL_ACCOUN>.repl.co

<h1>Usage</h1>
Once up and running, you will be able to use following calls 

<h3>POST /webhook/</h3>

<h4>Query Parameters</h4>
<ul>
<li> jsonRequest - can be set as true/false. Default is false. If set to true, the payload should be a standard json. Output to telegram will be sent in tabular format. If not set or if set to false, output to telegram will be clear text.</li>
<li> chart - Send the chart id if required to send chart snapshot along with alert message. For this to work - chart needs to be either a shared chart or environment variables for tvusername and tvpassword should be set to the user who has access to given chart.</li>
</ul>

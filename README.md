[![Trendoscope](https://svgshare.com/i/u3u.svg)](https://trendoscope.io)
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
<li>username - Your tradingview username</li>
<li>password - Your tradingview password</li>
<li>sessionid - Your tradingview session id. If you don't want to use userrname and password, this is an alternative. sessionid can be obtained from browser cookies</li>
</ul>

<h3>Run the repl</h3>
Just run the repl and your services are up and running. You will get the hostname on top right part of the project dashboard. Hostname will be of the format, <pre>https<span>://Tradingview-Telegram-Bot<span>.<span>[YOUR_REPL_ACCOUNT]<span>.<span>repl.co</pre>

<h1>Usage</h1>
Once up and running, you will be able to use following calls 

<h3>POST /webhook/</h3>

<h4>Query Parameters</h4>
<ul>
<li> <b>jsonRequest</b> - can be set as true/false. Default is false. If set to true, the payload should be a standard json. Output to telegram will be sent in tabular format. If not set or if set to false, output to telegram will be clear text.</li>
<li> <b>tblfmt</b> - table format to be used when jsonRequest is set to true. Default is plain. The values are exactly same as the ones required for <a href="https://pypi.org/project/tabulate/">tabulate</a> package. 
<li> <b>chart</b> - Send the chart id if required to send chart snapshot along with alert message. For this to work - chart needs to be either a shared chart or environment variables for tvusername and tvpassword should be set to the user who has access to given chart.</li>
<li> <b>ticker</b> - Chart ticker. You no longer need to use different chart for different tickers. You can have a common chart and pass ticker to it so that chart will automatically switch to given ticker before taking screenshot</li>
<li> <b>delivery</b> - Taking chart snapshot takes time. This also delays the delivery of alert message. To avoid this, we can use this option - delivery=asap so that alert message will be sent as soon as possible and chart is sent later. If this parameter is not set, then both the messages will be delivered together.</li>
</ul>

## Contributions & Thanks
If you found this project interesting or useful, create accounts with my referral links:
- [Tradingview](https://www.tradingview.com/?aff_id=112733)
- [BingX](https://bingx.com/en-us/partner/Trendoscope/)

# Profiles
<a href="https://p.trendoscope.io/"><img src="https://svgshare.com/i/u6r.svg" width="100" height="100"></a>
<a href="https://p.trendoscope.io/twitter"><img src="https://i.pinimg.com/originals/aa/3d/75/aa3d750ddec109594ac7c89cb8cbabab.jpg" width="100" height="100"></a>
<a href="https://p.trendoscope.io/telegram"><img src="https://i.pinimg.com/originals/70/c3/ea/70c3ea9e43ebd11ec98de96937529408.jpg" width="100" height="100"></a>
<a href="https://p.trendoscope.io/discord"><img src="https://i.pinimg.com/originals/b6/fe/4a/b6fe4a830e0263d8344b63e3dbcf3033.jpg" width="100" height="100"></a>
<a href="https://p.trendoscope.io/youtube"><img src="https://i.pinimg.com/originals/f4/14/b8/f414b816ef11df2c1eaae61f2fc8c489.jpg" width="100" height="100"></a>

# Links
https://linktr.ee/tscope

import os
from replit import db
import config
import requests
import platform
from urllib3 import encode_multipart_formdata


def login():
    print('Getting sessionid from db')
    sessionid =  db["sessionid"] if 'sessionid' in db.keys() else 'abcd'

    headers = {'cookie': 'sessionid=' + sessionid}
    test = requests.request("GET", config.urls["tvcoins"], headers=headers)
    print(test.text)
    if(test.status_code != 200 and 'sessionid' in os.environ.keys()):
        print('SessionId from secrets :'+os.environ['sessionid'])  
        headers = {'cookie': 'sessionid=' + os.environ['sessionid']}
        test = requests.request("GET", config.urls["tvcoins"], headers=headers)
        print(test.text)
        if(test.status_code == 200):
            db["sessionid"] = os.environ['sessionid']
            return
    
    print('username' in os.environ.keys() and 'password' in os.environ.keys())
    if test.status_code != 200 and 'username' in os.environ.keys() and 'password' in os.environ.keys():
        print('session id from db is invalid')
        username = os.environ['username']
        password = os.environ['password']

        payload = {
            'username': username,
            'password': password,
            'remember': 'on'
        }
        body, contentType = encode_multipart_formdata(payload)
        userAgent = 'TWAPI/3.0 (' + platform.system(
        ) + '; ' + platform.version() + '; ' + platform.release() + ')'
        print(userAgent)
        login_headers = {
            'origin': 'https://www.tradingview.com',
            'User-Agent': userAgent,
            'Content-Type': contentType,
            'referer': 'https://www.tradingview.com'
        }
        login = requests.post(config.urls["signin"],
                              data=body,
                              headers=login_headers)
        cookies = login.cookies.get_dict()
        sessionid = cookies["sessionid"]
        db["sessionid"] = sessionid

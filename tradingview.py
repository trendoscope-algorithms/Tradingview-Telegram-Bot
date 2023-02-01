import os
from replit import db
import config
import requests
import platform
from urllib3 import encode_multipart_formdata


def login():
        print('Getting sessionid from db')
        sessionid = db["sessionid"] if 'sessionid' in db.keys(
        ) else 'abcd'

        headers = {'cookie': 'sessionid=' + sessionid}
        test = requests.request("GET", config.urls["tvcoins"], headers=headers)
        print(test.text)
        print('sessionid from db : ' + sessionid)
        if test.status_code != 200:
            print('session id from db is invalid')
            username = os.environ['tvusername']
            password = os.environ['tvpassword']

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

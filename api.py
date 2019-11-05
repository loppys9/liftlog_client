#!/usr/bin/env python3

import json
import requests

url_base = "http://127.0.0.1:8000/"
api_url_base = "http://127.0.0.1:8000/api/"
# This is terrible, don't do it when things be working.
user = 'shane'
pwd = 'shane'
auth_vals = (user, pwd)

def login(session, user, password):
    url = '{0}auth/login/'.format(url_base)
    login_data = { 'username':user, 'password':password, 'next':'/api' }

    session.get(url)

    if 'csrftoken' in session.cookies:
        login_data['csrfmiddlewaretoken'] = session.cookies['csrftoken']

    response = session.post(url, login_data)

    print(response.status_code)
    print(response.text)

def get_api_root(session):
    request = session.get(api_url_base, auth=('shane', 'shane'))

    print(request.status_code)
    print(request.text)


if __name__ == "__main__":
    session = requests.session()
    login(session, user, pwd)
    #get_api_root()

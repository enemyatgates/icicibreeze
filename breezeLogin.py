#!/usr/bin/env python
import sys
sys.path.append('../../O+00+00+03+ICICIBREEZE/')
import breezeValues
import urllib.parse
import webbrowser

# Generate Login Session
def getLogin():
    loginUrl = breezeValues.breezeUrl+urllib.parse.quote_plus(breezeValues.breezeKey)
    print('Login URL:', loginUrl)
    openUrl = webbrowser.open(loginUrl, new=0, autoraise=False)
    if (openUrl):
        print("Login URL:", loginUrl, 'Opened Successfully')
getLogin()
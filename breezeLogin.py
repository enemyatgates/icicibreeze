#!/usr/bin/env python
import pathlib
import sys
sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent.parent)+'\\O+00+00+03+ICICIBREEZE\\')
import urllib.parse
import webbrowser
import breezeValues

# Generate Login Session
def getLogin():
    loginUrl = breezeValues.breezeUrl+urllib.parse.quote_plus(breezeValues.breezeKey)
    print('Login URL:', loginUrl)
    openUrl = webbrowser.open(loginUrl, new=0, autoraise=False)
    if (openUrl):
        print("Login URL:", loginUrl, 'Opened Successfully')
getLogin()
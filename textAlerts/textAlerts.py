import os
import requests
import json
import datetime
import time
from twilio.rest import Client
import random

account_sid = "ACfb6448b85d09e8b2b55afc743a7c8d1f"
auth_token  = "0ae0a1b7a5de7dad632dcbfc5eb3aa0d"


def checkTwentyMinutes(n, lux):
    body=""
    url = "https://time-series-store-predix.run.aws-usw02-pr.ice.predix.io/v1/datapoints"

    payload = "{\n  \"tags\": [\n    {\n      \"name\": \"Temperature:STORAGE"+str(n)+"\",\n      \"aggregations\": [\n              {\n                \"type\": \"avg\",\n                \"interval\": \"20mi\"\n              }\n            ]\n    },\n    {\n      \"name\": \"Humidity:STORAGE"+str(n)+"\",\n      \"aggregations\": [\n              {\n                \"type\": \"avg\",\n                \"interval\": \"20mi\"\n              }\n            ]\n    }\n  ],\n  \"start\": \"20mi-ago\"\n\t\n}"
    headers = {
        'authorization': "bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImxlZ2FjeS10b2tlbi1rZXkiLCJ0eXAiOiJKV1QifQ.eyJqdGkiOiI1NmY4NGYwOWNjY2M0MzM3OTU4MzQ1M2U3N2NlOGEzNyIsInN1YiI6ImFwcF9jbGllbnRfaWQiLCJzY29wZSI6WyJ0aW1lc2VyaWVzLnpvbmVzLmYzZTFlZjI3LTk1NDMtNGI1ZS1hMTVmLTE4NmVlZWVhMzZkMy5pbmdlc3QiLCJ0aW1lc2VyaWVzLnpvbmVzLmYzZTFlZjI3LTk1NDMtNGI1ZS1hMTVmLTE4NmVlZWVhMzZkMy5xdWVyeSIsInRpbWVzZXJpZXMuem9uZXMuZjNlMWVmMjctOTU0My00YjVlLWExNWYtMTg2ZWVlZWEzNmQzLnVzZXIiLCJ1YWEucmVzb3VyY2UiLCJvcGVuaWQiLCJ1YWEubm9uZSIsInByZWRpeC1hc3NldC56b25lcy41OGE2ZmEzYy0yM2QyLTQzNWMtOWIzNy03YjVlZWQ0NDVjNjgudXNlciJdLCJjbGllbnRfaWQiOiJhcHBfY2xpZW50X2lkIiwiY2lkIjoiYXBwX2NsaWVudF9pZCIsImF6cCI6ImFwcF9jbGllbnRfaWQiLCJncmFudF90eXBlIjoiY2xpZW50X2NyZWRlbnRpYWxzIiwicmV2X3NpZyI6IjEwZDg1NGQxIiwiaWF0IjoxNTAxNDE3Mzk3LCJleHAiOjE1MDE0NjA1OTcsImlzcyI6Imh0dHBzOi8vNzdhMzg2N2ItY2NlMC00MjNkLWE4ZWMtNDQ4ZDIwNDI2OTg0LnByZWRpeC11YWEucnVuLmF3cy11c3cwMi1wci5pY2UucHJlZGl4LmlvL29hdXRoL3Rva2VuIiwiemlkIjoiNzdhMzg2N2ItY2NlMC00MjNkLWE4ZWMtNDQ4ZDIwNDI2OTg0IiwiYXVkIjpbInVhYSIsIm9wZW5pZCIsInByZWRpeC1hc3NldC56b25lcy41OGE2ZmEzYy0yM2QyLTQzNWMtOWIzNy03YjVlZWQ0NDVjNjgiLCJ0aW1lc2VyaWVzLnpvbmVzLmYzZTFlZjI3LTk1NDMtNGI1ZS1hMTVmLTE4NmVlZWVhMzZkMyIsImFwcF9jbGllbnRfaWQiXX0.YaHHM_6PUVctrTT1d1iCb_y4ELTkAHUNAUtcKfXz71Ski9RX_s-hfWGd92qre8A05TLv5msrQ-HWa0KNj8UBskLjkTqtdKKYOQjw_S0mye_674r1DCq1y1oIyrir3v0eTmctsm4NWyEnUQRlZmDxGKKWo43aPD1eJylbl_sjCZ4uduuyLqadLLZr3FINOwXVDAJxz0Egsd017hNT8V6H7Va4NRts5qJTX6iF8RSjrY3HEgwCT6IsBtQAgqUj-nl6i3K-uwu5sBZAC-_hEdiHDDrspLOonFuV15fXC6O-wLQoB5-pEtDB42unhK-qGOysblOSKYg7vaKEob-haFSnOA",
        'predix-zone-id': "f3e1ef27-9543-4b5e-a15f-186eeeea36d3",
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "63ddba1e-ef4f-d35f-0029-b47fc59e3ea6"
        }
    
    response = requests.request("POST", url, data=payload, headers=headers)

    data = response.text
    data = json.loads(data)
    temperature = data['tags'][0]['results'][0]['values']
    humidity = data['tags'][1]['results'][0]['values']
    x=0
    while x < len(temperature):
        t=round(temperature[x][1],2)
        h=round(humidity[x][1],2)
        lux = round(lux,2)
        print t,h,lux
        if t > 70.0:
            body += "\nTemperature Alert! In the last 20 minutes, your average temperature in STORAGE{} was {}F \n".format(n,t)
        if h < 30.0 or h > 50.0:
            body += "\nHumidity Alert! In the last 20 minutes, your average humidity in STORAGE{} was {}% \n".format(n,h)
        if lux > 55 and n == 1:
            body += "\nHigh Light Exposure! STORAGE1 is full of artififacts that are very sensitive to light. In the last 20 minutes, the average lux was {} \n".format(lux)

        elif lux > 155 and n == 2:
            body += "\nHigh Light Exposure! STORAGE2 is full of artififacts that are sensitive to light. In the last 20 minutes, the average lux was {} \n".format(lux)
        
        x += 1
    sendMessage(body)

def sendMessage(b):
    client = Client(account_sid, auth_token)
    if b:
        message = client.messages.create(
            to="+19896717269", 
            from_="+19896079748",
            body=b)
        print(message.sid)
        


while True:
    lux = random.uniform(1.0, 200.0)
    checkTwentyMinutes(2, lux)
    time.sleep(1200)
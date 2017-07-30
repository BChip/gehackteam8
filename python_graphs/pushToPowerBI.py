import pygal
import requests
import json
import datetime
import time
import urllib2
import threading

REST_API_URL = 'https://api.powerbi.com/beta/2412c246-8cec-4f6f-846a-e324d59e13ff/datasets/bb845243-3edb-4c3b-b5bf-6f8ed867f4b8/rows?key=gEqky%2B61s%2FwmYqYPV8oyFeH67ryVBjB5BaE90KvTHzO%2Fle71M3QkkbE41GBAuVAjEeZLY0N%2FFVfQzl4TH0W4ig%3D%3D'

def getData(n):
    url = "https://time-series-store-predix.run.aws-usw02-pr.ice.predix.io/v1/datapoints"

    payload = "{\n  \"tags\": [\n    {\n      \"name\": \"Temperature:STORAGE"+str(n)+"\",\n      \"aggregations\": [\n              {\n                \"type\": \"avg\",\n                \"interval\": \"30mi\"\n              }\n            ]\n    },\n    {\n      \"name\": \"Humidity:STORAGE"+str(n)+"\",\n      \"aggregations\": [\n              {\n                \"type\": \"avg\",\n                \"interval\": \"30mi\"\n              }\n            ]\n    }\n  ],\n  \"start\": \"2mm-ago\"\n\t\n}"
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
        try:
            s = "STORAGE"+str(n)
            ti=datetime.datetime.fromtimestamp(temperature[x][0]/1000).strftime("%Y-%m-%dT%H:%M:%S%Z")
            t=round(temperature[x][1],1)
            h=round(humidity[x][1],1)
            print s,ti,t,h
            if ti and t and h:
                data = '[{{"stor": "{0}", "t": "{1}", "temp": "{2:0.1f}", "h": "{3:0.1f}" }}]'.format(s,ti, t, h)
                req = urllib2.Request(REST_API_URL, data)
                response = urllib2.urlopen(req)
                print response
            x += 1
            time.sleep(1)
        except:
            x += 1
            pass

getData(1)
getData(2)
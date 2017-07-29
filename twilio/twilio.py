import os
import requests
import json
import datetime
import time

from twilio.rest import Client

account_sid = "ACfb6448b85d09e8b2b55afc743a7c8d1f"
auth_token  = "0ae0a1b7a5de7dad632dcbfc5eb3aa0d"

#FRIENDLY NAME geAlert
#SID SK84b5358b38e43b4c4503517f80faab1c
#KEY TYPE Standard
#SECRET dZKSM9iqNsJ4IiOr8KbYGD6U52kMmooq

def check(t,loc):
    client = Client(account_sid, auth_token)
    url = "https://time-series-store-predix.run.aws-usw02-pr.ice.predix.io/v1/datapoints"

    payload = "{\n  \"tags\": [\n    {\n      \"name\": \""+t+":"+loc+"\",\n      \"filters\": {\n               \"measurements\": {\n                   \"condition\": \"le\",\n                   \"values\": \"100\"\n               }\n           },\n      \"aggregations\": [\n              {\n                \"type\": \"avg\",\n                \"interval\": \"20mi\"\n              }\n            ]\n    }\n  ],\n  \"start\": \"20mi-ago\"\n\t\n}"
    headers = {
        'authorization': "bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImxlZ2FjeS10b2tlbi1rZXkiLCJ0eXAiOiJKV1QifQ.eyJqdGkiOiI4MTg2ZGQ2NjI3NDQ0NDk5OGIwMDI1ZWQ1ZTIwNmUzNiIsInN1YiI6ImFwcF9jbGllbnRfaWQiLCJzY29wZSI6WyJ0aW1lc2VyaWVzLnpvbmVzLmYzZTFlZjI3LTk1NDMtNGI1ZS1hMTVmLTE4NmVlZWVhMzZkMy5pbmdlc3QiLCJ0aW1lc2VyaWVzLnpvbmVzLmYzZTFlZjI3LTk1NDMtNGI1ZS1hMTVmLTE4NmVlZWVhMzZkMy5xdWVyeSIsInRpbWVzZXJpZXMuem9uZXMuZjNlMWVmMjctOTU0My00YjVlLWExNWYtMTg2ZWVlZWEzNmQzLnVzZXIiLCJ1YWEucmVzb3VyY2UiLCJvcGVuaWQiLCJ1YWEubm9uZSIsInByZWRpeC1hc3NldC56b25lcy41OGE2ZmEzYy0yM2QyLTQzNWMtOWIzNy03YjVlZWQ0NDVjNjgudXNlciJdLCJjbGllbnRfaWQiOiJhcHBfY2xpZW50X2lkIiwiY2lkIjoiYXBwX2NsaWVudF9pZCIsImF6cCI6ImFwcF9jbGllbnRfaWQiLCJncmFudF90eXBlIjoiY2xpZW50X2NyZWRlbnRpYWxzIiwicmV2X3NpZyI6IjEwZDg1NGQxIiwiaWF0IjoxNTAxMzM4Mzg2LCJleHAiOjE1MDEzODE1ODYsImlzcyI6Imh0dHBzOi8vNzdhMzg2N2ItY2NlMC00MjNkLWE4ZWMtNDQ4ZDIwNDI2OTg0LnByZWRpeC11YWEucnVuLmF3cy11c3cwMi1wci5pY2UucHJlZGl4LmlvL29hdXRoL3Rva2VuIiwiemlkIjoiNzdhMzg2N2ItY2NlMC00MjNkLWE4ZWMtNDQ4ZDIwNDI2OTg0IiwiYXVkIjpbInVhYSIsIm9wZW5pZCIsInByZWRpeC1hc3NldC56b25lcy41OGE2ZmEzYy0yM2QyLTQzNWMtOWIzNy03YjVlZWQ0NDVjNjgiLCJ0aW1lc2VyaWVzLnpvbmVzLmYzZTFlZjI3LTk1NDMtNGI1ZS1hMTVmLTE4NmVlZWVhMzZkMyIsImFwcF9jbGllbnRfaWQiXX0.ne9HrKNzKPxaHrErmgS-IlQAKM19o1TmpnoCCwwJe0Zpnokq0S1HrbWwYFif_qIiLgLGhIW6InCe2tGOSEfQymteH67rfZ2EPKpFeADaGxQNH7eqnVstz13NpbNl7B-1JNQ25ZdZ-soM6QyrozHwpxDUMlS4meWEUZQR06rYHvISu3gZ2TtkuJae8bhzCuPOiRj2-WCP06hs5YuIq3fVq7Q9gu6az7Lnp-gaWVMtfl5b6SVgiboo_DBsY_j7WdNhCmjj_h-LmqsahFDkwyxwYcmeadVpBBJ6NLEFKRfGNpi0Cx0yf18WxS0xhcYC3IRNQ4dGzq5vXH42LZbjBq5D3w",
        'predix-zone-id': "f3e1ef27-9543-4b5e-a15f-186eeeea36d3",
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "63ddba1e-ef4f-d35f-0029-b47fc59e3ea6"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    data = response.text
    data = json.loads(data)
    data = data['tags'][0]['results'][0]['values']

    for d in data:
        s = round(d[1],2)
        print t, s
        if (s < 70.0 or s >= 80.0) and t == "Temperature":
            message = client.messages.create(
                to="+19896717269", 
                from_="+19896079748",
                body="Temperature Alert! In the last 20 minutes, your average temperature in {} was {}F".format(loc,s))
            print(message.sid)
        elif (s < 50.0 or s >= 65.0) and "Humidity":
            message = client.messages.create(
                to="+19896717269", 
                from_="+19896079748",
                body="Humidity Alert! In the last 20 minutes, your average humidity in {} was {}F".format(loc,s))
            print(message.sid)
            



while True:
    check("Temperature","STORAGE1")
    check("Temperature","STORAGE2")
    check("Humidity","STORAGE1")
    check("Humidity","STORAGE2")
    time.sleep(1200)
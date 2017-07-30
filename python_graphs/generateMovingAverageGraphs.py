import requests
import json
import numpy as np
import time
from statistics import mean, stdev
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot
import matplotlib.pyplot as plt

import pandas as pd
from pylab import *
import csv, string, sys, os, re
def get_stability(data):
    return stdev(data)
def moving_average(x_data, y_data, samples):
    w = [1.0/samples]*samples
    offset = (samples-1)//2
    y_data = np.convolve(y_data,w,'valid')
    x_data = x_data[offset:-offset]
    return x_data, y_data
def get_data(url, start_time, end_time, data_type, sensor, filter_max, filter_min ):
    interpolation = "6s"
    json_bullshit_interpolation = '''{{
       "start": "{}-ago",
       "end": "{}-ago",
       "tags": [
           {{
               "name": "{}:{}",
               "aggregations":[
                   {{
                       "type":"interpolate",
                       "interval":"{}"
                   }}
               ],
               "filters": {{
                    "measurements": {{
                           "condition": "le",
                           "values": "{}"
                        }}
               }}
           }}
       ]
    }}
    '''.format(start_time, end_time,data_type, sensor, interpolation,filter_max)  
    payload = json_bullshit_interpolation
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
    data = data['tags'][0]['results'][0]['values']
    data.sort()
    x_data = []
    y_data = []
    for row in data:
        if row[1] > filter_min:
            x_data.append(float(row[0]))
            y_data.append(float(row[1]))
    return x_data, y_data
while True:
    print("Starting Script")
    start_time = "24h"
    end_time = "1mi"
    samples = 15
    url = "https://time-series-store-predix.run.aws-usw02-pr.ice.predix.io/v1/datapoints"
    file_location = r"result.png"
    sensors = ["STORAGE1", "STORAGE2"]
    data_type = ["Temperature", "Humidity"]
    x_data = {}
    y_data = {}
    keys = []
    print("Starting Gathering Data")
    for s in sensors:
        for d in data_type:
            keys.append(s+d)
            x_data[s+d], y_data[s+d] = get_data(url, start_time, end_time, d, s, 100, 5)
            
    plt.figure()
    print("Starting Graphing")
    for k in keys:
        x_data[k], y_data[k] = moving_average(x_data[k], y_data[k], samples)
    f, ax = plt.subplots(2,2)
    array = ((0,0),(0,1),(1,0),(1,1))
    count = [0,1,2,3]
    stability = [0,1,2,3]
    means = [0,1,2,3]
    for index, num in zip(array, count):
        k = sensors[index[0]]+data_type[index[1]]
        ax[index].plot(x_data[k],y_data[k], 'b.')
        plt.title(k)
        print(k + " Stability: " + str(get_stability(y_data[k])))
        print(k + " Mean: " + str(mean(y_data[k])))
        stability[num] = get_stability(y_data[k])
        means[num] = mean(y_data[k])
    savefig(file_location)
    plt.show()
    print("Done")
    time.sleep(60)
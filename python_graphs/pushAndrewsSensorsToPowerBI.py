import urllib
import urllib2
import time
request = urllib.urlopen("http://gehack.mybluemix.net/getdata")
html = request.read()
html = html.decode("utf-8")
html = html.split(';')
sensors = {}

REST_API_URL = "https://api.powerbi.com/beta/2412c246-8cec-4f6f-846a-e324d59e13ff/datasets/b95a8a95-135a-4cc2-abb3-9043c2bf5608/rows?key=JTh6FCeTEwqR72c49PNtUFBii9BeYu5kJQ77iXLO29AzMDDt79vMNqbZ9HXk31yYf2dhYevC5%2FSMYPtFHvQH7A%3D%3D"

a = ['a','b','c','d']
count =0
while True:
    for line in html:
        l = line.split(',')
        ambtemp = l[0].split("=")[1]
        humidity = l[1].split("=")[1]
        letter = a[count]
        objtemp = l[2].split("=")[1]
        print ambtemp, humidity, letter, objtemp
        d = '[{{"ambientTemp": "{0}", "humidity": "{1}", "letter": "{2}", "objecttemp": "{3}" }}]'.format(ambtemp, humidity, letter, objtemp)
        req = urllib2.Request(REST_API_URL, d)
        response = urllib2.urlopen(req)
        time.sleep(1)
        count += 1
        if count == 4:
            count = 0
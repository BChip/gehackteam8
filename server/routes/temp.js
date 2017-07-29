var http = require("https");

var options = {
  "method": "POST",
  "hostname": "time-series-store-predix.run.aws-usw02-pr.ice.predix.io",
  "port": null,
  "path": "/v1/datapoints",
  "headers": {
    "authorization": "bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImxlZ2FjeS10b2tlbi1rZXkiLCJ0eXAiOiJKV1QifQ.eyJqdGkiOiI4MTg2ZGQ2NjI3NDQ0NDk5OGIwMDI1ZWQ1ZTIwNmUzNiIsInN1YiI6ImFwcF9jbGllbnRfaWQiLCJzY29wZSI6WyJ0aW1lc2VyaWVzLnpvbmVzLmYzZTFlZjI3LTk1NDMtNGI1ZS1hMTVmLTE4NmVlZWVhMzZkMy5pbmdlc3QiLCJ0aW1lc2VyaWVzLnpvbmVzLmYzZTFlZjI3LTk1NDMtNGI1ZS1hMTVmLTE4NmVlZWVhMzZkMy5xdWVyeSIsInRpbWVzZXJpZXMuem9uZXMuZjNlMWVmMjctOTU0My00YjVlLWExNWYtMTg2ZWVlZWEzNmQzLnVzZXIiLCJ1YWEucmVzb3VyY2UiLCJvcGVuaWQiLCJ1YWEubm9uZSIsInByZWRpeC1hc3NldC56b25lcy41OGE2ZmEzYy0yM2QyLTQzNWMtOWIzNy03YjVlZWQ0NDVjNjgudXNlciJdLCJjbGllbnRfaWQiOiJhcHBfY2xpZW50X2lkIiwiY2lkIjoiYXBwX2NsaWVudF9pZCIsImF6cCI6ImFwcF9jbGllbnRfaWQiLCJncmFudF90eXBlIjoiY2xpZW50X2NyZWRlbnRpYWxzIiwicmV2X3NpZyI6IjEwZDg1NGQxIiwiaWF0IjoxNTAxMzM4Mzg2LCJleHAiOjE1MDEzODE1ODYsImlzcyI6Imh0dHBzOi8vNzdhMzg2N2ItY2NlMC00MjNkLWE4ZWMtNDQ4ZDIwNDI2OTg0LnByZWRpeC11YWEucnVuLmF3cy11c3cwMi1wci5pY2UucHJlZGl4LmlvL29hdXRoL3Rva2VuIiwiemlkIjoiNzdhMzg2N2ItY2NlMC00MjNkLWE4ZWMtNDQ4ZDIwNDI2OTg0IiwiYXVkIjpbInVhYSIsIm9wZW5pZCIsInByZWRpeC1hc3NldC56b25lcy41OGE2ZmEzYy0yM2QyLTQzNWMtOWIzNy03YjVlZWQ0NDVjNjgiLCJ0aW1lc2VyaWVzLnpvbmVzLmYzZTFlZjI3LTk1NDMtNGI1ZS1hMTVmLTE4NmVlZWVhMzZkMyIsImFwcF9jbGllbnRfaWQiXX0.ne9HrKNzKPxaHrErmgS-IlQAKM19o1TmpnoCCwwJe0Zpnokq0S1HrbWwYFif_qIiLgLGhIW6InCe2tGOSEfQymteH67rfZ2EPKpFeADaGxQNH7eqnVstz13NpbNl7B-1JNQ25ZdZ-soM6QyrozHwpxDUMlS4meWEUZQR06rYHvISu3gZ2TtkuJae8bhzCuPOiRj2-WCP06hs5YuIq3fVq7Q9gu6az7Lnp-gaWVMtfl5b6SVgiboo_DBsY_j7WdNhCmjj_h-LmqsahFDkwyxwYcmeadVpBBJ6NLEFKRfGNpi0Cx0yf18WxS0xhcYC3IRNQ4dGzq5vXH42LZbjBq5D3w",
    "predix-zone-id": "f3e1ef27-9543-4b5e-a15f-186eeeea36d3",
    "content-type": "application/json",
    "cache-control": "no-cache",
    "postman-token": "2ec9b8ed-1f46-7c7e-66b7-9f7905e09110"
  }
};

var req = http.request(options, function (res) {
  var chunks = [];

  res.on("data", function (chunk) {
    chunks.push(chunk);
  });

  res.on("end", function () {
    var body = Buffer.concat(chunks);
    module.exports = body.toString();
  });
});

req.write(JSON.stringify({ tags: [ { name: 'Temperature:STORAGE1' } ], start: '2mm-ago' }));
req.end();

import requests

url = "https://www.fast2sms.com/dev/bulkV2"

querystring = {
    "authorization":"x1T7Cwp6gsQLEZOvY2HoXU34JSPiKWNIeqhBAcfGV90kzldRMtkNM7Fu0R4LYZW9w1BsiEPnpldTSxXa",
    "message":"This is test message from canceRX",
    "language":"english",
    "route":"q",
    "numbers":"7992381406"
    }

headers = {
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.json()["return"])

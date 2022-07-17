import requests

def convert ():
    what_currency = input('What currency do you want to convert? ')
    which_currency = input('to which currency do you want to convert? ')
    url = "https://binance43.p.rapidapi.com/ticker/24hr"

    querystring = {"symbol":"BTCUSDT"}

    headers = {
        "X-RapidAPI-Key": "febae8becamshfd2559dd073bc98p13e8f9jsn0a0965f0f99c",
        "X-RapidAPI-Host": "binance43.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

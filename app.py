import requests


def convert():
    # PLZ USE CODE eg:BTC
    what_currency = input('What currency do you want to convert? ').upper()
    # PLZ USE CODE eg:USDT
    which_currency = input(
        'to which currency do you want to convert? ').upper()
    url = "https://binance43.p.rapidapi.com/ticker/24hr"

    querystring = {"symbol": f"{what_currency}{which_currency}"}

    headers = {
        "X-RapidAPI-Key": "febae8becamshfd2559dd073bc98p13e8f9jsn0a0965f0f99c",
        "X-RapidAPI-Host": "binance43.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    json = response.json()
    print(json)
    print(f"""{json['symbol']}\n{json['bidPrice']}\n{json['lastPrice']}\n{json['highPrice']}\n{json['priceChange']}""")


convert()
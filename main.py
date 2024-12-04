import requests as rq
import pandas as pd
stocks = pd.read_csv('D:/Data Scrape Practice/Data Scrape Task/D_Scrape-Task3/stocks.csv')
st_dict = stocks.to_dict(orient='records')
cUrl = 'https://api.coinbase.com/v2/exchange-rates'
cHeader = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}
for st in st_dict:
    currency = st['Currency']
    currencyParam = {'currency': currency}
    cResp = rq.get(url=cUrl, headers=cHeader,params=currencyParam)
    cData = cResp.json()
    inr_rate = cData['data']['rates']['INR']
    st['INR_Price'] = st['Price'] * float(inr_rate)

df = pd.DataFrame(st_dict)
df.to_csv('stocks_INR.csv')

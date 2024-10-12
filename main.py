import streamlit as st
import requests

r=requests.get('https://api.coinlore.net/api/tickers/')
veri = r.json() #canlı veriler

coinler = veri['data'] #data içindekiler gelecek

coinfiyat={}

for coin in coinler: #tek tek sözlüğün içine bakıyor sayır satır, çoklu elemanlara tek tek ulaşır.Açtığı her şeye coin diyecek
    sembol=coin['symbol']
    fiyat=coin['price_usd']

    coinfiyat.update({sembol:float(fiyat)}) #matematiksel işlemler içine girebilmek için float a dönüştürdü yoksa tırnak içinde geliyordu matematik yapılamazdı.

#print(coinfiyat)

coinisimler= coinfiyat.keys()

coin1=st.sidebar.selectbox("Eldeki Coin",coinisimler)
miktar=st.sidebar.number_input("Miktar")
coin2=st.sidebar.selectbox("Hedef Coin",coinisimler)

c1 = coinfiyat.get(coin1) #BNB fiyatını getiriyor ne yazarsan keys kısmına onun value sinin getirir.
miktar=20
c2=coinfiyat.get(coin2)
sonuc=miktar*c1/c2

st.write(miktar,"adet",coin1,sonuc,"adet",coin2)

st.link_button("Satın Al",f"https://www.coinbase.com/tr/converter/{coin1}/{coin2}") #
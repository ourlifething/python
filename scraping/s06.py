import requests
from bs4 import BeautifulSoup 

res=requests.get('https://joytas.net/kaba/')
res.encoding=res.apparent_encoding
soup=BeautifulSoup(res.text, 'html.parser')

links = soup.select('li a')

with open('zoo.txt','w',encoding='utf-8')as file:
	for link in links:
		file.write(f'{link.text}:{link.get("href")}\n')

"""zoo.txt:
上野動物園:https://www.tokyo-zoo.net/zoo/ueno/
いしかわ動物園:http://www.ishikawazoo.jp/
東山動物園:http://www.higashiyama.city.nagoya.jp/
神戸どうぶつ王国:https://www.kobe-oukoku.com/
NIFREL:https://www.nifrel.jp/

"""

import requests
from bs4 import BeautifulSoup 

res=requests.get('https://joytas.net/kaba/')
res.encoding=res.apparent_encoding
soup=BeautifulSoup(res.text, 'html.parser')
"""名前を抜く"""

names = soup.select('td:first-child')
for name in names:
	print(name.text)

	"""
やすお
はな
だいち
のぞみ
やま
	"""

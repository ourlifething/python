import requests
from bs4 import BeautifulSoup 

res=requests.get('https://joytas.net/kaba/')
res.encoding=res.apparent_encoding
"""apparent_encoding は、Python の文字エンコーディングを自動的に判定するためのメソッド"""
#第1引数にhtml文字列,第2引数にパーサーを指定する。今回は追加ライブラリ不要な'html.parser'を指定
soup=BeautifulSoup(res.text, 'html.parser')
"""このパーサーは、HTML ドキュメントを解析して構文解析するために使用されます。"""
#BeautifulSoupオブジェクトをprintにそのまま渡すと全文を表示する
print(soup)

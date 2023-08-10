isError = False
n = 10
if isError == False and n < 100:
	print('ok')

num = int(input('数値>>'))
"""三項演算子
print('偶数' if num % 2 == 0 else '奇数')
"""
if num % 2 == 0:
	print('even')
else:
	print('odd')

hello = input('挨拶を入力>>')

if hello == 'こんにちは':
	print('ようこそ')
elif hello == '景気は？':
	print('ぼちぼちです')
elif hello == 'さようなら':
	print('お元気で！')
else:
	print('どうしました？')


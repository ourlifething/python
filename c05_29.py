def eat(breakfast, lunch, dinner = 'カレー',*desserts): #*desserts可変長引数
	print(f'朝は{breakfast}を食べました')
	print(f'昼は{lunch}を食べました')
	print(f'晩は{dinner}を食べました')

	for d in desserts:
		print(f'おやつに{desserts}を食べました')
	
print('8/1')
eat('トースト','パスタ','カレー','アイス','チョコ','カレー')

#sumof(n1,*args)合計を求めるのに引数ゼロは気持ち悪いので(n1,*args)とすることもよくある
def sumof(*args):
	total = 0
	for i in args:
		total += i
	return total
print(sumof())
print(sumof(3,5))
print(sumof(3,5,7))

"""
0
8
15
"""

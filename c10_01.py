try:
	price = int(input('料金を入力 >>'))
	number = int(input('人数を入力 >>'))
	print(f'1人当たり{price/number}円です')
except ValueError:
	print('料金または人数は整数を入力してください')
print('プログラムを終了します')

"""
料金を入力 >>1000
人数を入力 >>a
料金または人数は整数を入力してください
プログラムを終了します
"""

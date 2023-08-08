def plus(x, y):
	answer = x + y
	return answer

answer = plus(100, 50)
print(f'足し算の答えは{answer}')


#同じメモリ空間を代入:関数を代入するか or 実行結果を代入するか

hoge = plus
n = hoge(5,8)
print(n)

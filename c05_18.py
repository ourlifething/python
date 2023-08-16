#２つの戻り値を返す？

def plus_and_minus(a, b):
	return a + b, a - b      # タプルを返している

next, prev = plus_and_minus(1978, 1) # タプルをアンパック

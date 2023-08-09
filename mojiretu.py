msg = 'hello'
ls = list(msg)
print(ls)

word = input ('英単語>>')
ls = list(word)
if len(word) == len(set(ls)):
		print('同じアルファベットは含まれていない')
else:
		print('同じアルファベットが含まれている')

text = input('今日何をした>>?')
with open('diary.txt', 'a') as file:
	file.write(text + '\n')
	#file.close()はいらない
	"""
	用が済んだらすぐに閉じる操作
	with open('diary.txt', 'a') as file:
	r: 読み込み
	w: 書き込み
	a: 追記
	"""

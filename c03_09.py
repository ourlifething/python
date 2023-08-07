score = int(input('試験の結果を入力して下さい>>'))
if score < 0 or score > 100:
	print('異常な得点です')
	print('入力しなおしてください')
elif score >= 60:
	print('合格！')
	print('よくがんばりましたね')
else:
	print('残念ながら不合格です')
	print('追試です')
	
    

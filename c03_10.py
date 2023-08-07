print('全ての質問にyまたはnで答えて下さい')
okane_aruka = input('お金に余裕ありますか？>>')
if okane_aruka == 'y':
	onaka_suiteruka =input('お腹すごく空いてますか？>>')
	nomitai_kibunnka = input('ビールを飲みたいですか？>>')
	if onaka_suiteruka == 'y' and nomitai_kibunnka == 'y':
		print('焼き肉はいかがですか')
	elif onaka_suiteruka == 'y':
		print('カレーはいかがですか')
	elif nomitai_kibunnka == 'y':
		print('焼き鳥はいかがですか')
	else:
	  	print('パスタはいかがですか')
	yashoku_iruka = input('夜食は必要ですか>>')
	if yashoku_iruka == 'y':
	    print('コンビニのチキンはいかがですか')
else:
  	print('家で食べましょう')

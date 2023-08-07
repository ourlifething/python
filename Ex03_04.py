num = int(input('入力１〜１２>>'))
if num in [1,3,5,7,8,10,12]:
	print('31日までありますね')
elif num == 4:
	print('30日までありますね')
	print(f'年が明けてから{num}ヶ月が過ぎました')
elif num == 2:
	print('1年で一番寒い月ですね')
	print(f'年が明けてから{num}ヶ月が過ぎました')
print(f'{num}ヶ月が過ぎました')


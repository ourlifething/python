name = input('あなたの名前を教えてください>>')
print(f'{name}さんこんにちは')
food = input(f'{name}さんの好きな食べ物を教えてください>>')

if 'カレー' in food:
	print('ステキですカレーは最高ですよね！！')
else:
	print(f'私も{food}が好きですよ')

day = int(input('今日は何日？＞＞'))
if not(day in[28,30,31]):
	print('入ってません')
else:
	print(f'{day}日は含まれます')



#デフォルト引数にカレーを設定した

def eat(breakfast, lunch, dinner = 'カレー'):
	print(f'朝は{breakfast}を食べました')
	print(f'昼は{lunch}を食べました')
	print(f'晩は{dinner}を食べました')

print('8月1日')
eat('トースト','おにぎり')
print('8月2日')
eat('納豆ごはん','ラーメン')
print('8月3日')
eat('バナナ','そば','焼き肉') #dinner=dinner = 'カレー'が置き換わる
print('8月4日')
eat('サンドウィッチ','しうまい弁当')

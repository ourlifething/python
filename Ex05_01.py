def weather():
	print('今日は晴れです')
weather()

def calc_circle_area(r):
	return r * r * 3.14
print(calc_circle_area(3.0))

"""ヒントを書くこともできる（変数の型を説明）"""
def calc_circle_area(r:float)->float:
	return r * r * 3.14
print(calc_circle_area(2.0))

#呼び出すと時刻を返す
def nowstr()->str: # 戻り値はstr
	return '18時 25分 30秒'
print(nowstr())

#呼び出すと時刻を調べて時分秒を返す
def nowint()->tuple:
	return(18,25,30)

h,m,s = nowint()
print(h,m,s)

def is_leapyear(year:int)->bool:
	return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

print(is_leapyear(2023)) #False
print(is_leapyear(2020)) #True

#うるう年の判定
year = int(input('何年>>'))
if is_leapyear(year):
	print(f'{year}はうるう年です')
else:
	print(f'{year}はうるう年ではありません')
	

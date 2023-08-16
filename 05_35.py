#グローバル変数 : 便利だけど書き換えられる可能性あるので注意

name = '松田' # global変数


def change_name():
	global name        # global name='浅木' 並べて代入はNG  global nameまでは OK
	name = '浅木'

def hello():
	print(f'こんにちは{name}さん')

change_name()
hello()

"""
こんにちは浅木さん
"""

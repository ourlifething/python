setting = {
	'設定1' :'メール送信',
	'設定2' :'リクエスト',
	'設定3' :'レスポンス',
}
for key in setting:
	print(key)

"""
設定1
設定2
設定3
"""
for value in setting.values():
	print(value)

"""
メール送信
リクエスト
レスポンス
"""
val = setting.values()
print(val)

"""
dict_values(['メール送信', 'リクエスト', 'レスポンス'
"""

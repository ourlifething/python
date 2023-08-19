setting = {
	'設置1' : 'メール送信',
	'設定2' : 'リクエスト',
	'設定3' : 'レスポンス',
}
itm = setting.items()
print(itm)
"""
dict_items([('設置', 'メール送信'), ('設定2', 'リクエスト'), ('設定3', 'レスポンス')])

"""
for key,value in setting.items():
	print(f'{key}は{value}です')
	
"""
設置1はメール送信です
設定2はリクエストです
設定3はレスポンスで
"""

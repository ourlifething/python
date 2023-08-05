
"""
セットの＆演算
セット１＆セット２
2人の共通する趣味一覧を表示
"""
member_hobbies = {
	'松田':{'SNS', '麻雀', '自転車'},
	'浅木':{'麻雀', '食べ歩き', '数学', '数学', '数学'}
	}

common_hobbies = member_hobbies['松田'] & member_hobbies['浅木']
print(common_hobbies) #{'麻雀'}


"""辞書型に[]リストを格納"""
member_hobbies = {
    '松田': ['SNS', '麻雀', '自転車'],
    '浅木': ['麻雀', '食べ歩き', '数学']
}
print(member_hobbies['松田'])
print(member_hobbies['松田'][0])

"""setにset格納"""
member_hobbies2 = {
    '松田': {'SNS', '麻雀', '自転車'},
    '浅木': {'麻雀', '食べ歩き', '数学'}
}
print(member_hobbies2['松田'])#{'SNS', '麻雀', '自転車'}順不同
#print(member_hobbies2['松田'][0]) エラー


scores = {'network':60, 'database':80, 'security':60}
members = ['松田', '浅木', '工藤']
tpl = tuple(members)
print(tpl)#リストmembersを材料にしてタプルを生成
list1 = list(scores)#scoresキーを集めたlistを生成
print(list1)#scoresのキーをリストに
set1 = set(scores.values())#scores valuesを材料としてsetを生成
print(set1)
n1 = int('8')#intコンストラクターに'8'をしてn1に代入している

codes = ['#ff0000','#00ff00','#0000ff']
colors = ['red', 'green', 'blue']
dict1 = dict(zip(codes, colors))
print(dict1)
codes1 = ['#ff0000','#00ff00','#0000ff']
colors1 = ['red','blk', 'green', 'blue']#要素数が違う...blueが省かれた
dict2 = dict(zip(codes1, colors1))
print(dict2)

""" 
('松田', '浅木', '工藤')
['network', 'database', 'security']
{80, 60}
{'#ff0000': 'red', '#00ff00': 'green', '#0000ff': 'blue'}
{'#ff0000': 'red', '#00ff00': 'blk', '#0000ff': 'green'}
"""

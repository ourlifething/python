scores = {'network':60, 'databese':80, 'security':50}
print(scores)
print(scores['network'])#60
scores['proguraming'] = 65 #追加
scores['security'] = 55 #変更
print(scores)
del scores['security']
print(scores)
print(f'合計：{sum(scores.values())}')

ls = [1,2,3]
del ls[1]
print(ls)

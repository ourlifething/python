scores1 = [80, 40, 50]
scores2 = [80, 40, 50]
print(f'scores1のidentity{scores1}')
print(f'scores2のidentity{scores2}')

if scores1 == scores2: # 等価判定：内容が等しい
	print('scores1とscores2は同じ内容です')
else:
	print('scores1とscores2は違う内容です')

if id(scores1) == id(scores2): # 等値判定：存在が等しい
	print('scores1とscores2は同じ存在です')
else:
	print('scores1とscores2は違う存在です')

print(id(scores1)) # 140681118352512
print(id(scores2)) # 140680580347712


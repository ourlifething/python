def analyze_score(sansu,kokugo,rika,syakai,eigo=None, *others):
	ls = [sansu,kokugo,rika,syakai]
	if eigo != None:
		ls.append(eigo)
	ls = ls + list(others) # 可変長引数 *others (タプル) をリストに変換
	max_score = max(ls)
	min_score = min(ls)
	avg_score = sum(ls) / len(ls)

	return [max_score, min_score, avg_score]

x,y,g = analyze_score(1,2,3,4,5,6,7)
print(x,y,g)
"""
7 1 4.0
"""

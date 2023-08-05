subjects = ['国語','算数','理科','社会','英語']
score =[]
for sub in subjects:
	score.append(int(input(sub)))
sub_score = dict(zip(subjects,score))
print(sub_score)

"""
国語90
算数95
理科80
社会70
英語90
{'国語': 90, '算数': 95, '理科': 80, '社会': 70, '英語': 90}
"""

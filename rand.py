import random


num = random.randint(5, 10) #5~10の値をランダムに生成（端含む）

num = int(input('何回ふる？'))
d = []
for n in range(num): 
	dice = random.randint(1, 6)
	d.append(dice)
	#d.append(random.randint(1,6))
print(d)
print(f'合計は{sum(d)}')
print(f'最大は{max(d)}')
print(f'最小は{min(d)}')

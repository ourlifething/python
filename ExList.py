import random


arr = list(range(0,101))
print(arr)

ls=[random.randint(0,100) for i in range(100)]
print(ls)

ls =[]
for i in range(100):
	ls.append(random.randint(0,100))
print(len(ls))
print(ls)
ls.sort(reverse=True)
print(ls[:10]) # [100, 97, 97, 95, 93, 93, 93, 92, 91, 89]
"""
sort()は戻り値がない
sorted()は戻り値がある
"""


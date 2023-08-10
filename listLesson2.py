import random


#内包表記
ls = [i for i in range(1,11)]
print(ls)    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ls = [i**2 for i in range(1,11)]
print(ls)    # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# サイコロを3回振ったときの目をリストにする
dices = [random.randint(1,6) for i in range(3)]
print(dices) # [2, 4, 1]
"""
dices = []
for i in range(3):
	dices.append(random.randint(1,6))
"""

ls = [str(i) for i in range(1,11)]
print(ls)    # ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
ls = [int(i) for i in ls]
print(ls)    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


ls = [i for i in range(1,10) if i % 2 == 0]
print(ls)    # [2, 4, 6, 8]
"""
ls = []
for i in range(1,10):
	if i % 2 == 0:
		ls.append(i)
"""

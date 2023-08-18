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

ls = [i*j for i in range(1,3) for j in range(1,3)]
print('35',ls) # [1, 2, 2, 4]
"""
ls=[]
for i in range(1,3):
	for j in range(1,3):
		ls.append(i*j)
"""

ls = [[i]*3 for i in range(3)]
print(ls) # [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
"""
ls =[]
for i in range(3):
	ls.append([i]*3)
"""

ls = [[i*j for j in range(3)] for i in range(3)]
print(ls) # [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
"""
ls =[]
for i in range(3):
	temp = []
	for j in range(3):
		temp.append(i*j)
	ls.append(temp)
"""
import pprint
ls = [[ i*j for j in range(1,10)]for i in range(1,10)]
pprint.pprint(ls)

n1,n2 = [int(i) for i in input('num>>').split(' ')]
print(n1,n2)

#3 5
str1 = input('num>>')
ls1 = str1.split(' ')
a,b = [int(i) for i in ls1]
print(a,b)


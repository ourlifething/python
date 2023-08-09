import pprint

data = [[1, 2, 3,],[4, 5, 6]]
print(data[1][2]) #6


data=[
		[1, 2, 3],
		[4, 5, 6], # , ok
]
print(data)


data = []
for i in range(10):
		temp = []
		for j in range(10):
				temp.append(0)
		data.append(temp)
print(data) 



data = []
for i in range(10):
		temp = []
		for j in range(10):
				temp.append(0)
		data.append(temp)
pprint.pprint(data) #二次元リストを綺麗に出力できる import pprint

"""
[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
"""


""""""

data = [1, 2, 3] + [4, 5]
print(data) #[1,2,3,4,5]

data = [1, 2, 3] * 3
print(data) # [1,2,3,1,2,3,1,2,3]

data = [None] * 10 #[None,None,None,None,None,None,None,None,None,None]
for i in range(len(data)):
		data[i] = [0] * 10
pprint.pprint(data)

"""
https://joytas.net/programming/python/2-list

[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
"""

"""内包表記:https://qiita.com/mjpurin/items/ec6d115b4ff13d36b6b7"""

data = [[0]*10 for i in range(10)]
pprint.pprint(data)

#ls = [for n in range(1,8)]

ls = [n for n in range(1,8)]
print(ls) # [1,2,3,4,5,6,7]

ls = [n**2 for n in range(1,8)]
print(ls) # [1,4,9,16,25,36,49]



ls = [n for n in range(1,8) if n%2 ==0]
"""
for n in range(1,8):
		if n % 2 == 0:
				n
"""				
print(ls) # [2,4,6]



ls = [i*10+j for i in range(1,3) for j in range(2,5)]
"""
for i in range(1,3):
		for j in range(2,5)
"""
print(ls) #[12,13,14,22,23,24]



#要素が２つある二次元配列
ls = [[i*10+j for j in range(7,10)] for i in range(1,3)]
print(ls) #[[17,18,19],[27,28,29]]


"""
ls = [[] for i in range(10)]#10行のリスト
ls = [[0 for j in range(10)] for i in range(10)]#要素０のリスト
"""

ls = [[0 for j in range(10)] for i in range(10)]
pprint.pprint(ls)
ls = [[0]*10 for i in range(10)]
pprint.pprint(ls)

"""
[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
"""


ls = [[i*10+j for j in range(1,11)] for i in range(10)]
pprint.pprint(ls)

"""
[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
 [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
 [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
 [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
 [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
 [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
 [61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
 [71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
 [81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
 [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]]
"""




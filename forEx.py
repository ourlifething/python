for i in range(5):
	print(i)

"""
range()メソッド
range(5) # 0,1,2,3,4
range(3,5) # 3,4
range(1,10,3) # 1,4,7
"""
print(list(range(1,10)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

print('---------------')


#1から10まで以下のように出力せよ。
#1 2 3 4 5 6 7 8 9 10
for i in range(1,11):
	print(i, end=' ')
print()


print('---------------')


for i in range(1,4):
	for j in range(1,11):
		print(i*j, end=' ')
	print()


"""
1 2 3 4 5 6 7 8 9 10
2 4 6 8 10 12 14 16 18 20
3 6 9 12 15 18 21 24 27 30
"""


print('---------------')


height = int(input('何段の階段を作る>>?'))
for i in range(height):
	for j in range(i+1):
		print('*', end=' ')
	print()

"""
*
* *
* * *
* * * *
* * * * *
"""

height = int(input('何段の階段を作る>>?'))
for i in range(height):
	for j in range(height,i,-1):
		print('*', end=' ')
	print()

"""
* * * * *
* * * *
* * *
* *
*
"""





import random


count =1

print('サイコロを振ったよ')
num1 = random.randint(1,6)
num2 = random.randint(1,6)
print(f'{count}回目{num1}')
count +=1
print(f'{count}回目{num2}')
maxnum = max(num1,num2)
if num1 == num2:
		print('同じ')
elif maxnum == num1:
		print(f'2回目は1回目よりも{num1-num2}小さいです')
else:
		print(f'1回目は2回目よりも{num2-num1}小さいです')


import random
count = 0
while True:
	count += 1
	num = random.randint(1,99999)
	print(f'{count}回目{num}')
	if num == 7777:
		break
print(f'{count}回目に出ました')

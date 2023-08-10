num = int(input('数字>>'))
count = []
for i in range(1,num+1):
	count.append(i)
print(f'{sum(count)}')

print(sum(range(1,num+1)))

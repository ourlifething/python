st = int(input('start>>num?'))
end = int(input('end>>num?'))

arr =[]
for i in range(st,end+1):
	if i % 2 == 0:
		arr.append(i)
print(arr)


for i in range(st,end+1):
	if i % 2 == 0:
		print(i, end=' ')
print()

for i in range(1,10):
	if i % 2 == 0:
		continue
	for j in range(1,10):
		ans = i * j
		if ans > 50:
			continue
		print(f'{i*j}',end=' ')
	print()



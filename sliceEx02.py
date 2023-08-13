ls = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J" ]
n = input()
n1 = n.split(' ')

n2=ls[:int(n1[0])]             #[:1]
n3=ls[int(n1[0]):-int(n1[2])]  #[1:-8]
n4=ls[-int(n1[2]):]            #[-8:]
n5 = [n2,n3,n4]

for i in range(len(n5)):       #3
	for j in range(len(n5[i])):
		print(n5[i][j],end='')
	print()


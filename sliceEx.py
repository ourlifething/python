"""スライス"""

s1 = 'Hello'
s2 = s1[1:3] # index1~3 1以上3未満
print(s2) #el

for c in s1:
	print(c)
for c in s1:
	print(c,end='')

l1 = [10, 20, 30, 40, 50]
l2 = l1[1:4] # [20,30,40]
print(l2)

l2 = l1[3:] # [40,50]
print(l2)

l2 = l1[:3] #3未満
print(l2)   #10,20,30

l2 = l1[:]  #配列の複製（メモリ空間に２つ)
print(l2)   #[10, 20, 30, 40, 50]

l2 = l1[-2:]
print(l2)   # [40,50]

l2 = l1[2:100] #ある範囲で出力
print(l2) #[30,40,50]

"""step"""

l1 = [10, 20, 30, 40, 50, 60, 70, 80]
l2 = l1[1:7:2] #[20,40,60] 1以上７未満２個飛ばし

l2 = l1[::-1]
print(l2) #[80,70,60,50,40,30,20,10] reverse

ls = [4, 10, 2, 5, 7]

print(ls)      # [4, 10, 2, 5, 7]
print(len(ls)) # 5
print(ls[0])   # 4
print(ls[-1])  # 7

#リストの操作
for i in ls:
	print(i,end=' ')
print()


ls[0] = 1      # 要素の更新

ls.append(10)  # 末尾に追加

del ls[-1]     # リストの最後の要素を削除

n = ls.pop()   # 配列の末尾の値を削除してnに代入
n1 = ls.pop(0) # 先頭を削除してn1に代入
print(n,n1)    # 7 1

ls2 = [1,2,3]
ls3 = [4,5,6]
ls4 = ls2 + ls3 # [1,2,3,4,5,6]

ls5 = ls2 * 3   # [1,2,3,1,2,3,1,2,3]

ls6 = [3,1,4]
ls6.sort()      # 昇順ソート
print(ls6)      # [1, 3, 4]
ls6.sort(reverse = True)
print(ls6)      # [4, 3, 1]

"""リストをシャッフル"""
import random

ls7 = [1,2,3,4,5,6,7,8,9]
random.shuffle(ls7)
print(ls7)      # [8, 9, 1, 3, 6, 7, 4, 5, 2]

data = ['大吉','中吉','小吉','吉','凶']
result = random.choice(data)
print(result)   # ランダムに１つ選ぶ




n = int(input())
#print(n)#5

arr_nenrei=[]
for i in range(n):
    nenrei= int(input())
    arr_nenrei.append(nenrei)
#print(arr_nenrei) #[10, 20, 30, 40, 50]

m = int(input())
#print(m)#2

"""配列の中身が２個以上の時のシュミレーション"""
#arr2=[['2', '4', '10'], ['1', '3', '15'],['1','2','5']]


arr2=[]
for i in range(m):
    do = input()
    wakeru= do.split()#配列にする
    arr2.append(wakeru)
#print(arr2) #[['2', '4', '10'], ['1', '3', '15']]

"""配列の中身を文字列から整数に変更"""
arr3=[[int(arr2[i][j]) for j in range(len(arr2[i]))] for i in range(len(arr2))]
#print(arr3)#[[2, 4, 10], [1, 3, 15], [1, 2, 5]]


arr4=[]
for j in range(len(arr3)):
    arr5=[]
    for i in range(len(arr_nenrei)):
        if i+1 >= arr3[j][0] and i+1 <= arr3[j][1] and arr_nenrei[i]>=arr3[j][2]:
            arr5.append(arr3[j][2])
        elif  i+1 >= arr3[j][0] and i+1 <= arr3[j][1] and arr_nenrei[i] > 0:
            arr5.append(arr_nenrei[i])
        else:
            arr5.append(0)
    arr4.append(arr5)     
#print(arr4)#[[0, 10, 10, 10, 0], [10, 15, 15, 0, 0], [5, 5, 0, 0, 0]]
"""配列を足し合わせる↑これを↓これにする"""
t=[sum(i) for i in zip(*arr4)]　"""zip(*___)タプル化している"""
#print(t)#[15, 30, 25, 10, 0]

"""*（アスタリスク）は、Pythonにおいてアンパック演算子（Unpacking Operator）として使用されます。
具体的には、* を使うと、リストやタプル内の要素を展開して個別の引数として渡すことができます。
これは、関数への引数の渡し方と結びついており、リストやタプル内の要素を関数に渡す際に非常に便利です。"""

num=[]
for i in range(len(arr_nenrei)):#[10, 20, 30, 40, 50]
    if t[i] <= arr_nenrei[i]:
        num.append(t[i])
    else:
        num.append(arr_nenrei[i])
#print(num)   
for i in num:
    print(i)

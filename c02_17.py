scores  = (70, 80, 55)#タプル
#scores[0] = 100 error タプルはイミュータブル、変更できない 
print(scores)
print(scores[0])
print(f'要素数は{len(scores)}')
print(f'合計は{sum(scores)}')



scores2  = [70, 80, 55]
print(scores2)
print(scores2[0])
print(f'要素数は{len(scores2)}')
print(f'合計は{sum(scores2)}')

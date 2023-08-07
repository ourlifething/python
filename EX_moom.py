dist = 384400 * 1000 * 1000 #月までの距離 km*1000=m  m*1000=mm
thickness = 1 #紙の厚さ
count = 0 #折り曲げた回数

while dist > thickness:
		thickness *= 2
		count += 1

		print(f'{count}回折り曲げた：厚み{thickness}')
print(f'{count}回で到着した')


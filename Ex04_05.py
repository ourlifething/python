temp = [7.8, 9.1, 10.2, 11.0, 12.5, 12.4, 14.3, 13.8, 12.9, 12.4]
for t in temp:
	print(t)
temp_new = temp[:]#[:]#リストの複製参照先も違う
temp_new[5] = 'N/A'
print(temp)
print(temp_new)

del temp_new[5]
print(f'平均気温：{sum(temp_new)/len(temp_new):.1f}')


"""
7.8
9.1
10.2
11.0
12.5
12.4
14.3
13.8
12.9
12.4
[7.8, 9.1, 10.2, 11.0, 12.5, 12.4, 14.3, 13.8, 12.9, 12.4]
[7.8, 9.1, 10.2, 11.0, 12.5, 'N/A', 14.3, 13.8, 12.9, 12.4]
平均気温：11.6

"""
#isinstance()

temp_data = []
for t in temp_new:
	if not isinstance(t,float):
		continue
	temp_data.append(t)
print(f'平均気温：{sum(temp_new)/len(temp_new):.1f}')
#平均気温：11.6













x = 10
x = x + 100
x = x / 3
print(f'{x:.2f}')  # 36.67
print(type(x))     # <class 'float'>
# print(x:.2f)   error

height = float(input('身長cm>>'))
weight = float(input('体重kg>>'))
bmi = weight / (height/100 * height / 100)
print(f'BMIは{bmi}です')
print(f'BMIは{bmi:.2f}です')#小数点２桁


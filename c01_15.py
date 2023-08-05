price = input('料金を入力>>')#戻り値str
print(type(price))
number = int(input('人数を入力>>'))
print(type(price))
payment = price / number
print('お支払いは'+ payment + '円です')

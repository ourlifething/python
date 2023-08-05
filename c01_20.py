price = input('料金を入力>>')#戻り値str
price =int(price)
number = int(input('人数を入力>>'))
payment = int(price / number)
print('お支払いは'+ str(payment) + '円です')


"""
1人辺りの支払額は支払い総額を参加人数で割った金額
支払いの単位は100円とし100円未満の金額がある場合は切り上げる
支払額を超過した分は漢字が受け取ることができる
"""

def int_input(msg):
	if msg == 'amount':
		amount = int(input(f'支払い総額を入力>>'))
		return amount
	elif msg == 'people':
		people = int(input(f'参加人数を入力>>'))
		return people


def calc_payment(amount, people):
	dnum = amount / people
	pay = dnum // 100 * 100

	if dnum > pay:
		pay = int(pay + 100)
	payorg = amount - pay * (people - 1)
	return payorg, pay


def show_payment(pay,payorg,people=2):
	print('***支払額***')
	print(f'1人あたり{pay:.0f}円({people-1}人)、幹事は{payorg:.0f}円です')

def warikan():
	amount = int_input('amount')
	people = int_input('people')
	payorg,pay = calc_payment(amount,people)
	show_payment(pay,payorg,people)

warikan()

import tkinter as tk

KEKKA = [
'前世が猫だった可能性は極めて低いです',
'いたって普通の人間です',
'特別、おかしなところはありません',
'やや猫っぽいところがあります',
'猫に近い性格のようです',
'猫にかなり近い性格です',
'前世は猫だったかもしれません',
'見た目は人間中身は猫の可能性があります',
]
ITEM = [
'高いところが好き',
'ボールを見ると転がしたくなる',
'ビックリすると髪の毛が逆立つ',
'ネズミのおもちゃが気になる',
'ニオイに敏感',
'魚の骨をしゃぶりたくなる',
'夜元気になる',
]

def click_btn():
	pts = 0
	for i in range(7):
		if bvar[i].get() == True:
			pts += 1
	nekodo = int(100*pts/7)
	text.delete('1.0',tk.END)
	text.insert('1.0', '<診断結果>\nあなたの猫度は{}%です。\n{}'.format(nekodo,KEKKA[pts]))

root = tk.Tk()
root.title('ネコ診断アプリ')
root.resizable(False,False)
canvas = tk.Canvas(root,width=800, height=600)
canvas.pack()
img = tk.PhotoImage(file='sumire.png')
canvas.create_image(400, 300, image=img)
button = tk.Button(text='診断する', font=('Times New Roman', 32), bg='lightgreen', command=click_btn)
button.place(x=400, y=480)
text = tk.Text(width=40, height=5, font=('Times New Roman', 16))
text.place(x=320, y=30)

bvar = [None]*7
cbtn = [None]*7

for i in range(7):
	bvar[i] = tk.BooleanVar()
	bvar[i].set(False)
	cbtn[i] = tk.Checkbutton(text=ITEM[i], font=('Times New Roman', 12), variable=bvar[i], bg='#dfe')
	cbtn[i].place(x=400, y=160+40*i)
root.mainloop()

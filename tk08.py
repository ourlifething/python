import tkinter as tk # sqlのasと同じ
import random

def btn_click():
	label['text'] = random.choice(['大吉','中吉','小吉','凶'])
	label.update()

root = tk.Tk()
root.title('おみくじ') #タイトルを設定
root.resizable(False,False) # 画面サイズ変更禁止

canvas = tk.Canvas(root,width=800,height=600)
canvas.pack()
img = tk.PhotoImage(file='miko.png')

canvas.create_image(400,300,image=img) #中点
label = tk.Label(root,text='??',font=('Arial',120),bg='white')
label.place(x=380,y=60)
btn = tk.Button(root,text="おみくじを引く",font=('Arial',36),command=btn_click,bg='skyblue')
btn.place(x=370,y=400)
root.mainloop()


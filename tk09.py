import tkinter as tk

def btn_click():
	txt = entry.get()
	btn['text']=txt
root=tk.Tk()
root.title('My Window')
root.geometry('400x200')
entry=tk.Entry(width=20)
btn=tk.Button(text='文字列の取得',command=btn_click)
btn.place(x=20,y=100)
root.mainloop()

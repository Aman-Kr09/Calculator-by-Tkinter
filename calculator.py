from tkinter import *
from tkinter import messagebox
import math


def message():
	messagebox.showinfo(title='About Us', message='HAPPY REPUBLIC DAY')

def his():
	history_window =Toplevel(root)
	history_window.title("Calculation History")
	history_window.geometry("300x400")
	history_listbox =Listbox(history_window,font=('lucida',12),width=40)
	history_listbox.pack(pady=10,padx=10,fill=BOTH,expand=True)
	for h in calc_history:
		history_listbox.insert(END,h)


def type_input(val):
	input.insert(END, val)


def clear():
	input.delete(0, END)


def solve(expre):
	try:
		global i
		res = eval(expre)
		result.insert(END, f'({i})Answer = {res}')
		calc_history.append(f'({i})Answer = {res}')
		i=i+1
	except:
		try:
			expre = expre.replace('sin', 'math.sin')
			expre = expre.replace('cos', 'math.cos')
			expre = expre.replace('tan', 'math.tan')
			expre = expre.replace('log', 'math.log')
			expre = expre.replace('exp', 'math.e**')
			res = eval(expre)
			result.insert(END, f'({i})Answer = {res}')
			calc_history.append(f'({i})Answer = {res}')
			i=i+1
		except:
			messagebox.showwarning(title='Invalid Expression', message='Please provide valid expression')


root = Tk()
root.geometry('320x570')
root.title('Calculator')

root.wm_iconbitmap("C:/Users/Seenu/OneDrive/Desktop/PYTHON/tkinter/hello.ico")

menu_bar = Menu(root)

i=1
calc_history = []

open = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='HELLO!', menu=open)
open.add_command(label='GREET', command=message)
menu_history = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='History', menu=menu_history)
menu_history.add_command(label='View History', command=his)
exit = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='Exit', menu=exit)
exit.add_command(label='Close', command=quit)

root.config(menu=menu_bar)


top_frame = Frame(root).pack()
result = Listbox(top_frame, height=5, width=20, font=('lucida', 20, 'bold'),background="orange")
result.pack(pady=10)


input = Entry(top_frame, width=50, borderwidth=5, bd=5, font=('lucida', 15, 'bold'))   #Entry is used to entre our expression
input.pack(pady=10)
input.focus_set()

#window and root exchange krna hai and change messages and architecture history of calculator
keys = Frame(root)
keys.pack() #all buttons packed here

# number buttons     #execute when button pressed

b0 = Button(keys, text='0',padx=40,relief=GROOVE, borderwidth=5, command=lambda: type_input(0), font=('lucida', 10, 'bold')).grid(row=2, column=0)
b1 = Button(keys, text='1',padx=40,relief=GROOVE, borderwidth=5,background="blue", command=lambda: type_input(1), font=('lucida', 10, 'bold')).grid(row=2, column=1)
b2 = Button(keys, text='2',padx=40,relief=GROOVE, borderwidth=5, command=lambda: type_input(2), font=('lucida', 10, 'bold')).grid(row=2, column=2)
b3 = Button(keys, text='3',padx=40,relief=GROOVE, borderwidth=5, command=lambda: type_input(3), font=('lucida', 10, 'bold')).grid(row=3, column=0)
b4 = Button(keys, text='4',padx=40,relief=GROOVE, borderwidth=5,background="blue", command=lambda: type_input(4), font=('lucida', 10, 'bold')).grid(row=3, column=1)
b5 = Button(keys, text='5',padx=40,relief=GROOVE, borderwidth=5, command=lambda: type_input(5), font=('lucida', 10, 'bold')).grid(row=3, column=2)
b6 = Button(keys, text='6',padx=40,relief=GROOVE, borderwidth=5, command=lambda: type_input(6), font=('lucida', 10, 'bold')).grid(row=4, column=0)
b7 = Button(keys, text='7',padx=40,relief=GROOVE, borderwidth=5, command=lambda: type_input(7), font=('lucida', 10, 'bold')).grid(row=4, column=1)
b8 = Button(keys, text='8',padx=40,relief=GROOVE, borderwidth=5, command=lambda: type_input(8), font=('lucida', 10, 'bold')).grid(row=4, column=2)
b9 = Button(keys, text='9',padx=40,relief=GROOVE, borderwidth=5,background="green", command=lambda: type_input(9), font=('lucida', 10, 'bold')).grid(row=5, column=0)
b10 = Button(keys, text='+',padx=40, relief=GROOVE, borderwidth=5, background="green",command=lambda: type_input('+'), font=('lucida', 10, 'bold')).grid(row=5, column=1)
b11 = Button(keys, text='-',padx=40, relief=GROOVE, borderwidth=5, background="green",command=lambda: type_input('-'), font=('lucida', 10, 'bold')).grid(row=5, column=2)
b12 = Button(keys, text='x',padx=40, relief=GROOVE, borderwidth=5,background="green", command=lambda: type_input('*'), font=('lucida', 10, 'bold')).grid(row=6, column=0)
b13 = Button(keys, text='/',padx=40, relief=GROOVE, borderwidth=5,background="green", command=lambda: type_input('/'), font=('lucida', 10, 'bold')).grid(row=6, column=1)
b14 = Button(keys, text='==',padx=35, relief=GROOVE, borderwidth=5,background="green", command=lambda: solve(input.get()), font=('lucida', 10, 'bold')).grid(row=6, column=2)
b15 = Button(keys, text='sin',padx=35, relief=GROOVE, borderwidth=5, background="green",command=lambda: type_input('sin'), font=('lucida', 10, 'bold')).grid(row=7, column=0)
b16 = Button(keys, text='cos',padx=33, relief=GROOVE, borderwidth=5,background="green", command=lambda: type_input('cos'), font=('lucida', 10, 'bold')).grid(row=7, column=1)
b17 = Button(keys, text='tan',padx=35, relief=GROOVE, borderwidth=5,background="green", command=lambda: type_input('tan'), font=('lucida', 10, 'bold')).grid(row=7, column=2)
b18 = Button(keys, text='log',padx=35, relief=GROOVE, borderwidth=5,background="green", command=lambda: type_input('log'), font=('lucida', 10, 'bold')).grid(row=8, column=0)
b19 = Button(keys, text='.',padx=40, relief=GROOVE, borderwidth=5, background="green",command=lambda: type_input('.'), font=('lucida', 10, 'bold')).grid(row=8, column=1)
b20 = Button(keys, text='exp',padx=35, relief=GROOVE, borderwidth=5,background="green", command=lambda: type_input('exp'), font=('lucida', 10, 'bold')).grid(row=8, column=2)
b21 = Button(keys, text='(',padx=42, relief=GROOVE, borderwidth=5,background="green", command=lambda: type_input('('), font=('lucida', 10, 'bold')).grid(row=9, column=0)
b22 = Button(keys, text=')',padx=42, relief=GROOVE, borderwidth=5,background="green", command=lambda: type_input(')'), font=('lucida', 10, 'bold')).grid(row=9, column=1)
b23 = Button(keys, text='clear', padx=32,relief=GROOVE,borderwidth=5,background="green", command=clear, font=('lucida', 10, 'bold')).grid(row=9, column=2)


status = StringVar()
status.set('Calculator made by _shinu_aman_')

Label(root, textvariable=status, width=30, relief=SUNKEN, bg='grey', fg='black', font=('Helvetica', 15)).pack(side=BOTTOM ,fill=X)

root.mainloop()
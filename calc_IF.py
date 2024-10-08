from tkinter import *

root = Tk()
root.title('Calculator')

#user_input = Entry(root, width=35, borderwidth=5)
user_input = Entry(root, width=50, borderwidth=5)
user_input.grid(row=0, column=0, columnspan=3, padx=10,pady=10)

def btn_click(number):
    current = user_input.get()
    user_input.delete(0, END)
    user_input.insert(0,str(current) + str(number))

def btn_cls():
    user_input.delete(0, END)

def btn_add():
    first_num = user_input.get()
    global f_num
    global opp
    opp = 'add'
    f_num = int(first_num)
    user_input.delete(0, END)

def btn_div():
    first_num = user_input.get()
    global f_num
    global opp
    opp = 'div'
    f_num = int(first_num)
    user_input.delete(0, END)

def btn_mult():
    first_num = user_input.get()
    global f_num
    global opp
    opp = 'mult'
    f_num = int(first_num)
    user_input.delete(0, END)

def btn_sub():
    return

def btn_equals():
    second_num = user_input.get()
    user_input.delete(0, END)
    if opp == 'add':
        user_input.insert(0, f_num + int(second_num))
    elif opp == 'div':
        user_input.insert(0, f_num / int(second_num))   
    elif opp == 'mult':
        user_input.insert(0, f_num * int(second_num))   
    #elif opp ==  'opp':    

#defining keypad digit buttons
btn1 = Button(root, text='1', padx=40, pady=20, command=lambda:btn_click(1))
btn2 = Button(root, text='2', padx=40, pady=20, command=lambda:btn_click(2))
btn3 = Button(root, text='3', padx=40, pady=20, command=lambda:btn_click(3))
btn4 = Button(root, text='4', padx=40, pady=20, command=lambda:btn_click(4))
btn5 = Button(root, text='5', padx=40, pady=20, command=lambda:btn_click(5))
btn6 = Button(root, text='6', padx=40, pady=20, command=lambda:btn_click(6))
btn7 = Button(root, text='7', padx=40, pady=20, command=lambda:btn_click(7))
btn8 = Button(root, text='8', padx=40, pady=20, command=lambda:btn_click(8))
btn9 = Button(root, text='9', padx=40, pady=20, command=lambda:btn_click(9))
btn0 = Button(root, text='0', padx=40, pady=20, command=lambda:btn_click(0))

#functional buttons
btn_cls = Button(root, text='clear', padx=31, pady=20, command=btn_cls)
btn_equals = Button(root, text='equals', padx=27, pady=20, command=btn_equals)

#operation buttons
btn_add = Button(root, text='add', padx=33, pady=20, command=btn_add)
btn_div = Button(root, text='div', padx=35, pady=20, command=btn_div)
btn_mult = Button(root, text='mult', padx=31, pady=20, command=btn_mult)
btn_sub = Button(root, text='sub', padx=40, pady=20, command=btn_sub)

#displaying buttons
btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)

btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)

btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)

btn0.grid(row=4, column=0)
btn_cls.grid(row=4,column=1)
btn_equals.grid(row=4,column=2)

btn_add.grid(row=5,column=0)
btn_div.grid(row=5,column=1)
btn_mult.grid(row=5, column=2)

#btn_sub.grid(row=,column=)


root.mainloop()
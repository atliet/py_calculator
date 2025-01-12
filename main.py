from tkinter import *

exp = ""

def press(num):
    global exp
    exp = exp + str(num)
    eq.set(exp)

def equalPress():
    try:
        global exp
        total = str(eval(exp))
        eq.set(total)
        exp = total
    except:
        eq.set(" Error ")
        exp = ""

def clear():
    global exp
    exp = ""
    eq.set("")

if __name__ == "__main__":
    GUI = Tk()
    GUI.configure(background="white")
    GUI.title("Very simple calculator with Python TKInter")
    GUI.geometry("270x150")

    eq = StringVar()

    exp_field = Entry(GUI, textvariable=eq)
    exp_field.grid(columnspan=4, ipadx=70)

    # Number buttons
    button1 = Button(GUI, text=' 1 ', fg='black', bg='red', command=lambda: press(1), height=1, width=7) 
    button1.grid(row=2, column=0) 
    button2 = Button(GUI, text=' 2 ', fg='black', bg='red', command=lambda: press(2), height=1, width=7) 
    button2.grid(row=2, column=1) 
    button3 = Button(GUI, text=' 3 ', fg='black', bg='red', command=lambda: press(3), height=1, width=7) 
    button3.grid(row=2, column=2) 
    button4 = Button(GUI, text=' 4 ', fg='black', bg='red', command=lambda: press(4), height=1, width=7) 
    button4.grid(row=3, column=0) 
    button5 = Button(GUI, text=' 5 ', fg='black', bg='red', command=lambda: press(5), height=1, width=7) 
    button5.grid(row=3, column=1) 
    button6 = Button(GUI, text=' 6 ', fg='black', bg='red', command=lambda: press(6), height=1, width=7) 
    button6.grid(row=3, column=2) 
    button7 = Button(GUI, text=' 7 ', fg='black', bg='red', command=lambda: press(7), height=1, width=7) 
    button7.grid(row=4, column=0) 
    button8 = Button(GUI, text=' 8 ', fg='black', bg='red', command=lambda: press(8), height=1, width=7) 
    button8.grid(row=4, column=1) 
    button9 = Button(GUI, text=' 9 ', fg='black', bg='red', command=lambda: press(9), height=1, width=7) 
    button9.grid(row=4, column=2) 
    button0 = Button(GUI, text=' 0 ', fg='black', bg='red', command=lambda: press(0), height=1, width=7) 
    button0.grid(row=5, column=0) 

    # Math symbol and action buttons
    plus = Button(GUI, text=' + ', fg='black', bg='red', command=lambda: press("+"), height=1, width=7) 
    plus.grid(row=2, column=3) 
    minus = Button(GUI, text=' - ', fg='black', bg='red', command=lambda: press("-"), height=1, width=7) 
    minus.grid(row=3, column=3) 
    multiply = Button(GUI, text=' * ', fg='black', bg='red', command=lambda: press("*"), height=1, width=7) 
    multiply.grid(row=4, column=3) 
    divide = Button(GUI, text=' / ', fg='black', bg='red', command=lambda: press("/"), height=1, width=7) 
    divide.grid(row=5, column=3) 
    equal = Button(GUI, text=' = ', fg='black', bg='red', command=equalPress, height=1, width=7) 
    equal.grid(row=5, column=2) 
    clear = Button(GUI, text='Clear', fg='black', bg='red', command=clear, height=1, width=7) 
    clear.grid(row=5, column='1') 
    Decimal= Button(GUI, text='.', fg='black', bg='red', command=lambda: press('.'), height=1, width=7) 
    Decimal.grid(row=6, column=0) 

    GUI.mainloop()

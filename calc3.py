# Code made by @treywaevin on github

from tkinter import *

# Create window
win = Tk()
win.title('Calculator')
win.geometry('525x675')
win.resizable(False, False)

# Instances
expression = ""
neg = False


# Button Inputs
def inputNum(digit):
    global expression
    global neg
    if digit is 'C':
        print('test')
        expression = ""
        equation.config(text="0")
    elif digit is "sign":
        if not neg:
            expression += "-"  # adds neg symbol to beginning of num
            neg = True
            equation.config(text=expression)
        else:
            try:
                if equation[(len(expression) - 1):] == '-':
                    expression = expression[0:(len(expression) - 1)]
                equation.config(text=expression)
            except TypeError:
                print('error')

    elif digit is '%':
        decimal = float(expression) / 100
        expression = str(decimal)
        equation.config(text=expression)
    else:
        print('else')
        expression += str(digit)
        equation.config(text=expression)


# Evaluate Equation
def evalEq():
    global expression
    # displays error when answer cannot be computed
    try:
        solution = eval(expression)
        expression = str(solution)
        equation.config(text=expression)
    except ZeroDivisionError:
        equation.config(text="error")


# Layout labels and buttons

equation = Label(win, background='grey', foreground='white', text='0', anchor='e', height=6, font=("Courier,90"))
equation.grid(row=0, column=0, sticky='nsew', columnspan=4)
btnClear = Button(win, background='light grey', text='C', command=lambda: inputNum('C')).grid(row=1, column=0, ipadx=53,
                                                                                              ipady=45)
btnSign = Button(win, background='light grey', text='+/-', command=lambda: inputNum('sign')).grid(row=1, column=1,
                                                                                                  ipadx=53, ipady=45)
btnPcnt = Button(win, background='light grey', text='%', command=lambda: inputNum('%')).grid(row=1, column=2, ipadx=59,
                                                                                             ipady=45)
btnPlus = Button(win, background='orange', text='+', command=lambda: inputNum('+')).grid(row=1, column=3, ipadx=53,
                                                                                         ipady=45)

btn1 = Button(win, background='light grey', text='1', command=lambda: inputNum(1)).grid(row=2, column=0, ipadx=54,
                                                                                        ipady=45)
btn2 = Button(win, background='light grey', text='2', command=lambda: inputNum(2)).grid(row=2, column=1, ipadx=59,
                                                                                        ipady=45)
btn3 = Button(win, background='light grey', text='3', command=lambda: inputNum(3)).grid(row=2, column=2, ipadx=60,
                                                                                        ipady=45)
btnSub = Button(win, background='orange', text='-', command=lambda: inputNum('-')).grid(row=2, column=3, ipadx=55,
                                                                                        ipady=45)

btn4 = Button(win, background='light grey', text='4', command=lambda: inputNum(4)).grid(row=3, column=0, ipadx=54,
                                                                                        ipady=45)
btn5 = Button(win, background='light grey', text='5', command=lambda: inputNum(5)).grid(row=3, column=1, ipadx=59,
                                                                                        ipady=45)
btn6 = Button(win, background='light grey', text='6', command=lambda: inputNum(6)).grid(row=3, column=2, ipadx=59,
                                                                                        ipady=45)
btnMul = Button(win, background='orange', text='x', command=lambda: inputNum('*')).grid(row=3, column=3, ipadx=55,
                                                                                        ipady=45)

btn7 = Button(win, background='light grey', text='7', command=lambda: inputNum(7)).grid(row=4, column=0, ipadx=54,
                                                                                        ipady=45)
btn8 = Button(win, background='light grey', text='8', command=lambda: inputNum(8)).grid(row=4, column=1, ipadx=59,
                                                                                        ipady=45)
btn9 = Button(win, background='light grey', text='9', command=lambda: inputNum(9)).grid(row=4, column=2, ipadx=59,
                                                                                        ipady=45)
btnDiv = Button(win, background='orange', text='/', command=lambda: inputNum('/')).grid(row=4, column=3, ipadx=55,
                                                                                        ipady=45)

btn0 = Button(win, background='light grey', text='0', command=lambda: inputNum(0)).grid(row=5, column=0, ipadx=54,
                                                                                        ipady=45, columnspan=2,
                                                                                        sticky='nsew')
btnDec = Button(win, background='light grey', text='.', command=lambda: inputNum('.')).grid(row=5, column=2, ipadx=59,
                                                                                            ipady=45)
btnEval = Button(win, background='orange', text='=', command=evalEq).grid(row=5, column=3, ipadx=55, ipady=45)

win.mainloop()
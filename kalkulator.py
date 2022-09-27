from tkinter import *
import math

root = Tk()
root.title("Calculator")
root.geometry("480x300")
root.resizable(width = False, height = False)

calculator = Frame(root)
calculator.grid()

class Calculator():
    def __init__(self):
        self.current = ""
        self.total = 0
        self.operation = ""
        self.result = False
        self.input = True
        self.check_sum = False

    def enterNumber(self, number):
        first = display.get()
        second = str(number)
        self.result = False
        if self.input:
            self.current = second
            self.input = False
        else:
            if second == ".":
                if second in first:
                    return
            self.current = first + second
        self.output(self.current)

    
    def reg_operations(self):
        if self.operation == "add":
            self.total += self.current
        if self.operation == "subtract":
            self.total -= self.current
        if self.operation == "multiply":
            self.total *= self.current
        if self.operation == "divide":
            self.total /= self.current
        if self.operation == "mod":
            self.total %= self.current
        
        self.check_sum = False
        self.input = True
        self.output(self.total)

    def operations(self, operation):
        self.current = float(self.current)
        if self.check_sum:
            self.reg_operations()
        elif not self.result:
            self.total = self.current
            self.input = True
        
        self.check_sum = True
        self.operation = operation
        self.result = False

    def output(self, value):
        display.delete(0, END)
        display.insert(0, value)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.reg_operations()
        else:
            self.total = float(display.get())

    def clear(self):
        self.result = False
        self.current = "0"
        self.output(0)
        self.input = True 

    def clear_all(self):
        self.clear()
        self.total = 0

    def pi(self):
        self.result = False
        self.current = math.pi
        self.output(self.current)

    def tau(self):
        self.result = False
        self.current = math.tau
        self.output(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.output(self.current)

    def mathPM(self):
        self.result = False
        self.current = -(float(display.get()))
        self.output(self.current)

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(display.get()))
        self.output(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(display.get())))
        self.output(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(display.get())))
        self.output(self.current)

    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(display.get())))
        self.output(self.current)

    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(display.get())))
        self.output(self.current)

    def asinh(self):
        self.result = False
        self.current = math.asinh(float(display.get()))
        self.output(self.current)

    def acosh(self):
        self.result = False
        self.current = math.acosh(float(display.get()))
        self.output(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(display.get())))
        self.output(self.current)

    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(display.get())))
        self.output(self.current)

    def log(self):
        self.result = False
        self.current = math.log(float(display.get()))
        self.output(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp(float(display.get()))
        self.output(self.current)
    
    def expm1(self):
        self.result = False
        self.current = math.expm1(float(display.get()))
        self.output(self.current)

    def lgamma(self):
        self.result = False
        self.current = math.lgamma(float(display.get()))
        self.output(self.current)

    def degrees(self):
        self.result = False
        self.current = math.degrees(float(display.get()))
        self.output(self.current)

    def log2(self):
        self.result = False
        self.current = math.log2(float(display.get()))
        self.output(self.current)

    def log10(self):
        self.result = False
        self.current = math.log10(float(display.get()))
        self.output(self.current)

    def log1p(self):
        self.result = False
        self.current = math.log1p(float(display.get()))
        self.output(self.current)

value = Calculator()

    

display = Entry(calculator, width = 30, justify = RIGHT)
display.grid(row = 0, column = 0, columnspan = 4, pady=1)
display.insert(0, "0")

numbers = "789456123"
i=0
buttons = []

for j in range(2,5):
	for k in range(3):
		buttons.append(Button(calculator, width = 6, height = 2,
						bd = 4,text = numbers[i]))
		buttons[i].grid(row = j, column = k, pady = 1)
		buttons[i]["command"] = lambda x = numbers[i]: value.enterNumber(x)
		i+=1   

btnZero = Button(calculator, text = "0",
                width = 6, height = 2, bd = 4,
                command = lambda: value.enterNumber(0)).grid(row = 5, column = 0, pady = 1)

btnClear = Button(calculator, text = "C",
                width = 6, height = 2, bd = 4,
                command = value.clear).grid(row = 1, column = 0, pady = 1)

btnClearAll = Button(calculator, text = "CE",
                width = 6, height = 2, bd = 4,
                command = value.clear_all).grid(row = 1, column = 1, pady = 1)  

btnsq = Button(calculator, text = "\u221A", 
            width = 6, height = 2, bd = 4,
            command = value.squared).grid(row = 1, column = 2, pady = 1)

btnadd = Button(calculator, text = "+", 
            width = 6, height = 2, bd = 4,
            command = lambda: value.operations("add")).grid(row = 1, column = 3, pady = 1)

btnsub = Button(calculator, text = "-", 
            width = 6, height = 2, bd = 4,
            command = lambda: value.operations("subtract")).grid(row = 2, column = 3, pady = 1)

btnmul = Button(calculator, text = "*", 
            width = 6, height = 2, bd = 4,
            command = lambda: value.operations("multiply")).grid(row = 3, column = 3, pady = 1)

btndiv = Button(calculator, text = "/", 
            width = 6, height = 2, bd = 4,
            command = lambda: value.operations("divide")).grid(row = 4, column = 3, pady = 1)

btndot = Button(calculator, text = ".", 
            width = 6, height = 2, bd = 4,
            command = lambda: value.enterNumber(".")).grid(row = 5, column = 1, pady = 1)

btnPM = Button(calculator, text = chr(177), 
            width = 6, height = 2, bd = 4,
            command = value.mathPM).grid(row = 5, column = 2, pady = 1)

btnEquals = Button(calculator, text = "=",
            width = 6, height = 2, bd = 4,
            command = value.sum_of_total).grid(row = 5, column = 3, pady = 1)

#Napredne funkcije

btnPi = Button(calculator, text = "pi", 
            width = 6, height = 2, bd = 4,
            command = value.pi).grid(row = 1, column = 4, pady = 1)

btnSin = Button(calculator, text = "sin", 
            width = 6, height = 2, bd = 4,
            command = value.sin).grid(row = 1, column = 5, pady = 1)

btnCos = Button(calculator, text = "cos", 
            width = 6, height = 2, bd = 4,
            command = value.cos).grid(row = 1, column = 6, pady = 1)

btnTan = Button(calculator, text = "tan", 
            width = 6, height = 2, bd = 4,
            command = value.tan).grid(row = 1, column = 7, pady = 1)




btn2Pi = Button(calculator, text = "2pi", 
            width = 6, height = 2, bd = 4,
            command = value.tau).grid(row = 2, column = 4, pady = 1)


btnSinh = Button(calculator, text = "sin", 
            width = 6, height = 2, bd = 4,
            command = value.sinh).grid(row = 2, column = 5, pady = 1)

btnCosh = Button(calculator, text = "cos", 
            width = 6, height = 2, bd = 4,
            command = value.cosh).grid(row = 2, column = 6, pady = 1)

btnTanh = Button(calculator, text = "tan", 
            width = 6, height = 2, bd = 4,
            command = value.tanh).grid(row = 2, column = 7, pady = 1)





btnLog = Button(calculator, text = "log", 
            width = 6, height = 2, bd = 4,
            command = value.log).grid(row = 3, column = 4, pady = 1)

btnExp = Button(calculator, text = "exp", 
            width = 6, height = 2, bd = 4,
            command = value.exp).grid(row = 3, column = 5, pady = 1)

btnMod = Button(calculator, text = "Mod", 
            width = 6, height = 2, bd = 4,
            command = lambda: value.operations("mod")).grid(row = 3, column = 6, pady = 1)

btnE = Button(calculator, text = "e", 
            width = 6, height = 2, bd = 4,
            command = value.e).grid(row = 3, column = 7, pady = 1)






btnLog10 = Button(calculator, text = "log10", 
                width = 6, height = 2, bd = 4,
                command = value.log10).grid(row = 4, column = 4)

btnLog1p = Button(calculator, text = "log1p", 
                width = 6, height = 2, bd = 4,
                command = value.log1p).grid(row = 4, column = 5)

btnexpm1 = Button(calculator, text = "expm1", 
                width = 6, height = 2, bd = 4,
                command = value.expm1).grid(row = 4, column = 6)

btngamma = Button(calculator, text = "gamma", 
                width = 6, height = 2, bd = 4,
                command = value.lgamma).grid(row = 4, column = 7)






btnLog2 = Button(calculator, text = "log2", 
                width = 6, height = 2, bd = 4,
                command = value.log2).grid(row = 5, column = 4)

btndegree= Button(calculator, text = "deg", 
                width = 6, height = 2, bd = 4,
                command = value.degrees).grid(row = 5, column = 5)

btnasinh = Button(calculator, text = "asinh", 
                width = 6, height = 2, bd = 4,
                command = value.asinh).grid(row = 5, column = 6)

btnacosh = Button(calculator, text = "acosh", 
                width = 6, height = 2, bd = 4,
                command = value.acosh).grid(row = 5, column = 7)

root.mainloop()
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 19:18:05 2022

@author: tonyw
"""

import tkinter as tk
import math

def buttonPresser(button):
    
    if isinstance(button, int) or button ==".":
        calc_entry.insert('end',button)
    elif button == "C":
        var.set(1)
        calc_entry.delete(0, 'end')
        calc_output['text'] = 0
    elif button == "+":
        add_calc()
    elif button == "-":
        sub_calc()
    elif button == "x":
        mult_calc()
    elif button == "/":
        div_calc()
    elif button == "+/-":
        calc_entry.insert(0,'-')
    elif button == "^":
        exp_calc()
    elif button == "Log10":
        log_calc()
    elif button == "Root":
        root_calc()
    elif button == "Pi":
        calc_entry.insert(0,math.pi)
        
def getString():
    string = calc_entry.get()
    newString = ""
    count=0
    for i in string:
        if i =='-' :
            count +=1
            if i == '-' and count > 1:
                continue
            else:
                newString += i
        else:
            newString += i
    return newString


def log_calc():
    var.set(1)
    num = getString()
    calc_output['text'] = num
    calc_entry.delete(0, 'end')
    if isinstance(num, str):
        calc_entry.delete(0, 'end')
        calc_output['text'] = math.log10(float(num))
        
def root_calc():
    var.set(1)
    num = getString()
    calc_output['text'] = num
    calc_entry.delete(0, 'end')
    if isinstance(num, str):
        calc_entry.delete(0, 'end')
        calc_output['text'] = math.sqrt(float(num))

def exp_calc():
    var.set(1)
    num = getString()
    calc_output['text'] = num
    calc_entry.delete(0, 'end')
    num_button.wait_variable(var)
    num2 = getString()
    if isinstance(num2, str):
        calc_entry.delete(0, 'end')
        calc_output['text'] = float(num) ** float(num2)

def mult_calc():
    var.set(1)
    num = getString()
    calc_output['text'] = num
    calc_entry.delete(0, 'end')
    num_button.wait_variable(var)
    num2 = getString()
    if isinstance(num2, str):
        calc_entry.delete(0, 'end')
        calc_output['text'] = float(num) * float(num2)

def div_calc():
    var.set(1)
    num = getString()
    calc_output['text'] = num
    calc_entry.delete(0, 'end')
    num_button.wait_variable(var)
    num2 = getString()
    if isinstance(num2, str):
        calc_entry.delete(0, 'end')
        calc_output['text'] = float(num) / float(num2)
        
def sub_calc():
    var.set(1)
    num = getString()
    calc_output['text'] = num
    calc_entry.delete(0, 'end')
    num_button.wait_variable(var)
    num2 = getString()
    if isinstance(num2, str):
        calc_entry.delete(0, 'end')
        calc_output['text'] = float(num) - float(num2)

def add_calc():
    var.set(1)
    num = getString()
    calc_output['text'] = num
    calc_entry.delete(0, 'end')
    num_button.wait_variable(var)
    num2 = getString()
    if isinstance(num2, str):
        calc_entry.delete(0, 'end')
        calc_output['text'] = float(num) + float(num2)



calculator = tk.Tk()

calculator.title("Calculator")
calculator.geometry("200x200")

calculator.resizable(width=True, height=True)
calc_entry = tk.Entry()
calc_output = tk.Label(text='0')
calc_output.grid(row=0,column=3, sticky='e')
calc_entry.grid(row=0,column=0,columnspan=3,sticky='w',pady=5)

buttonDict = {7:{"row":1,"column":0},8:{"row":1,"column":1},
              9:{"row":1,"column":2},"C":{"row":1,"column":3},
              4:{"row":2,"column":0},5:{"row":2,"column":1},
              6:{"row":2,"column":2},"+":{"row":2,"column":3}, 
              1:{"row":3,"column":0},2:{"row":3,"column":1},
              3:{"row":3,"column":2},"-":{"row":3,"column":3},
              "/":{"row":4,"column":0},0:{"row":4,"column":1},
              ".":{"row":4,"column":2},"x":{"row":4,"column":3},
         "^":{"row":5,"column":0}, "+/-":{"row":5,"column":1}, 
         "Pi":{"row":5,"column":2,},"=":{"row":5,"column":3},
         "Root":{"row":"6","column":"0"}, "Log10":{"row":"6","column":"1"}}


var = tk.IntVar()


for k,v in buttonDict.items():
        if k == "=":
            num_button = tk.Button(master=calculator, text=k, command=lambda: var.set(1))
            num_button.grid(row=buttonDict[k]["row"], column=buttonDict[k]["column"],padx=0, pady=0,sticky="nsew")
        else:
            num_button = tk.Button(master=calculator, text=k, command=lambda k=k:buttonPresser(k))
            num_button.grid(row=buttonDict[k]["row"], column=buttonDict[k]["column"],padx=0, pady=0,sticky="nsew")
        
for i in range(0,6):

    calculator.rowconfigure(i+1,weight = 1)
    if i < 4:
        calculator.columnconfigure(i,weight =1)
        
userinput = calc_entry.get()



calculator.mainloop()




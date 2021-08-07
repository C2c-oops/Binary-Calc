# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 23:38:47 2018

@author: Sahil Singh c2c
"""

from tkinter import *
from tkinter import messagebox
import time
root = Tk()
root.geometry("1600x800+0+0")
root.title("Base Converter")
root.configure(background='Cadet Blue')
#==========================TOP(Number System Conversion)=======================
Tops = Frame(root, bg='Cadet Blue', bd=20, pady=5, relief=SUNKEN)
Tops.pack(side=TOP)
lable_Title = Label(Tops,font=('arial',50,'bold'), text="NUMBER SYSTEM CONVERSION", bd=21, bg='Cadet Blue', fg='Cornsilk', justify=CENTER)
lable_Title.grid(row=0, column=0)
#==========================Frames_R============================================
Mainframe_R = Frame(root, bg='Powder Blue', bd=10, relief=RIDGE)
Mainframe_R.pack(side=RIGHT)
Cal_R=Frame(Mainframe_R, bg='Powder Blue', bd=6, relief=RIDGE)
Cal_R.pack(side=TOP)
Buttons_R = Frame(Mainframe_R, bg='Powder Blue', bd=3, relief=RIDGE)
Buttons_R.pack(side=BOTTOM)
Log_R=Frame(Mainframe_R, bg='Powder Blue', bd=4, relief=RIDGE)
Log_R.pack(side=BOTTOM)
#==========================Frames_L============================================
MainFrame_L = Frame(root, bg='Cadet Blue', bd=10, relief=RIDGE)
MainFrame_L.pack(side=LEFT)
#=========================Entry================================================
value_Entry = Frame(MainFrame_L, bg='powder blue', bd=20, relief=GROOVE)
value_Entry.pack(side=TOP)
label_1 = Label(value_Entry, font=('arial',15,'bold'), text="Enter value:")
label_1.grid(row=0)
entry = Entry(value_Entry, font=('arial',16,'bold'), bd=8, width=6, justify=LEFT)
entry.grid(row=0, column=1)
#========================Conversion_F==========================================
CON_F = Frame(MainFrame_L, bg='Cadet Blue', bd=3, relief=RIDGE)
CON_F.pack(side=TOP)
CBF = Frame(CON_F, bg='Powder Blue', bd=10, relief=GROOVE)
CBF.pack(side=LEFT)
label_2 = Label(CBF, font=('arial',20,'bold'), text="Convert BASE From:")
label_2.grid(row=0, column=0)
CBT = Frame(CON_F, bg='Powder Blue', bd=10, relief=GROOVE)
CBT.pack(side=RIGHT)
label_3 = Label(CBT, font=('arial',20,'bold'), text="Convert BASE To:")
label_3.grid(row=0, column=0)
#========================Result================================================
Result_Entry = Frame(MainFrame_L, bg='powder blue', bd=20, relief=GROOVE)
Result_Entry.pack(side=BOTTOM)
label_4 = Label(Result_Entry, font=('arial',15,'bold'), text="Result:")
label_4.grid(row=0)
#=======================Buttons_F================================================
Buttons_L = Frame(MainFrame_L, bg='Powder Blue', bd=3, relief=RIDGE)
Buttons_L.pack(side=BOTTOM)
Convert_F = Frame(Buttons_L, bg='Powder Blue', bd=3, relief=RIDGE)
Convert_F.pack(side=LEFT)
Explain_F = Frame(Buttons_L, bg='Powder Blue', bd=3, relief=RIDGE)
Explain_F.pack(side=RIGHT) 
#========================Var========================
var_a1=IntVar()
var_a2=IntVar()
var_a3=IntVar()
var_a4=IntVar()
var_b1=IntVar()
var_b2=IntVar()
var_b3=IntVar()
var_b4=IntVar()
text_Input=StringVar()
Log_ref=StringVar()
Date1=StringVar()
Time1=StringVar()
label_space=StringVar()
operator=""
#=======================Date&Time============================
Date1.set(time.strftime("%d/%m/%y"))
Time1.set(time.strftime("%H:%M:%S"))
#=======================Def=========================================
def iExit():
    iExit = messagebox.askyesno("Exit Calculator", "Confirm if You Want To Exit")
    if iExit > 0:
        root.destroy()
        return
def btnReset():
    var_a1.set(0)
    var_a2.set(0)
    var_a3.set(0)
    var_a4.set(0)
    var_b1.set(0)
    var_b2.set(0)
    var_b3.set(0)
    var_b4.set(0)
    text_Input.set(0)
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)
    
def btnClear():
    global operator
    operator = ""
    text_Input.set("")
    
def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""        
    
def bin_to_bin(b):
    return (bin(int(str(b), 2)))

def bin_to_dec(b):
    return int(str(b), 2)

def bin_to_oct(b):
    return oct(int(str(b), 2))

def bin_to_hex(b):
    return hex(int(str(b), 2))

def dec_to_bin(d):
    return bin(int(d))

def dec_to_dec(d):
    return int(d)

def dec_to_oct(d):
    return oct(int(d))

def dec_to_hex(d):
    return hex(int(d))

def oct_to_bin(o):
    return bin(int(str(o), 8))

def oct_to_dec(o):
    return int(str(o), 8)

def oct_to_oct(o):
    return oct(int(str(o), 8))

def oct_to_hex(o):
    return hex(int(str(o), 8))


def hex_to_bin(h):
    return bin(int(str(h), 16))

def hex_to_dec(h):
    return int(str(h), 16)

def hex_to_oct(h):
    return oct(int(str(h), 16))

def hex_to_hex(h):
    return hex(int(str(h), 16))
    
def explain():
    if var_a1.get() == 1 and var_b1.get() ==1:
        messagebox.showinfo("Explaination","You know the answer already..!! No need to convert")
    elif var_a1.get() == 1 and var_b2.get() == 1:
        messagebox.showinfo("Explaination","The right most digit in the binary number is multiplied by 2 to the power of 0 ( which is 1 ). The next digit is multiplied by 2 to the power of 1 ( which is 2 ) and so on.")
    elif var_a1.get() == 1 and var_b3.get() == 1:
        messagebox.showinfo("Explaination","Octal. The octal numeral system, or oct for short, is the base-8 number system, and uses the digits 0 to 7. Octal numerals can be made from binary numerals by grouping consecutive binary digits into groups of three (starting from the right). For example, the binary representation for decimal 74 is 1001010.")
    elif var_a1.get() == 1 and var_b4.get() == 1:
        messagebox.showinfo("Explaination","Binary: 11100101 = 1110 0101, Binary = 1110 0101, Hexadecimal = E 5 = E5 hex")
    elif var_a2.get() == 1 and var_b1.get() == 1:
        messagebox.showinfo("Explaination","converting decimal to binary number equivalents is to write down the decimal number and to continually divide-by-2 (two) to give a result and a remainder of either a “1” or a “0” until the final result equals zero.")
    elif var_a2.get() == 1 and var_b2.get() == 1:
        messagebox.showinfo("Explaination","You know the answer already..!! No need to convert")
    elif var_a2.get() == 1 and var_b3.get() == 1:
        messagebox.showinfo("Explaination","taking a number like 100 base ten, you’d have:- 100/8=12 remainder, 12/8=1 remainder 4, 1/8=0 remainder 1. So the equivalent of 100 in base 8 would be 144. Each octal digit represents increasing powers of 8. So 144 is saying 1*8^2 (8 squared), plus 4 time 8, plus 4.")
    elif var_a2.get() == 1 and var_b4.get() == 1:
        messagebox.showinfo("Explaination","1.Divide the decimal number by 16,Treat the division as an integer division. 2.Write down the remainder (in hexadecimal). 3.Divide the result again by 16,Treat the division as an integer division. 4.Repeat step 2 and 3 until result is 0. 5.The hex value is the digit sequence of the remainders from the last to first.")
    elif var_a3.get() == 1 and var_b1.get() == 1:
        messagebox.showinfo("Explaination","The octal numeral system, or oct for short, is the base-8 number system, and uses the digits 0 to 7. Octal numerals can be made from binary numerals by grouping consecutive binary digits into groups of three (starting from the right). For example, the binary representation for decimal 74 is 1001010.")
    elif var_a3.get() == 1 and var_b2.get() == 1:
        messagebox.showinfo("Explaination","For converting octal number into decimal number we have to start multiplying the digits of the number from right hand side with increasing powers of 8 staring from 0 and finally summing up all the products.")
    elif var_a3.get() == 1 and var_b3.get() == 1:
        messagebox.showinfo("Explaination","You know the answer already..!! No need to convert")
    elif var_a3.get() == 1 and var_b4.get() == 1:
        messagebox.showinfo("Explaination","When converting from octal to hexadecimal, it is often easier to first convert the octal number into binary and then from binary into hexadecimal.")
    elif var_a4.get() == 1 and var_b1.get() == 1:
        messagebox.showinfo("Explaination","Each of the 16 hexadecimal digits are equal to 4 binary digits, so all you need to do is memorize the 16 conversions. For example, the hexadecimal 1 is equal to the binary 0001.")
    elif var_a4.get() == 1 and var_b2.get() == 1:
        messagebox.showinfo("Explaination","3B in base 16 is equal to each digit multiplied with its corresponding 16n:- 3B16 = 3×16^1+11×16^0 = 48+11 = 59^10")
    elif var_a4.get() == 1 and var_b3.get() == 1:
        messagebox.showinfo("Explaination","step 1: Separate the digits of the given hex number, if it contains more than 1 digit. step 2: Find the equivalent binary number for each digit of octal number. Add 0's to the left if any of the binary equivalent is shorter than 4 bits. step 3: Write the all groups binary numbers together, maintaining the same group. step 4: Separate the binary digits into groups, each containing 3 bits or digits from right to left. Add 0s to the left, if the last group contains less than 3 bits. step 5: Find the octal equivalent for each group. step 6: Write all octal equivalent of each digit together where keeping the same order provides the octal equivalent for the given hexadecimal.")
    elif var_a4.get() == 1 and var_b4.get() == 1:
        messagebox.showinfo("Explaination","You know the answer already..!! No need to convert")
    
def convert():
    label_space = Label(Result_Entry, text="                                         ")
    if entry.get() == "":
        messagebox.showinfo("EMPTY", "Please enter value.")
    elif var_a1.get() == 1 and var_b1.get() == 1:
        try:
            label_answer = Label(Result_Entry, font=('arial',16,'bold'), text=bin_to_bin(entry.get())[2:])
            label_space.grid(row=0, column=1, columnspan=2)
            label_answer.grid(row=0, column=1, columnspan=2)
        except:
            messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly '0' and '1' are accepted.")
    elif var_a1.get() == 1 and var_b2.get() == 1:
        try:
            label_answer = Label(Result_Entry, font=('arial',16,'bold'), text=bin_to_dec(entry.get()))
            label_space.grid(row=0, column=1, columnspan=2)
            label_answer.grid(row=0, column=1, columnspan=2)
        except:
            messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly '0' and '1' are accepted.")
    elif var_a1.get() == 1 and var_b3.get() == 1:
        try:
            label_answer = Label(Result_Entry, font=('arial',16,'bold'), text=bin_to_oct(entry.get())[2:])
            label_space.grid(row=0, column=1, columnspan=2)
            label_answer.grid(row=0, column=1, columnspan=2)
        except:
            messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly '0' and '1' are accepted.")
    elif var_a1.get() == 1 and var_b4.get() == 1:
        try:
            label_answer = Label(Result_Entry, font=('arial',16,'bold'), text=bin_to_hex(entry.get()).upper()[2:])
            label_space.grid(row=0, column=1, columnspan=2)
            label_answer.grid(row=0, column=1, columnspan=2)
        except:
            messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly '0' and '1' are accepted.")
    elif var_a2.get() == 1 and var_b1.get() == 1:
        try:
            label_answer = Label(Result_Entry, font=('arial',16,'bold'), text=dec_to_bin(entry.get())[2:])
            label_space.grid(row=0, column=1, columnspan=2)
            label_answer.grid(row=0, column=1, columnspan=2)
        except:
            messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly numbers are accepted.")
    elif var_a2.get() == 1 and var_b2.get() == 1:
        try:
            label_answer = Label(Result_Entry, font=('arial',16,'bold'), text=dec_to_dec(entry.get()))
            label_space.grid(row=0, column=1, columnspan=2)
            label_answer.grid(row=0, column=1, columnspan=2)
        except:
            messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly numbers are accepted.")
    elif var_a2.get() == 1 and var_b3.get() == 1:
        try:
            label_answer = Label(Result_Entry, font=('arial',16,'bold'), text=dec_to_oct(entry.get())[2:])
            label_space.grid(row=0, column=1, columnspan=2)
            label_answer.grid(row=0, column=1, columnspan=2)
        except:
            messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly numbers are accepted")
    elif var_a2.get() == 1 and var_b4.get() == 1:
        try:
            label_answer = Label(Result_Entry, font=('arial',16,'bold'), text=dec_to_hex(entry.get()).upper()[2:])
            label_space.grid(row=0, column=1, columnspan=2)
            label_answer.grid(row=0, column=1, columnspan=2)
        except:
            messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly numbers are accepted.")
    elif var_a3.get() == 1 and var_b1.get() == 1:
        try:
            label_answer = Label(Result_Entry, font=('arial',16,'bold'), text=oct_to_bin(entry.get())[2:])
            label_space.grid(row=0, column=1, columnspan=2)
            label_answer.grid(row=0, column=1, columnspan=2)
        except:
            messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly 0 to 7 numbers are accepted.")
    elif var_a3.get() == 1 and var_b2.get() == 1:
        try:
            label_answer = Label(Result_Entry, font=('arial',16,'bold'), text=oct_to_dec(entry.get()))
            label_space.grid(row=0, column=1, columnspan=2)
            label_answer.grid(row=0, column=1, columnspan=2)
        except:
            messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly 0 to 7 numbers are accepted.")
    elif var_a3.get() == 1 and var_b3.get() == 1:
        try:
            label_answer = Label(Result_Entry, font=('arial',16,'bold'), text=oct_to_oct(entry.get()))
            label_space.grid(row=0, column=1, columnspan=2)
            label_answer.grid(row=0, column=1, columnspan=2)
        except:
            messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly 0 to 7 numbers are accepted.")
    elif var_a3.get() == 1 and var_b4.get() == 1:
        try:
            label_answer = Label(Result_Entry, font=('arial',16,'bold'), text=oct_to_hex(entry.get()).upper()[2:])
            label_space.grid(row=0, column=1, columnspan=2)
            label_answer.grid(row=0, column=1, columnspan=2)
        except:
            messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly 0 to 7 numbers are accepted.")
    elif var_a4.get() == 1 and var_b1.get() == 1:
        try:
            label_answer = Label(Result_Entry, font=('arial',16,'bold'), text=hex_to_bin(entry.get())[2:])
            label_space.grid(row=0, column=1, columnspan=2)
            label_answer.grid(row=0, column=1, columnspan=2)
        except:
            messagebox.showinfo("ERROR INPUT",
                                "You have entered invalid input.\nOnly 0 to 9 and 'A' to 'F' are accepted.")
    elif var_a4.get() == 1 and var_b2.get() == 1:
        try:
            label_answer = Label(Result_Entry, font=('arial',16,'bold'), text=hex_to_dec(entry.get()))
            label_space.grid(row=0, column=1, columnspan=2)
            label_answer.grid(row=0, column=1, columnspan=2)
        except:
            messagebox.showinfo("ERROR INPUT",
                                "You have entered invalid input.\nOnly 0 to 9 and 'A' to 'F' are accepted.")
    elif var_a4.get() == 1 and var_b3.get() == 1:
        try:
            label_answer = Label(Result_Entry, font=('arial',16,'bold'), text=hex_to_oct(entry.get())[2:])
            label_space.grid(row=0, column=1, columnspan=2)
            label_answer.grid(row=0, column=1, columnspan=2)
        except:
            messagebox.showinfo("ERROR INPUT",
                                "You have entered invalid input.\nOnly 0 to 9 and 'A' to 'F' are accepted.")
    elif var_a4.get() == 1 and var_b4.get() == 1:
        try:
            label_answer = Label(Result_Entry, font=('arial',16,'bold'), text=hex_to_hex(entry.get()).upper())
            label_space.grid(row=0, column=1, columnspan=2)
            label_answer.grid(row=0, column=1, columnspan=2)
        except:
            messagebox.showinfo("ERROR INPUT",
                                "You have entered invalid input.\nOnly 0 to 9 and 'A' to 'F' are accepted.")
    else:
        messagebox.showinfo("REQUIREMENT", "Choose options on the both side")
        
def Log():
    txtLog.delete("1.0",END)
    txtLog.insert(END,'----------------------------------------------------------------------------------'+"\n")
    txtLog.insert(END,'======>LOVELY PROFESSIONAL UNIVERSITY<====='+"\n")
    txtLog.insert(END,'                                 Python Project On'+"\n")
    txtLog.insert(END,'                          Number System Conversion'+"\n")
    txtLog.insert(END,'----------------------------------------------------------------------------------'+"\n")
    txtLog.insert(END,Date1.get()+"\t\t\t\t"+Time1.get()+"\n")
    txtLog.insert(END,'Submitted to- Isha Mam'+"\n")
    txtLog.insert(END,'\t\t Name \t\t Reg No.'+"\n")
    txtLog.insert(END,'Submitted By- Avinash Singh'+"\t\t\t\t11710000"+"\n")
    txtLog.insert(END,'\t          Alok Pandey'+"\t\t\t11710000"+"\n")
    txtLog.insert(END,'\t          Sahil Singh'+"\t\t\t11710000"+"\n")    

def chka1():
    if (var_a1.get() == 1):
        c_a2.configure(state = DISABLED)
        c_a2.focus()
        c_a3.configure(state = DISABLED)
        c_a3.focus()
        c_a4.configure(state = DISABLED)
        c_a4.focus()
    elif(var_a1.get() == 0):
        c_a2.configure(state = NORMAL)
        c_a2.focus()
        c_a3.configure(state = NORMAL)
        c_a3.focus()
        c_a4.configure(state = NORMAL)
        c_a4.focus()
def chka2():
    if (var_a2.get() == 1):
        c_a1.configure(state = DISABLED)
        c_a1.focus()
        c_a3.configure(state = DISABLED)
        c_a3.focus()
        c_a4.configure(state = DISABLED)
        c_a4.focus()
    elif(var_a2.get() == 0):
        c_a1.configure(state = NORMAL)
        c_a1.focus()
        c_a3.configure(state = NORMAL)
        c_a3.focus()
        c_a4.configure(state = NORMAL)
        c_a4.focus()
def chka3():
    if (var_a3.get() == 1):
        c_a1.configure(state = DISABLED)
        c_a1.focus()
        c_a2.configure(state = DISABLED)
        c_a2.focus()
        c_a4.configure(state = DISABLED)
        c_a4.focus()
    elif(var_a3.get() == 0):
        c_a1.configure(state = NORMAL)
        c_a1.focus()
        c_a2.configure(state = NORMAL)
        c_a2.focus()
        c_a4.configure(state = NORMAL)
        c_a4.focus()
def chka4():
    if (var_a4.get() == 1):
        c_a1.configure(state = DISABLED)
        c_a1.focus()
        c_a2.configure(state = DISABLED)
        c_a2.focus()
        c_a3.configure(state = DISABLED)
        c_a3.focus()
    elif(var_a4.get() == 0):
        c_a1.configure(state = NORMAL)
        c_a1.focus()
        c_a2.configure(state = NORMAL)
        c_a2.focus()
        c_a3.configure(state = NORMAL)
        c_a3.focus()
def chkb1():
    if (var_b1.get() == 1):
        c_b2.configure(state = DISABLED)
        c_b2.focus()
        c_b3.configure(state = DISABLED)
        c_b3.focus()
        c_b4.configure(state = DISABLED)
        c_b4.focus()
    elif(var_b1.get() == 0):
        c_b2.configure(state = NORMAL)
        c_b2.focus()
        c_b3.configure(state = NORMAL)
        c_b3.focus()
        c_b4.configure(state = NORMAL)
        c_b4.focus()
def chkb2():
    if (var_b2.get() == 1):
        c_b1.configure(state = DISABLED)
        c_b1.focus()
        c_b3.configure(state = DISABLED)
        c_b3.focus()
        c_b4.configure(state = DISABLED)
        c_b4.focus()
    elif(var_b2.get() == 0):
        c_b1.configure(state = NORMAL)
        c_b1.focus()
        c_b3.configure(state = NORMAL)
        c_b3.focus()
        c_b4.configure(state = NORMAL)
        c_b4.focus()
def chkb3():
    if (var_b3.get() == 1):
        c_b1.configure(state = DISABLED)
        c_b1.focus()
        c_b2.configure(state = DISABLED)
        c_b2.focus()
        c_b4.configure(state = DISABLED)
        c_b4.focus()
    elif(var_b3.get() == 0):
        c_b1.configure(state = NORMAL)
        c_b1.focus()
        c_b2.configure(state = NORMAL)
        c_b2.focus()
        c_b4.configure(state = NORMAL)
        c_b4.focus()
def chkb4():
    if (var_b4.get() == 1):
        c_b1.configure(state = DISABLED)
        c_b1.focus()
        c_b2.configure(state = DISABLED)
        c_b2.focus()
        c_b3.configure(state = DISABLED)
        c_b3.focus()
    elif(var_b4.get() == 0):
        c_b1.configure(state = NORMAL)
        c_b1.focus()
        c_b2.configure(state = NORMAL)
        c_b2.focus()
        c_b3.configure(state = NORMAL)
        c_b3.focus()

c_a1 = Checkbutton(CBF, font=('arial',15,'bold'), text="Binary", variable=var_a1, onvalue=1, offvalue=0, bg='powder blue', command = chka1)
c_a1.grid(row=3, column=0, sticky=W)
c_a2 = Checkbutton(CBF, font=('arial',15,'bold'), text="Decimal", variable=var_a2, onvalue=1, offvalue=0, bg='powder blue', command = chka2)
c_a2.grid(row=4, column=0, sticky=W)
c_a3 = Checkbutton(CBF, font=('arial',15,'bold'), text="Octal", variable=var_a3, onvalue=1, offvalue=0, bg='powder blue', command = chka3)
c_a3.grid(row=5, column=0, sticky=W)
c_a4 = Checkbutton(CBF, font=('arial',15,'bold'), text="Hexa Decimal", variable=var_a4, onvalue=1, offvalue=0, bg='powder blue', command = chka4)
c_a4.grid(row=6, column=0, sticky=W)
c_b1 = Checkbutton(CBT, font=('arial',15,'bold'), text="Binary", variable=var_b1, onvalue=1, offvalue=0, bg='powder blue', command = chkb1)
c_b1.grid(row=3, column=0, sticky=W)
c_b2 = Checkbutton(CBT, font=('arial',15,'bold'), text="Decimal", variable=var_b2, onvalue=1, offvalue=0, bg='powder blue', command = chkb2)
c_b2.grid(row=4, column=0, sticky=W)
c_b3 = Checkbutton(CBT, font=('arial',15,'bold'), text="Octal", variable=var_b3, onvalue=1, offvalue=0, bg='powder blue', command = chka3)
c_b3.grid(row=5, column=0, sticky=W)
c_b4 = Checkbutton(CBT, font=('arial',15,'bold'), text="Hexa Decimal", variable=var_b4, onvalue=1, offvalue=0, bg='powder blue', command = chka4)
c_b4.grid(row=6, column=0, sticky=W)
#==============================Log=============================================
txtLog = Text(Log_R, width=46,height=12, bg="white", bd=4, font=('arial',12,'bold'))
txtLog.grid(row=0, column=0)
#==============================Buttons=========================================
btn_convert = Button(Convert_F, padx=16, pady=1, bd=7, fg="black", bg="powder blue", font=('arial',16,'bold'), width=10, text="CONVERT", command=convert)
btn_convert.grid(row=0,sticky=W)
btn_explan = Button(Explain_F, padx=16, pady=1, bd=7, fg="black", bg="powder blue", font=('arial',16,'bold'), width=10, text="EXPLANATION", command=explain)
btn_explan.grid(row=0,sticky=W)
btn_Reset = Button(Buttons_R, padx=16, pady=1, bd=7, fg="black", bg="powder blue", font=('arial',16,'bold'), width=10, text="RESET", command=btnReset)
btn_Reset.grid(row=0, column=0)
btn_Log = Button(Buttons_R, padx=16, pady=1, bd=7, fg="black", bg="powder blue", font=('arial',16,'bold'), width=10, text="INFO", command=Log)
btn_Log.grid(row=0, column=1)
btn_Quit = Button(Buttons_R, padx=16, pady=1, bd=7, fg="black", bg="powder blue", font=('arial',16,'bold'), width=10, text="QUIT", command=iExit)
btn_Quit.grid(row=0, column=2)
#==============================Calculator======================================    
txtDisplay = Entry(Cal_R, width=45, bg="white", bd=4, font=('arial',12,'bold'), justify=RIGHT, textvariable = text_Input)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")
#==============================Buttons=========================================
btn7 = Button(Cal_R, padx=16, pady=1, bd=7, fg="black", font=('arial',16,'bold'), width=5, text="7", command=lambda:btnClick(7))
btn7.grid(row=2, column=0)
btn8 = Button(Cal_R, padx=16, pady=1, bd=7, fg="black", font=('arial',16,'bold'), width=5, text="8", command=lambda:btnClick(8))
btn8.grid(row=2, column=1)
btn9 = Button(Cal_R, padx=16, pady=1, bd=7, fg="black", font=('arial',16,'bold'), width=5, text="9", command=lambda:btnClick(9))
btn9.grid(row=2, column=2)
btnAdd = Button(Cal_R, padx=16, pady=1, bd=7, fg="black", bg="powder blue", font=('arial',16,'bold'), width=5, text="+", command=lambda:btnClick("+"))
btnAdd.grid(row=2, column=3)
#==============================Buttons=========================================
btn4 = Button(Cal_R, padx=16, pady=1, bd=7, fg="black", font=('arial',16,'bold'), width=5, text="4", command=lambda:btnClick(4))
btn4.grid(row=3, column=0)
btn5 = Button(Cal_R, padx=16, pady=1, bd=7, fg="black", font=('arial',16,'bold'), width=5, text="5", command=lambda:btnClick(5))
btn5.grid(row=3, column=1)
btn6 = Button(Cal_R, padx=16, pady=1, bd=7, fg="black", font=('arial',16,'bold'), width=5, text="6", command=lambda:btnClick(6))
btn6.grid(row=3, column=2)
btnSub = Button(Cal_R, padx=16, pady=1, bd=7, fg="black", bg="powder blue", font=('arial',16,'bold'), width=5, text="-", command=lambda:btnClick("-"))
btnSub.grid(row=3, column=3)
#==============================Buttons=========================================
btn1 = Button(Cal_R, padx=16, pady=1, bd=7, fg="black", font=('arial',16,'bold'), width=5, text="1", command=lambda:btnClick(1))
btn1.grid(row=4, column=0)
btn2 = Button(Cal_R, padx=16, pady=1, bd=7, fg="black", font=('arial',16,'bold'), width=5, text="2", command=lambda:btnClick(2))
btn2.grid(row=4, column=1)
btn3 = Button(Cal_R, padx=16, pady=1, bd=7, fg="black", font=('arial',16,'bold'), width=5, text="3", command=lambda:btnClick(3))
btn3.grid(row=4, column=2)
btnMulti = Button(Cal_R, padx=16, pady=1, bd=7, fg="black", bg="powder blue", font=('arial',16,'bold'), width=5, text="*", command=lambda:btnClick("*"))
btnMulti.grid(row=4, column=3)
#==============================Buttons=========================================
btnclears = Button(Cal_R, padx=16, pady=1, bd=7, fg="red", bg="powder blue", font=('arial',16,'bold'), width=5, text="C", command=btnClear)
btnclears.grid(row=5, column=0)
btn0 = Button(Cal_R, padx=16, pady=1, bd=7, fg="black", bg="powder blue", font=('arial',16,'bold'), width=5, text="0", command=lambda:btnClick("0"))
btn0.grid(row=5, column=1)
btnEqual = Button(Cal_R, padx=16, pady=1, bd=7, fg="black", bg="powder blue", font=('arial',16,'bold'), width=5, text="=", command=btnEquals)
btnEqual.grid(row=5, column=2)
btnDiv = Button(Cal_R, padx=16, pady=1, bd=7, fg="black", bg="powder blue", font=('arial',16,'bold'), width=5, text="/", command=lambda:btnClick("/"))
btnDiv.grid(row=5, column=3)
root.mainloop()

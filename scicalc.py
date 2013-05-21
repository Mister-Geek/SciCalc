#!usr/bin/env python3
import sys
import os
from math import *
import cmath

#Banner
def banner():
    print('''
    ====================================
    Scientific CLI_Calculator by Mr.Geek
    ====================================
    ''')

#Set clear
def clear():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')
    else:
        sys.exit("This script is not for apple guys , Exiting ...")

#Usage
_help = '''
    Usage :
    Basic Calculation :
           format >>> 2 + 3
                  >>> 5.0
           use spaces in between numbers and operators.
    Functions :
           format >>> sqrt(-10)
                  >>> 3.1622776601683795j
    Converter : binary to decimal , octal to decimal , hex to decimal
           format >>> 101 -b
                  >>> 5
           replace with '-o' '-h'
    Type >>> list
           to see all available functions.
    Type >>> c
           to clear.
    Type >>> exit
           to exit.
    Type >>> help
           to get help.
    If you type out of range , only typed string will return.
         >>> Mr.Geek
         Mr.Geek
'''
_list = '''
List of all available functions
===============================
Basic Calc:
-----------
x + y
x - y
x / y
x * y
x // y
sin(x) +-/* cos(y)/tan/cot/sec/cosec
cos(x) +-/* sin(y)/tan/cot/sec/cosec
tan(x) +-/* sin(y)/cos/cot/sec/cosec

Functions
---------
sin(x)
cos(x)
tan(x)
cot(x)
sec(x)
cosec(x)
pow(x,y)      --print [2(power)3 = 8]
abs(x)        --print absolute value
sqrt(x)       --print square root
ceil(x)       --round to least digit --e.g. >>> ceil(9.3) -> 10
floor(x)      --round to most digit --e.g. >>> floor(9.7) -> 9
exp(x)        --print exponential value
deg(x)        --convert radian to degree
pi            --print pi value
e             --print e value

Converters
==========
-b            --convert binary to decimal
-o            --convert octal to decimal
-h            --convert hex to decimal (Not Fully working now)
'''

#Main Calculating func
def console():
    run = 1
    while run:
        con = input (">>> ").split()
        try:
            if len(con) == 1:
                if con[0] == 'c':
                    clear()
                elif con[0] == 'help':
                    print(_help)
                elif con[0] == 'list':
                    print(_list)
                elif con[0] == 'exit':
                    print('[x] Exiting... bye !!!')
                    run = False
                else:
                    bas_func(con[0])
            
            elif len(con) == 3:
                bas_calc(con[0],con[1],con[2])
            elif len(con) == 2 and con[1] == '-b':
                bin_dec(con[0])
            elif len(con) == 2 and con[1] == '-o':
                oct_dec(con[0])
            elif len(con) == 2 and con[1] == '-h':
                hex_dec(con[0])
            else:
                print("Syntax Error : Please type >>> help to see help documentation")
             
        except KeyboardInterrupt:
            sys.exit(0)                     
            
#Series of calculator funcs
#Basic calc+trigo            
def bas_calc(c1,c2,c3):
    if c1.startswith('sin(') and c3.startswith('cos('):
        x = c1[4:-1]
        y = c3[4:-1]
        if c2 == '+':
            print(sin(float(x))+cos(float(x)))
        elif c2 == '-':
            print(sin(float(x))-cos(float(x)))
        elif c2 == '/':
            print(sin(float(x))/cos(float(x)))
        elif c2 == '*':
            print(sin(float(x))*cos(float(x)))
        else:
             print("Syntax Error : please type help to see help documentation")
    elif c1.startswith('sin(') and c3.startswith('tan('):
        x = c1[4:-1]
        y = c3[4:-1]
        if c2 == '+':
            print(sin(float(x))+tan(float(x)))
        elif c2=='-':
            print(sin(float(x))-tan(float(x)))
        elif c2=='/':
            print(sin(float(x))/tan(float(x)))
        elif c2=='*':
            print(sin(float(x))*tan(float(x)))
        else:
             print("Syntax Error : please type help to see help documentation")     
    elif c1.startswith('sin(') and c3.startswith('cot('):
        x = c1[4:-1]
        y = c3[4:-1]
        if c2 == '+':
            print(sin(float(x))+(1/tan(float(x))))
        elif c2=='-':
            print(sin(float(x))-(1/tan(float(x))))
        elif c2=='/':
            print(sin(float(x))/(1/tan(float(x))))
        elif c2=='*':
            print(sin(float(x))*(1/tan(float(x))))
        else:
             print("Syntax Error : please type help to see help documentation")
    elif c1.startswith('sin(') and c3.startswith('sec('):
        x = c1[4:-1]
        y = c3[4:-1]
        if c2 == '+':
            print(sin(float(x))+(1/cos(float(x))))
        elif c2=='-':
            print(sin(float(x))-(1/cos(float(x))))
        elif c2=='/':
            print(sin(float(x))/(1/cos(float(x))))
        elif c2=='*':
            print(sin(float(x))*(1/cos(float(x))))
        else:
             print("Syntax Error : please type help to see help documentation")
    elif c1.startswith('sin(') and c3.startswith('cosec('):
        x = c1[4:-1]
        y = c3[6:-1]
        if c2 == '+':
            print(sin(float(x))+(1/sin(float(x))))
        elif c2=='-':
            print(sin(float(x))-(1/sin(float(x))))
        elif c2=='/':
            print(sin(float(x))/(1/sin(float(x))))
        elif c2=='*':
            print(sin(float(x))*(1/sin(float(x))))
        else:
             print("Syntax Error : please type help to see help documentation")
    elif c1.startswith('cos(') and c3.startswith('sin('):
        x = c1[4:-1]
        y = c3[4:-1]
        if c2 == '+':
            print(cos(float(x))+sin(float(x)))
        elif c2=='-':
            print(cos(float(x))-sin(float(x)))
        elif c2=='/':
            print(cos(float(x))/sin(float(x)))
        elif c2=='*':
            print(cos(float(x))*sin(float(x)))
        else:
             print("Syntax Error : please type help to see help documentation")
    elif c1.startswith('cos(') and c3.startswith('tan('):
        x = c1[4:-1]
        y = c3[4:-1]
        if c2 == '+':
            print(cos(float(x))+tan(float(x)))
        elif c2=='-':
            print(cos(float(x))-tan(float(x)))
        elif c2=='/':
            print(cos(float(x))/tan(float(x)))
        elif c2=='*':
            print(cos(float(x))*tan(float(x)))
        else:
             print("Syntax Error : please type help to see help documentation")
    elif c1.startswith('cos(') and c3.startswith('cot('):
        x = c1[4:-1]
        y = c3[4:-1]
        if c2 == '+':
            print(cos(float(x))+(1/tan(float(x))))
        elif c2=='-':
            print(cos(float(x))-(1/tan(float(x))))
        elif c2=='/':
            print(cos(float(x))/(1/tan(float(x))))
        elif c2=='*':
            print(cos(float(x))*(1/tan(float(x))))
        else:
             print("Syntax Error : please type help to see help documentation")
    elif c1.startswith('cos(') and c3.startswith('sec('):
        x = c1[4:-1]
        y = c3[4:-1]
        if c2 == '+':
            print(cos(float(x))+(1/cos(float(x))))
        elif c2=='-':
            print(cos(float(x))-(1/cos(float(x))))
        elif c2=='/':
            print(cos(float(x))/(1/cos(float(x))))
        elif c2=='*':
            print(cos(float(x))*(1/cos(float(x))))
        else:
             print("Syntax Error : please type help to see help documentation")
    elif c1.startswith('cos(') and c3.startswith('cosec('):
        x = c1[4:-1]
        y = c3[6:-1]
        if c2 == '+':
            print(cos(float(x))+(1/sin(float(x))))
        elif c2=='-':
            print(cos(float(x))-(1/sin(float(x))))
        elif c2=='/':
            print(cos(float(x))/(1/sin(float(x))))
        elif c2=='*':
            print(cos(float(x))*(1/sin(float(x))))
        else:
             print("Syntax Error : please type help to see help documentation")
    elif c1.startswith('tan(') and c3.startswith('sin('):
        x = c1[4:-1]
        y = c3[4:-1]
        if c2 == '+':
            print(tan(float(x))+sin(float(x)))
        elif c2=='-':
            print(tan(float(x))-sin(float(x)))
        elif c2=='/':
            print(tan(float(x))/sin(float(x)))
        elif c2=='*':
            print(tan(float(x))*sin(float(x)))
        else:
             print("Syntax Error : please type help to see help documentation")
    elif c1.startswith('tan(') and c3.startswith('cos('):
        x = c1[4:-1]
        y = c3[4:-1]
        if c2 == '+':
            print(tan(float(x))+cos(float(x)))
        elif c2=='-':
            print(tan(float(x))-cos(float(x)))
        elif c2=='/':
            print(tan(float(x))/cos(float(x)))
        elif c2=='*':
            print(tan(float(x))*cos(float(x)))
        else:
             print("Syntax Error : please type help to see help documentation")
    elif c1.startswith('tan(') and c3.startswith('cot('):
        x = c1[4:-1]
        y = c3[4:-1]
        if c2 == '+':
            print(tan(float(x))+(1/tan(float(x))))
        elif c2=='-':
            print(tan(float(x))-(1/tan(float(x))))
        elif c2=='/':
            print(tan(float(x))/(1/tan(float(x))))
        elif c2=='*':
            print(tan(float(x))*(1/tan(float(x))))
        else:
             print("Syntax Error : please type help to see help documentation")
    elif c1.startswith('tan(') and c3.startswith('sec('):
        x = c1[4:-1]
        y = c3[4:-1]
        if c2 == '+':
            print(tan(float(x))+(1/cos(float(x))))
        elif c2=='-':
            print(tan(float(x))-(1/cos(float(x))))
        elif c2=='/':
            print(tan(float(x))/(1/cos(float(x))))
        elif c2=='*':
            print(tan(float(x))*(1/cos(float(x))))
        else:
             print("Syntax Error : please type help to see help documentation")
    elif c1.startswith('tan(') and c3.startswith('cosec('):
        x = c1[4:-1]
        y = c3[6:-1]
        if c2 == '+':
            print(tan(float(x))+(1/sin(float(x))))
        elif c2=='-':
            print(tan(float(x))-(1/sin(float(x))))
        elif c2=='/':
            print(tan(float(x))/(1/sin(float(x))))
        elif c2=='*':
            print(tan(float(x))*(1/sin(float(x))))
        else:
             print("Syntax Error : please type help to see help documentation")
    else:
        try:
            if c2 == '+':
                print(float(c1)+float(c3))
            elif c2 == '-':
                print(float(c1)-float(c3))
            elif c2 == '/':
                print(float(c1)/float(c3))
            elif c2 == '*':
                print(float(c1)*float(c3))
            elif c2 == '%':
                print(float(c1)%float(c3))
            elif c2 == '//':
                print(float(c1)//float(c3))
            else:
                print('Syntax Error:')
                return
        except ZeroDivisionError:
            print("You cannot divide by Zero you know!")
            return

#Basic funcs:        
def bas_func(b):
    if b.startswith('pow('):
        x = b[4:5]
        y = b[6:7]
        print(pow(float(x),float(y)))
    elif b.startswith('abs('):
        x = b[4:-1]
        print(abs(int(x)))
    elif b.startswith('sqrt('):
        x = b[5:-1]
        if x.startswith('-'):
            print(cmath.sqrt(float(x)))
        else:
            print(sqrt(float(x)))
    elif b.startswith('ceil('):
        x = b[5:-1]
        print(ceil(float(x)))
    elif b.startswith('floor('):
        x = b[6:-1]
        print(floor(float(x)))
    elif b.startswith('exp('):
        x = b[4:-1]
        print(exp(float(x)))
    elif b.startswith('deg('):
        x = b[4:-1]
        print(degrees(float(x)))
    elif b.startswith('rad('):
        x = b[4:-1]
        print(radians(float(x)))
    elif b == 'pi':
        print(pi)
    elif b == 'e':
        print(e)
    elif b.startswith('sin('):
        x = b[4:-1]
        print(sin(float(x)))
    elif b.startswith('cos('):
        x = b[4:-1]
        print(cos(float(x)))
    elif b.startswith('tan('):
        x = b[4:-1]
        print(tan(float(x)))
    elif b.startswith('cot('):
        x = b[4:-1]
        print(1/tan(float(x)))
    elif b.startswith('sec('):
        x = b[4:-1]
        print(1/cos(float(x)))
    elif b.startswith('cosec('):
        x = b[6:-1]
        print(1/sin(float(x)))
    else:
        print(b)

#covertions
def bin_dec(d):
    var1 = list(d)
    dec = 0
    y = len(var1)
    for x in var1:
        y -= 1
        dec += int(x)*pow(2,int(y))
    print(dec)

def oct_dec(d):
    var1 = list(d)
    dec = 0
    y = len(var1)
    for x in var1:
        y -= 1
        dec += int(x)*pow(8,int(y))
    print(dec)

def hex_dec(d):
    #Need to work HEX 'ABCDEF'
    var1 = list(d)
    dec = 0
    y = len(var2)
    for x in var2:
        y -= 1
        dec += int(x)*pow(16,int(y))
    print(dec)
  
#Main func
def main():
    clear()
    banner()
    console()    

#Call main func
main()

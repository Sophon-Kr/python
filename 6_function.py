#function
def Display_Function(parameter_for_display):
    print('This is display function')
    print('Message form Argument:',parameter_for_display)
    return

Display_Function('Hello--'*3)

#requirment argument
#ต่างส่ง จำนวน parameter กับ argument  ให้จำนวนตรงกัน
def Requirment_Function(username,password,userid):
    print('username',username)
    print('password',password)
    print('userid',userid)
    print()
    return

a,b,c='Akira',123321,'0001'
Requirment_Function(a,b,c)
#สลับตำแหน่งได้แต่ชื่อต้องตรงกันและต้องใส่ไปใน argument เลย
print()
Requirment_Function(password=123321,username='Akira',userid='0001')

#Defult Argument
def Defult_Argument(username, password=1234, userid='0001'):
    print('username',username)
    print('password',password)
    print('userid',userid)
    print()
    return

Defult_Argument(username='ABC', password=1234, userid='0001')
Defult_Argument(username='ABC', userid='0001')
Defult_Argument(username='ABC')

#vriable-length arguments
def Variable_Length_Argument(arg1,*vartuple) :
    print('arg1',arg1)
    for var in vartuple :
        print('vartuple',var)
    return;

Variable_Length_Argument(12,20,13,13,31,31,44,3523,53,637,34,78,546,6)
#ตัวแรกจะถูกส่งให้เป็นของ  arg1 ก่อน

######### Anonymous function :lamda
#ไม่ต้องประกาศชื่อ function
sum =lambda arg1,arg2 :arg1+arg2
print('Display lambda function')
print('Value of Total : ',sum(40,60))

print('Lambda in list')
lambda_list=[lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** 4]
for f in lambda_list:
    print(f(3))
print(lambda_list[0](11))

############the return statement####################
def sum(arg1,arg2):
    "Add both the parameter and retern them."
    total=arg1+arg2
    print('Inside the function :',total)
    return total;
total= sum(10,20)
print('Outside the function : ',total)
#more example in 6.1_mini_calculator.py

#--------------------------------------------#


########### Return multiple value################
#ทำได้โดยการใช้ตัวแปรแบบ tuple
import random
def Roll_Dice():
    return(1+random.randrange(6),1+random.randrange(6))

dice_loop=0
while dice_loop < 11 :
    d1,d2=Roll_Dice()
    print(d1,',',d2)
    dice_loop+=1

#-----------------------------------------------------#

#global  variable
#ตอนประกาศไม่ต้อง
#ตอนจะใช้ใน function ให้ใช้ globalนำหน้า
#ไม่งั้นจะมองเป็นคละตัวแปรกัน
print('#########using global#########')
global_variable='This is global variable'
print('Outside function: ',global_variable)

def Global_Display():
    global global_variable
    global_variable = 'inside function'
    print('Inside function: ',global_variable)
Global_Display()
print('Outside function after pass function: ',global_variable)

print('-----------------------------------------')
global_variable='This is global variable'
print('Outside function: ',global_variable)

def Global_Display():
    global_variable = 'inside function'
    print('Inside function: ',global_variable)

Global_Display()
print('Outside function after pass function: ',global_variable)

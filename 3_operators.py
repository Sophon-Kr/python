#operators
a1 = 20
a2 = 3

#####Arithmatic Operator############
print("#####Arithmatic Operator############")
print(a1+a2) #addition
print(a1-a2) #substraction
print(a1*a2) #multipication
print(a1/a2) #division
print(a1%a2) #modulus หารเอาเศษ
print(a1**a2) #exponent ยกกำลัง
print(a1//a2) #floor division หารเอาส่วนปัดเศษทิ้ง
#------------------------------------#

############Comparison operators###########
print("############Comparison operators###########")
print(a1>a2)
print(a1>=a2)
print(a1<a2)
print(a1<=a2)
print(a1==a2)
print(a1!=a2)
#ไม่สามารถใช้ ===,!==,<>(หมายถึงไม่เท่ากัน) เหมือน C/C++ได้
#-----------------------------------------#
################bitwise  operation############
print("#############bitwise  operation############")





#---------------------------------------------#

#####################logical  operation############
print("#############logical  operation############")
A=True
B=False
print('A = ',A)
print('B = ',B)
print('A and B :',A and B)
print('A or B :',A or B)
print('Not B :',not B)

print('A is B :',A is B) #เป็น ใช้เทียบเท่ากับได้
print('A is not B :',A is not B) #ไม่เป็น ใช้เทียบเท่ากับได้

list_1=[1,2,3,4,5,6,7,8,9]
print('1 in list_1',1 in list_1)
print('1 in list_1',1 not in list_1)


def decimalToBinary(n):
    #in-built function
    return bin(n).replace("0b", "")
           
a=0
b=9
print(decimalToBinary(a))
print(decimalToBinary(b))
print(decimalToBinary(a&b)) #and
print(decimalToBinary(a|b)) #or
print(decimalToBinary(a^b)) #xor
print(decimalToBinary(~a)) #not
print(decimalToBinary(b << 3)) #shift left 3 ตำแหน่ง
print(decimalToBinary(b >> 3)) #shift right 3 ตำแหน่ง

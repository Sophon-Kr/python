import sys,random
#decisions
#python ไม่มี switch case

###################if example##################
var_true=1001
if var_true :
    #ค่าที่ไม่ใช่ 0 ,null จะเป็นจริงเสมอ
    print('This condition is true')
    print(var_true)

var_false=0
if var_false :
    print("This condition is false")
    print('This condition not  display')
    print(var_false)

print('Good bye!!!!')
#-------------------------------------------------#

################### if-else example##################
# Calculating discount price and VAT Example
# name_of_goods=input('Input goods name:')
# price_of_goods=float(input('Input price of %s:' %name_of_goods))
# if price_of_goods>=500 :
#     print('you get special price !!!!!!!!')
#     discount=price_of_goods*0.03
#     price_of_goods=price_of_goods-discount
# else:
#     print('you get normal price')
# VAT=price_of_goods*0.07
# price_of_goods=price_of_goods+VAT
# print('The price of %s include VAT is %.2f Baht' %(name_of_goods,price_of_goods))

#-------------------------------------------------#

#####################if - elif########################
#Grade Evalution Example
# name_of_student=input('Input your name:')
# score_of_student=float(input("input your score:"))
# if score_of_student >=80 :
#     print(name_of_student+' '+'your grade is A')
#     print(score_of_student)
# elif score_of_student >=75 :
#     print(name_of_student+' '+'your grade is B+')
#     print(score_of_student)
# elif score_of_student >=70 :
#     print(name_of_student+' '+'your grade is B')
#     print(score_of_student)
# elif score_of_student >=65 :
#     print(name_of_student+' '+'your grade is C+')
#     print(score_of_student)
# elif score_of_student >=60 :
#     print(name_of_student+' '+'your grade is C')
#     print(score_of_student)
# elif score_of_student >=55 :
#     print(name_of_student+' '+'your grade is D+')
#     print(score_of_student)
# elif score_of_student >=50 :
#     print(name_of_student+' '+'your grade is D')
#     print(score_of_student)
# else:
#     print(name_of_student+' '+'your grade is F')
#     print(score_of_student)


#-------------------------------------------------#

##################### Loop ########################
#python ไม่มี switch,do-while,forecach
#while Loop
count=0
while (count <= 9) :
    print('The count is :',count)
    count+=1
print("Bye !!")

#infinit loop
# true_condition=True
# while true_condition == 1:
#     infinite_loop= int(input('Input some number:'))

#else with while and for
number=0
while number < 7 :
    print(number,'less than 7')
    number+=1
else :
    print(number,'is not less than',number)
print("BYE!!")

#-------------------------------------------------#

##################### for loop ########################
fruit_list=['apple','banana','coconut']
for i in range(5,50,5) :
    sys.stdout.write(str(i) +'  ')
    print()
for j in fruit_list:
    print(j)

#time table example
for row in range(1,10) :
    for col in range(1,10) :
        prod=row*col
        if prod<10 :
            print(' ',end='')
        print(prod,' ',end='')
    print()


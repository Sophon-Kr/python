def menu():
    print(" ")
    print('Welcome to calculator program ')
    print('Your option are : ')
    print(' ')
    print('1. Addition')
    print('2. Substraction')
    print('3. Multiplicaion')
    print('4. Division')
    print('5. Quit calculator program')
    print(' ')
    return int(input('Choose your option: '))

def Addition(number_1,number_2):
    print('Addition')
    print('Result of',number_1, '+' , number_2,'is :',number_1+number_2)
    return number_1+number_2

def Substraction(number_1,number_2):
    print('Substraction')
    print('Result of',number_1, '-' , number_2,'is :',number_1-number_2)
    return number_1-number_2

def Multiplicaion(number_1,number_2):
    print('Multiplicaion')
    print('Result of',number_1, '*' , number_2,'is :',number_1*number_2)
    return number_1*number_2

def Division(number_1,number_2):
    if number_2 == 0 :
        print("Can't divide by zero")
        return False
    else:
        print('Division')
        print('Result of',number_1, '/' , number_2,'is :',number_1/number_2)
        return number_1/number_2

def main() :
    loop=1
    choise=0
    while loop==1 :
        choise=menu()
        if choise ==1 :
            Addition(int(input('Input number 1:')),int(input('Input number 2:')))
        elif choise == 2 :
            Substraction(int(input('Input number 1:')),int(input('Input number 2:')))
        elif choise == 3 :
            Division(int(input('Input number 1:')),int(input('Input number 2:')))
        elif choise == 4 :
            Multiplicaion(int(input('Input number 1:')),int(input('Input number 2:')))
        elif choise == 5 :
            loop=0;
        else:
            print("Good bye!!")
    


if __name__ == "__main__" :
    main()

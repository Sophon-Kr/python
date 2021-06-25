import sys, getopt

def display():
    #วิธีการแสดงผลในรูปแบบต่าง ๆ
    # print() เพื่อแสดงผล
    # sys.stdout.write() เพื่อแดงผลต่อในบรรทัดเดียว
    #ความแตกต่าง
    print("Print String");print("Print String2") 
    sys.stdout.write("Print String1");sys.stdout.write("Print String2")

    #เขียยนยาวแต่ไม่หมดในหนึ่งบรรทัดใช้ /
    print()
    print('This is really long lines\
        but we can make it cross\
        multiple lines')
    x=1+2+3\
      +4+5+6\
      +7+8+9
    print(x)
    #หรือใช้ """ """ ครอบ
    str="""This is really long lines
        but we can make it cross
        multiple lines """

    print(str) #แต่แบบนี้จะไม่ต่อกันในหนึ่งบรรทัด
    #ในเครื่องหมาย {} [] () ไม่ต้องใช้ \ 
    day=['Sunday', 'Monday', 'Tuesday', 'Wednesday',
    'Thursday','Friday','Saturday']
    print(day)

    string='Hello python'
    #แสดงหลายครั้ง
    print(string*50)
    print()
    # ต่อข้อความใช้ +
    print(string+'1'+string+'2'+string+'3'+string+'4')
    #สามารถวางตำแหน่งได้เหมือนภาษา C
    print("Hello world.",string)
    print("Hello world. %s" %string)

def InputFunction():
    # username=input("input username:")
    # Id=int(input("input id:"))
    # print(username)
    # print(Id)
    print()

        
def helpfulFunction():
    #dir() บอกข้อมูลภานในโมดูล
    D=dir(main)
    print(D)

    #help() คำสั่งช่วยเหลือ
    # H=help()
    # print(H)


def main():
    print("I'm the main Function.")
    display()
    InputFunction()
    helpfulFunction()


if __name__=="__main__":
    main()
    



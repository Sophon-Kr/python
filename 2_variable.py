# simple variable
string_type = 'Akira'
float_type = 24.75
integer_type = 50
boolean_type = True
complex_Num_type=2 + 7j

print(type(complex_Num_type))
#ประกาศหลายค่าพร้อมกันได้
a=b=c=d=1
j,k,l=10,20,"L-size"
print(a)
print(b)
print(c)
print(d)
print(j)
print(k)
print(l)

#ถ้าให้ เป็น " " ระบบจะมองเป็น string แต่ถ้าไม่ต้องกาารให้ใช้ None
String_none=""
N=None
print(type(String_none))
print(type(N))
#plus integer
x=1
y=2
z=x+y
print(z)

#plus string
a = 'Animal is sloth'
b = 'what is animals'
c = a+b
print(a+b)

#string  and integer
#if string plus interger ERROR 
#convert First
b1 = int('20')
#b1 = float('20.22')
b2 = 50
B3 = b1+b2
print(B3)
#or 
b1 = '20'
b2 = str(50);
#ห้ามตั้งชื่อตัวแปรว่า str เพราะจะทำให้ใช้งาน function  str ไม่ได้
B3 = b1+b2
print(B3)

#การเลือกแสดง string structure variable[start:end:step]
#ถ้าติดลบจะนับจากหลังมาเริ่มที่ 1
print()
Sring_display="00123456789"
print(Sring_display[3:7])
print(Sring_display[-2:-9:-1])
#****เราไม้่สามารถกำหนดค่าตรงๆให้ string  ได้ ต้องใช้ str.replace(old, new [, count]) 
Sring_display=Sring_display.replace('0','K',1)
print(Sring_display[0::])



#################list########################
# ใช้เครื่องหมาย  []  ประเภทข้อมูลต่างกันได้
lst1=[1,2,3,4,5,'String1',3.456,'String2']
print(type(lst1))
print(lst1)
#เข้าถึงข้อมูลได้เหมือน string 
print(lst1[1])
print(lst1[1:6:2])
# สามรถกำหนดโดยบอกตำแหน่ง index ได้เลย
print("Before edit:",lst1[5])
lst1[5]='Edit_String1'
print("After edit:",lst1[5])
#list operations
L=len(lst1) #ความยาวของ list
print(L)

lst2=[9,8,7,6,5,4,3,2,1]
lst3=lst1+lst2 #รวม list โดยการใช้ +
print(lst3)
lst4=lst2*3 #เป็นการทำซ้ำ list
print(lst4)

#สามารถใช้ for เพื่อ เอาข้มูลใน list มาใช้งานได้
for a in lst4:
    print(a)

#สามารถใช้ in เพื่อเช็คข้อมูล //ถ้ามีจะได้ True
b = 9 in lst4
print(b)

#ใช้ del เพื่อลบได้ 
print("Before delete:",lst2)
del(lst2[0])
print("After delete:",lst2)
#--------------------------------------------#

################  Tuples #####################
# คล้าย list แต่จะ fix ขนาดไม่สามารถแก้ไขได้ภายหลัง
# ข้อดีคือ การทำงานรวดเร็ว
# ใช้ ()  เพื่อกำหนด

tuple1=('Sun',1,2,3,123,454.232,"At the End")
print(tuple1)
print(type(tuple1))

#ข้อแตกต่างคือไม่สามารถแก้ไขข้อมูลตรงๆ ได้และขนาดจะ fix
print(tuple1[1])
# tuple1[1]=1000 ถ้าทำแบบนี้จะ  error
#----------------------------------------------#

################  Dictionary #####################
#มีลักษณะคล้าย list ใช้ {} เพื่อกำหนด
#มีการกำหนดข้อมูลเป็นคู่ข้อมูล เป็น key และ value
#key ไม่ควรใช้ซ้ำ
dict1={123:"Sunday",456:'Monday'}
print(dict1)
print(dict1[123])
# การเรียกช้งานให้เรียกใช้งานโดย key แทนการเรียก index แบบ list
# ถ้าใช้ index เช่น dict1[1] จะ error
dict2={'Name':'Akira','Age':22,'Point':2.454}
print(dict2['Name'])
print(dict2['Age'])
print(dict2['Point'])
#สามารถเพิ่มข้อมูลใน dictionary ได้เรื่อยๆ  ****แต่ต้องประกาศว่างไว้ก่อน 
dict3={} #จำเป็นต้องมี
dict3['Type']='Animal'
dict3['Number_id']=12345
print(dict3)
#key หลายค่าต่อ หนึ่ง value  ได้
#หนึ่ง key หลาย value ได้
 
tuple_key=(1,2,3,4,5,6,7)
tuple_value=('animal','bird','cat','doraemon','elegant','finish','gold')

complex_dict_key={}
complex_dict_value={}

complex_dict_key[tuple_key]='Number_type'
complex_dict_value['String_type']=tuple_value
print(complex_dict_key)
print(complex_dict_value)

#สามารถใช้ for เพื่อ เอาข้อมูลออกมาใช้ได้ตามปกติ
for i in complex_dict_value:
    print(i) #key
    print(complex_dict_value[i]) #value

    for j in complex_dict_value[i]:
       print(j)  # separate value
#----------------------------------------------#

################  sets #####################
# การประกาศ set  ให้ใช้ set() และจะใช้ {}
set1=set()
# set1=() มองเป็น tuple
# set1=[] มองเป็น list
# set1={} มองเป็น dictionary กำหนดตรงๆแบบนี้ไม่ได้
# แต่ถ้ากำหนดเลยใช้ได้ เช่น
set1={'apple','banana','orange'} #set
dict5={1:'apple',2:'banana',3:'orange'} #dictionary มี key:value

print(type(set1))
print(type(dict5))

#สามารถเปลี่ยขนยเป็น set ได้โดยการ ใช้ set(variable)
print(lst1)
print(type(lst1))
set_list1=set(lst1)
print(set_list1)
print(type(set_list1))

# อย่าลืมว่า set คือจะไม่ซ้ำถ้าซ้ำจะเหลือตัวเดียว
set2=set('aaaaaaaabbbbbbbbbbbbbcccccccccccccdddddddddddd')
print(set2)

#การดำเนินการกับ set
print('Union:',set1|set2)
set3=set1|set2
print('Intersection:',set1&set3)
print('Differnce:',set1-set2)
print('Differnce:',set2-set1)
set4={'apple','banana','orange','mango','papaya'} 
set5={'apple','banana','orange','starfruit','sugar apple'} 
print('symetric difference:',set5^set4) #ตรงข้าม intersectrion คือส่วนที่ไม่เหมือนกันทั้งหมด
#ใช้ operation ได้ปกติ <,<=,>,>=,==,!=,in,not in
#ใช้ for เพื่อเข้าถึงสมาชิก เพราะเราไม่รู้ว่ามีการเรียงอย่างไร



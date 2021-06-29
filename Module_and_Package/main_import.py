#import ทั้ง function และ variable ทั้งหมด ใช้  import mudule
#ถ้ามีหลายอันใช้ ,  เพื่อคั่น import mudule1,module2,module3
#-----------------------------------------------------#
#import บาง function หรือ variable (ไม่ได้ต้องการทั้งหมด)
#from module import function
#-----------------------------------------------------#
#form module import*
# ใช้ * เพื่่อ import ทั้ง function และ variable ทั้งหมด ได้
#-----------------------------------------------------#
#import มาแล้วตั้งชื่อใหม่เพื่อให้ใช้งานง่าย
# import old_module as new_module
#-----------------------------------------------------#
#เรียกใช้งาน module.function(argument)
import calculate_area

calculate_area.square(10,5)

from display_paragraphs import print_string
print_string()
#ถ้า import function แยกไม่ต้องจุดชื่อ module ก่อน
#display_paragraphs.print_string  xxx ผิด
#print_string เรียกใช้ได้เลย

import print_loop as P
P.P_Loop()

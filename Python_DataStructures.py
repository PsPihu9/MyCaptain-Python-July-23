'''
@author: Prashansa Shah 
@description: Coding Data Structures in Python
'''
# Task 1 - find area of circle for input radius

import math

radius=float(input("Input the radius of the circle: "))
area=math.pi*(radius**2)
print("The area of the circle with radius ",radius," is: ",area)


# Task 2 - print extension according to input filename

filename=str(input("Input the Filename: "))
ext=filename.split(".")
if ext[1]=='py':
    print("The extension of the file is : 'python'")
else:
    print("The extension is not '.py'.")

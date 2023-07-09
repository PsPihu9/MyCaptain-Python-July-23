'''
@author: Prashansa Shah 
@description: Coding Loops in Python
'''

# Task - print all positive numbers in a range

n=int(input("Enter the number of elements in the list: "))
print("Enter ",n," numbers: ")
list1=[]

for i in range(n):
    num=int(input())
    if num>0:
        list1.append(num)
print(list1)

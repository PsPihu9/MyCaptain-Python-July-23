'''
@author: Prashansa Shah 
@description: Coding Loops in Python
'''
# Task - print Fibonacci numbers


i=0
j=1
n=int(input("Enter the number of elements of the Fibonacci sequence: "))

while n>0:
    print(i)
    i,j=j,i+j
    n-=1

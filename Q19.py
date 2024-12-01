# Q19  Write a python program print the fibonacci series
num = int(input("Enter a number : "))
a,b=0,1
print("Fibonacci Sequence ")
for i in range(num):
    print(a,end=" ")
    a,b = b, a+b
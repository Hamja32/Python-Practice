# Q16 Write a python program to check prime number 
num = int(input("Enter a number : "))
if num > 1:
    for i in range(2,num):
        if num%i == 0:
            print("The number is not a prime number")
            break
        else:
            print("The number is a prime number")
            break
else:
    print("The number is not a prime number")
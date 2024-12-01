# Q20  Write a python program to check Armstrong number
num = int(input("Enter a number : "))
sum=0
temp = num
while temp > 0:
    digit = temp%10
    sum += digit ** 3
    temp//=10
if sum==num:
    print("The number is an armstrong number")
else:
    print("The number is not an armstrong number")
# Q12 : Write a python program to test whether a passed letter is a vowel or not
letter = input("Enter your letter : ")
if(letter in 'aeiou'):
    print("The letter",letter,"is a vowel")
elif letter.isalpha():
    print("The letter",letter,"is a consonent")
else:
    print("letter",letter,"is","Invalid input..")


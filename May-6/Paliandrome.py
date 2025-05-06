# Function To check Paliandrome Returns True Or False
def palindrome(stringToCheck):
    return stringToCheck == stringToCheck[::-1]

#Taking Input of string
str = input("Enter String :")
if palindrome(str):
    print(str,"is Paliandrome") 
else :
    print(str,"is not Paliandrome")
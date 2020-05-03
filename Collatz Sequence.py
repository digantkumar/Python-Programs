# Python program for Collatz/Syracuse Sequence
# The program lets the user type in a positive integer and keeps running the sequence until the function returns 1.
# Digant Kumar

def collatz(number):
    if number%2 == 0:
        return number//2
    elif number%2 !=0:
        return 3*number + 1

def collatz_seq(num):
    count = 0
    if num>0:
        print(num)
    elif num==0:
        return 0
    else:
        return "Error! Please enter a positive number!"
    while num!= 1 and num>=0:
        num = collatz(num)
        count = count + 1
        print(num)
    return None

try:
    print("Enter number: ", end="")
    num = int(input())
    print(collatz_seq(num))
except ValueError:
    print("Error! Enter integer values only")
    print("Enter number: ", end="")
    num = int(input())
    print(collatz_seq(num))
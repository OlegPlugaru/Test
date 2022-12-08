import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print(Back.RED)

num1 = float(input("Enter first number: "))
print(Back.CYAN)
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    result = num1 + num2
    print(Back.CYAN + "Result is " + str(result))
elif op == "-":
    result = num1 - num2
    print("Result is " + str(result))
else:
    print("Ivalid operator!")
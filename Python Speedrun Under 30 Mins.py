#Comment

"""

Multiline Comment

"""


print("Welcome To Our TFP Calc")

firstNum = int(input("Enter The First Number"))
operator = str(input("Enter The Operator"))
secondNumm = int(input("Enter The Second Number"))

def Calculator():
    if operator == "+":
        print(firstNum + secondNumm)
    elif operator == "-":
        print(firstNum - secondNumm)
    elif operator == "*":
        print(firstNum * secondNumm)
    elif operator == "/":
        print(firstNum / secondNumm)
    else:
        print("Please Check Your Operator. And Try Again!")


Calculator()

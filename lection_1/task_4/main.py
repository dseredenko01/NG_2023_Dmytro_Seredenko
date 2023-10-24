import math

operator = (input("Enter an operator (+ - * / √ x^2): "))

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

match operator:
    case '+':
        print(round(num1 + num2, 4))
    case '-':
        print(round(num1 - num2, 4))
    case '*':
        print(round(num1 * num2, 4))
    case '/':
        print(round(num1 / num2, 4))
    case '√':
        print(round(math.sqrt(num1), 4))
    case 'x^2':
        result = pow(num1, 2)
        print(round(result, 4))
    case other:
        print(f"{operator} is invalid operator")

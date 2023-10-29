
operator = (input("Enter an operator (+ - * / √ x^y): "))

if operator == '+' or operator == '-' or operator == '*' or operator == '/':
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
elif operator == 'x^y' or operator == '√':
    match operator:
        case '√':
            num = int(input("Enter the number: "))
            power = int(input("Enter the power from which you want to extract the root: "))
            print(round(num ** (1./power), 4))
        case 'x^y':
            num = float(input("Enter the number: "))
            power = int(input("Enter the power to which you want to raise the number: "))
            print(round(num ** power, 4))
else:
    print(f"{operator} is invalid operator")
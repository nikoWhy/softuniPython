n1 = int(input())
n2 = int(input())
operation = input()

result = 0

if operation == '+' or operation == '-' or operation == '*':
    if operation == '+':
        result = n1 + n2
    elif operation == '-':
        result = n1 - n2
    else:
        result = n1 * n2
    if result % 2 == 0:
        print(f'{n1} {operation} {n2} = {result} - even')
    else:
        print(f'{n1} {operation} {n2} = {result} - odd')
elif (operation == '/' or operation == '%') and n2 > 0:
    if operation == '/':
        result = n1 / n2
        print(f'{n1} {operation} {n2} = {result:.2f}')
    elif operation == '%':
        result = n1 % n2
        print(f'{n1} {operation} {n2} = {result}')

else:
    print(f'Cannot divide {n1} by zero')
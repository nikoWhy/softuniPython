n = int(input())

first_number = int(input())

for i in range (1, n):
    current_number = int(input())
    if current_number > first_number:
        first_number = current_number

print(first_number)
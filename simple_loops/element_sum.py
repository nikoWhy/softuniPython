n = int(input())

first_number = int(input())
sum = first_number

for i in range (1, n):
    current_number = int(input())
    sum += current_number
    if current_number > first_number:
        first_number = current_number

if (sum / 2) == first_number:
    print('Yes')
else:
    diff = abs(sum - 2*first_number)
    print(diff)

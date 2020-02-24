n = int(input())

odd_min = 100000000
odd_max = -1000000000
odd_sum = 0

even_min = 100000000
even_max = -1000000000
even_sum = 0

for i in range (1, n+1):
    current_number = float(input())
    if i%2 == 0:
        even_sum += current_number
        if current_number > even_max:
            even_max = current_number
        if current_number < even_min:
            even_min = current_number
    else:
        odd_sum += current_number
        if current_number > odd_max:
            odd_max = current_number
        if current_number < odd_min:
            odd_min = current_number

if odd_min == 100000000:
    odd_min = 'No'
if odd_max == -1000000000:
    odd_max = 'No'
if even_min == 100000000:
    even_min = 'No'
if even_max == -1000000000:
    even_max = 'No'

print(odd_sum)
print(odd_min)
print(odd_max)
print(even_sum)
print(even_min)
print(even_max)
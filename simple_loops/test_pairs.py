n = int(input())

old_sum = 0
new_sum = 0
diff = 0
for i in range(1, n+1):
    num1 = int(input())
    num2 = int(input())

    new_sum  = num1 + num2
    if (i >1 and old_sum != new_sum):
        diff = abs(new_sum - old_sum)
    old_sum = new_sum

if diff == 0:
    print(f'Yes {new_sum}')
else:
    print(f'No {diff}')
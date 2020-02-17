screening = input()
rows = int(input())
colomns = int(input())
revenue = 0

if screening == 'Premiere':
    revenue = 12 * rows * colomns
elif screening == 'Normal':
    revenue = 7.5 * rows * colomns
else:
    revenue = 5 * rows * colomns

print(f'{revenue:.2f} leva')
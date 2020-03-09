n = int(input())

for row in range(1,n+1):
    for col in range(1, n-row+1):
        print(' ', end='')
    for col in range(0,row):
        print('* ', end='')
    print()

for row in range(1,n):
    for col in range(0, row):
        print(' ', end='')
    for col in range(1, n-col):
        print('* ', end='')
    print()
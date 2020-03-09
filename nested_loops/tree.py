n = int(input())

for row in range(0, n+1):
    star = '*'*row
    space = ' '*(n-row)
    print(space, end='')
    print(star,end='')
    print(' | ', end='')
    print(star,end='')
    print(space)

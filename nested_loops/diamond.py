

n = int(input())

stars = 1

if n%2==0:
    stars += 1

padding = int((n-stars)/2)

for row in range(0,(n+1)//2):
    
    mid = n - 2*padding -2
    
    if mid >= 0:
        print('-'*padding + '*' + '-'*mid + '*' + '-'*padding)
    else:
        print('-'*padding + '*'*stars + '-'*padding)
    if padding > 0:
        padding -= 1

#padding +=1

for row in range(0,(n-1)//2):
    padding += 1
    mid = n - 2*padding -2
    if mid >= 0:
        print('-'*padding + '*' + '-'*mid + '*' + '-'*padding)
    else:
        print('-'*padding + '*'*stars + '-'*padding)
    
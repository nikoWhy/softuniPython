import math

n = int(input())

stars = 1
if n%2 == 0:
    stars +=1

roof_length = math.ceil(n/2)


for row in range(0,roof_length):
    padding = (n-stars) // 2
    print('-'*padding + '*'*stars + '-'*padding)
    stars += 2

for row in range(0,n//2):
    print('|' + '*'*(n-2) + '|')
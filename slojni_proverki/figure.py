h = int(input())
x = int(input())
y = int(input())

if ((x <= 3 * h and x >= 0) and (y <= h and y >= 0)):
    if x == 0 or y == 0 or x == 3 * h or y == h:
        print('border')
    else:
        print('inside')
elif ((x <= 2 * h and x >= h) and (y <= 4 * h and y >= h)):
    if x == h or x == 2 * h or y == h or y == 4 * h:
        print('border2')
    else:
        print('inside2')
else:
    print('outside')
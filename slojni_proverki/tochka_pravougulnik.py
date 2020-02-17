x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x = int(input())
y = int(input())

if (x <= x2 and x >= x1) and (y == y1 or y == y2):
    print('Border')
elif (y <= y2 and y >= y1) and (x == x1 or x == x2):
    print('Border')
else:
    print('Inside / Outside')

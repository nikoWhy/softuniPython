n = int(input())

p1 = 0
p2 = 0
p3 = 0

for i in range(1 , n+1):
    current_num = int(input())
    if current_num%2==0:
        p1 +=1
    if current_num%3==0:
        p2 +=1
    if current_num%4==0:
        p3 +=1

p1 = (p1/n)*100
p2 = (p2/n)*100
p3 = (p3/n)*100

print(p1)
print(p2)
print(p3)
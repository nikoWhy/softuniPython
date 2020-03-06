inherited_money = float(input())
year = int(input())

ivan_age = 18

for year_count in range(1800, year+1):
    if year_count%2 ==0:
        inherited_money -= 12000
    else:
        inherited_money -= 12000 + (ivan_age*50)
    ivan_age += 1

if inherited_money >=0:
    print(f'Yes {inherited_money:.2f}')
else:
    print(f'No {abs(inherited_money):.2f}')
lilly_age = int(input())
washing_machine_price = float(input())
price_per_toy = int(input())

toys_money = 0
birthday_money = 10
saved_money_birthday = 0
total_money = 0

for i in range(1, lilly_age+1):
    if i%2 ==0:
        saved_money_birthday += (birthday_money - 1)
        birthday_money+= 10
    else:
        toys_money+=price_per_toy

total_money = saved_money_birthday + toys_money


if total_money >= washing_machine_price:
    print(f'Yes {total_money-washing_machine_price}')
else:
    print(f'No {washing_machine_price - total_money}')
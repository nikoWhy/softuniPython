distance = int(input())
typeDay = input()

if distance < 20:
    if typeDay == "day":
        price = 0.7 + (0.79 * distance)
    else:
        price = 0.7 + (0.9 * distance)
elif distance < 100:
    price = distance * 0.09
else:
    price = distance * 0.06

print(round(price, 2))
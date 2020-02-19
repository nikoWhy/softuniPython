month = input()
nights = int(input())

studio_price = 76
apartment_price = 77
studio_total_price = studio_price * nights
apartment_total_price = apartment_price * nights

if month == 'May' or month == 'October':
    studio_price = 50
    apartment_price = 65
    studio_total_price = studio_price * nights
    apartment_total_price = apartment_price * nights
    if nights > 14:
        studio_total_price = studio_total_price * 0.7
        apartment_total_price = apartment_total_price * 0.9
    elif nights > 7:
        studio_total_price = studio_total_price * 0.95
elif month == 'June' or month == 'September':
    studio_price = 75.2
    apartment_price = 68.70
    studio_total_price = studio_price * nights
    apartment_total_price = apartment_price * nights
    if nights > 14:
        studio_total_price = studio_total_price * 0.8
        apartment_total_price = apartment_total_price * 0.9
elif (month == 'July' or month == 'August') and nights > 14:
        apartment_total_price = apartment_total_price * 0.9

print(f'{apartment_total_price:.2f} lv.')
print(f'{studio_total_price:.2f} lv.')
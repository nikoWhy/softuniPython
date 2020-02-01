days_per_month = int(input())
dollars_per_day = float(input())
dollar_leva = float(input())

money_per_month = days_per_month * dollars_per_day

money_per_year = money_per_month * 12 + 2.5 * money_per_month

net_year_money = money_per_year - 0.25 * money_per_year

dollars_per_day = net_year_money / 365

leva_per_day = dollars_per_day * dollar_leva

print(f'{leva_per_day:.2f}')
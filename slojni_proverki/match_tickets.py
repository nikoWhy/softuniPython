total_budget = float(input())
category = input()
persons = int(input())

vip_ticket_price = 499.99
normal_ticket_price = 249.99
budget = 0

if category == 'VIP':
    if persons >= 1 and persons <= 4:
        budget = (total_budget - total_budget * 0.75) - persons * vip_ticket_price
    elif persons <= 9:
        budget = (total_budget - total_budget * 0.6) - persons * vip_ticket_price
    elif persons <= 24:
        budget = (total_budget - total_budget * 0.5) - persons * vip_ticket_price
    elif persons <= 49:
        budget = (total_budget - total_budget * 0.4) - persons * vip_ticket_price
    else:
        budget = (total_budget - total_budget * 0.25) - persons * vip_ticket_price
else:
    if persons >= 1 and persons <= 4:
        budget = (total_budget - total_budget * 0.75) - persons * normal_ticket_price
    elif persons <= 9:
        budget = (total_budget - total_budget * 0.6) - persons * normal_ticket_price
    elif persons <= 24:
        budget = (total_budget - total_budget * 0.5) - persons * normal_ticket_price
    elif persons <= 49:
        budget = (total_budget - total_budget * 0.4) - persons * normal_ticket_price
    else:
        budget = (total_budget - total_budget * 0.25) - persons * normal_ticket_price

if budget >= 0:
    print(f'Yes! You have {budget:.2f} leva left.')
else:
    print(f'Not enough money! You need {abs(budget):.2f} leva.')
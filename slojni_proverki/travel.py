budget = float(input())
season = input()
destination = ''
stay = 'Hotel'

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        budget = budget * 0.3
        stay = 'Camp'
    else:
        budget = budget * 0.7
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        budget = budget * 0.4
        stay = 'Camp'
    else:
        budget = budget * 0.8
else:
    destination = 'Europa'
    budget = budget * 0.9

print(f'Somewhere in {destination}')
print(f'{stay} - {budget:.2f}')
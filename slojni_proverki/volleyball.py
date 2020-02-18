from math import trunc

year_type = input()
holidays = int(input())
weekends_home = int(input())

weekends_sofia = 48 - weekends_home
weekends_sofia_play = weekends_sofia * 3 / 4
play_holidays = holidays * 2 / 3

play_total = play_holidays + weekends_home + weekends_sofia_play

if year_type == 'leap':
    play_total = play_total * 1.15

print(trunc(play_total))
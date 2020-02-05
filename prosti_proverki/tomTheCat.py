from math import fabs

restDays = int(input())

workDays = 365 - restDays
playTime = (workDays * 63) + (restDays * 127)

timeDifference = fabs(30000 - playTime)
hours = timeDifference // 60
minutes = timeDifference % 60

if playTime <= 30000:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
else:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
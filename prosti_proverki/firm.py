from math import trunc

necessaryHours = int(input())
days = int(input())
workers = int(input())

projectDays = days * 0.9

projectHours = trunc(projectDays * 10 * workers)

if projectHours < necessaryHours:
    print(f"Not enough time!{necessaryHours - projectHours} hours needed.")
else:
    print(f"Yes!{projectHours - necessaryHours} hours left.")
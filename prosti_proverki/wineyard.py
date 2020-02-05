from math import trunc, ceil

totalArea = int(input())
grapes = float(input())
wineRequest = int(input())
workers = int(input())

wineyardArea = totalArea * 0.4
grapesWine = grapes * wineyardArea

wine = grapesWine / 2.5

if wine < wineRequest:
    print(f"It will be a tough winter! More {trunc(wineRequest - wine)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {trunc(wine)} liters.")
    print(f"{ceil(wine - wineRequest)} liters left -> {ceil((wine - wineRequest) / workers)} liters per person.")
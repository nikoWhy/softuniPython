from math import pi

figureType = input().lower()

if figureType == "square":
    side = float(input())
    area = side * side
elif figureType == "recatangle":
    sideA = float(input())
    sideB = float(input())
    area = sideA * sideB
elif figureType == "circle":
    r = float(input())
    area = pi * r * r
elif figureType == "triangle":
    side = float(input())
    h = float(input())
    area = (side * h) / 2

print(f"{area:.3f}")
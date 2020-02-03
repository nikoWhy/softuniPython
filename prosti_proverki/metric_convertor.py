size = float(input())
sourceMetric = input().lower()
destMetric = input().lower()

def metricCovert(destMetric,size):
    if destMetric == "cm":
        size = size * 100
    elif destMetric == "mm":
        size = size * 1000
    elif destMetric == "mi":
        size = size * 0.000621371192
    elif destMetric == "inch":
        size = size * 39.3700787
    elif destMetric == "km":
        size = size * 0.001
    elif destMetric == "ft":
        size = size * 3.2808399
    elif destMetric == "yd":
        size = size * 1.0936133
    print(size)


if sourceMetric == "mm":
    size = size / 1000
elif sourceMetric == "km":
    size = size / 0.001
elif sourceMetric == "cm":
    size = size / 100
elif sourceMetric == "mi":
    size = size / 0.000621371192
elif sourceMetric == "in":
    size = size / 39.3700787
elif sourceMetric == "ft":
    size = size / 3.2808399
elif sourceMetric == "yd":
    size = size / 1.0936133

metricCovert(destMetric,size)

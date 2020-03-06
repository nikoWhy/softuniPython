n = int(input())

price = 0
bus_count = 0
truck_count = 0
train_count = 0

for i in range(1, n+1):
    current_number = int(input())
    if current_number <= 3:
        bus_count += current_number
    elif current_number <= 11:
        truck_count += current_number
    else:
        train_count += current_number

sum = bus_count + truck_count + train_count

price = (bus_count*200 + truck_count*175 + train_count*120)/sum

bus_count = (bus_count/sum)*100
truck_count = (truck_count/sum)*100
train_count = (train_count/sum)*100

print(price)
print(bus_count)
print(truck_count)
print(train_count)
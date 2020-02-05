from math import trunc

volume = int(input())
flowPipeOne = int(input())
flowPipeTwo = int(input())
hours = float(input())

waterVolume = (flowPipeOne + flowPipeTwo) * hours

waterPercent = trunc((waterVolume / volume) * 100)

pipeOnePercent = trunc((flowPipeOne / (flowPipeOne + flowPipeTwo)) * 100)
pipeTwoPercent = trunc((flowPipeTwo / (flowPipeOne + flowPipeTwo)) * 100)

if volume >= waterVolume:
    print(f"The pool is {waterPercent}% full. Pipe 1: {pipeOnePercent}%. Pipe 2: {pipeTwoPercent}%.")
else:
    print(f"For {hours} hours the pool overflows with {trunc(waterVolume - volume)} liters.")
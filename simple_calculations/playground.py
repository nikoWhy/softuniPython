playground_side = int(input())
tile_width = float(input())
tile_lenght = float(input())
bench_width = int(input())
bench_lenght = int(input())

playground_volume = playground_side ** 2

tile_volume = tile_lenght * tile_width

bench_volume = bench_lenght * bench_width

playground_volume = playground_volume - bench_volume

number_tiles = playground_volume / tile_volume

time_needed = number_tiles * 0.2

print(round(number_tiles, 2))
print(round(time_needed, 2))
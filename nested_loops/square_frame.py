n = int(input())

print('+ ' + '- '*(n-2) + '+')

for row in range(0, n-2):
    print('| ', end = '')
    for col in range(0, n-2):
        print('- ', end='')
    print('|')

print('+ ' + '- '*(n-2) + '+')
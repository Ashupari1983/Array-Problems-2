def water(n):
    bars = [0, n, 0, n, 0]
    return min(max(bars[:3]), max(bars[2:])) - bars[2]

a = int(input('Enter bar height: '))
print('Water accumulated:', water(a))
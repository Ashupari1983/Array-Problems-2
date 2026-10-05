
def profit():
    prices = [1, 8, 4, 9, 2, 4]
    min_price, profit = prices[0], 0

    for i in prices:
        min_price = min(min_price, i)
        profit = max(profit, i - min_price)

    print( profit)

profit()


def prof():
    price = [8, 3, 5, 2, 9, 1, 7]
    profit = 0

    for i in range(1, len(price)):
        if price[i] > price[i - 1]:
            profit += price[i] - price[i - 1]

    print(profit)

prof()

def water():
    bars = [5,2,1,8,9]
    print(min(max(bars[:3]), max(bars[2:])) - bars[2])

water()
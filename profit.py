def pro(n):
    prices = list(range(n,0,-1))+list(range(1,n+1))
    min_price, profit = prices[0],0
    for p in prices[1::]:
        min_price = min(min_price, p)
        profit = max(profit, p - min_price)
    return profit

a = int(input('Enter Number: '))
print('Profit (max): ',pro(a))
def print_prices(prices):
    for price in prices:
        chunks = str(price).split('.')

        if len(chunks[1]) == 1:
            chunks[1] = chunks[1] + '0'
        print(f'{chunks[0]} руб {chunks[1]} коп')


prices = [10.5, 12.8, 7.0, 3.49, 14.98, 12.32, 33.94, 8.20, 47.35, 26.12,
          9.9, 12.2, 10.0, 32.41, 16.42, 18.18, 1.01, 8.05, 2.07, 3.12]
# task 1
print_prices(prices)

# task 2
print(f'\n id(prices) unsorted: \t\t   {id(prices)}')
prices.sort()
print(f'\n id(prices) sorted (in-place): {id(prices)}')

#task 3
print('\n Sorted ascending:')
print_prices(prices)

#task 4
prices_desc = sorted(prices, reverse=True)
print('\n Sorted descending:')
print_prices(prices_desc)

#task 5
print('\n 5 the most expensive goods:')
print_prices(prices_desc[:5])


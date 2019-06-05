#!/usr/bin/python

import argparse

def find_max_profit(prices):
  minimum_price = prices[0]
  maximum_profit = None

  # return if len(prices) < 2
  if len(prices) < 2:
    return maximum_profit

  # start maximum_profit at difference between
  # first 2 prices
  maximum_profit = prices[1] - prices[0]

  # iterate over everything, keep track of minimum price
  # and maximum profit
  for i in range(1, len(prices) - 1):
    profit = prices[i] - minimum_price

    if profit > maximum_profit:
      maximum_profit = profit

    if prices[i] <= minimum_price:
      minimum_price = prices[i]

  return maximum_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  # Use parsed arguments to define prices and profit
  prices = args.integers
  profit = find_max_profit(prices)

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

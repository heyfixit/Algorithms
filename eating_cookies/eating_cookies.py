#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution
def eating_cookies(n, cache=None):
  if n < 0:
    return 0

  if n == 0:
    return 1

  variation_sum = 0
  for i in range(1,4):
    variation_sum += eating_cookies(n - i)

  # print(f"Sum for {n}: {variation_sum}")

  return variation_sum

  # if n == 1:
  #   return 1
  #
  # if n == 2:
  #   return 2
  #
  # if n == 3:
  #   return 4
  #
  # if n == 4:
  #   return 7
  #
  # if n == 5:
  #   return 13


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')

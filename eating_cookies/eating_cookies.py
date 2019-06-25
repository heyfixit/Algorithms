#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution
def eating_cookies(n, cache=None):
  if cache == None:
    cache = [0 for i in range(n + 1)]


  if n < 0:
    return 0

  if n == 0:
    return 1

  if cache[n] > 0 and n < len(cache):
    return cache[n]

  variation_sum = 0
  for i in range(1,4):
    variation_sum += eating_cookies(n - i, cache)

  cache[n] = variation_sum
  return variation_sum

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')

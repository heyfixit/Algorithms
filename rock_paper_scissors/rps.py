#!/usr/bin/python

import sys

def rock_paper_scissors(n):

  choices = ['rock', 'paper', 'scissors']

  def calc_variations(n, variations=None):
    # if n is 0, we're done
    if n == 0:
      return [[]]

    if variations is None:
      variations = {
        1: [[r] for r in choices]
      }

    if n in variations:
      return variations[n]

    result = calc_variations(n - 1, variations)

    new_result = []
    for v in result:
      for c in choices:
        new_result.append(v + [c])

    variations[n] = new_result
    return new_result

  return calc_variations(n)


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')

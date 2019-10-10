#!/usr/bin/python

import sys

def making_change(amount, denominations=[1,5,10,25,50]):
  cache = {0:1}
  coins = [coin for coin in denominations if coin <= amount]
  for coin in coins:
      for higher_amount in range(coin, amount + 1):
          diff = higher_amount - coin
          if diff in cache:
              if higher_amount in cache:
                  cache[higher_amount] += cache[diff]
              else:
                  cache[higher_amount] = cache[diff]                       
  return cache[amount]  
  


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")
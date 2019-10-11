#!/usr/bin/python

import argparse
from math import inf

#attempted a recursve solution, didnt owork so great in the case of negative profits

# def find_max_profit(prices):
#   #find starting point- start at i = 0, if i+1 < i, increment by 1
#   max_profit = -inf
#   min_buy_idx = 0
#   max_profit_sale_idx = 1
#   start = 0

#   #iterate across, calc max profit and max profit sale index:
#   j = start+1
#   while j < len(prices):
#     if prices[j] - prices[start] > max_profit:
#       max_profit = prices[j] - prices[start]
#       min_buy_idx = start
#       max_profit_sale_idx = j
#     j += 1

#   #make subset from buy to index of max profit, get index of minimum buy, update the max_profit
#   subset = prices[start:max_profit_sale_idx+1]
#   min_buy_idx += subset.index(min(subset))
#   max_profit = prices[max_profit_sale_idx] - prices[min_buy_idx]
    
#   #repeat (recursive?) starting at next index after the sale index, compare profit
#   if max_profit_sale_idx == len(prices):
#     return max_profit
#   else:
#     return max(max_profit, find_max_profit(prices[max_profit_sale_idx:]))

def find_max_profit(prices):
    max_profit = -inf
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            if prices[j]-prices[i] > max_profit:
                max_profit = prices[j]-prices[i]
    return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
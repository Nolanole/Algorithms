 #!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

# pointless_zeroes=[]
def eating_cookies(n, pointless_zeroes=[], cache = {0:1, 1:1, 2:2}):
  if n in cache:
    return cache[n]
  else:
    for i in range(max(cache)+1, n+1): 
      cache[i] = eating_cookies(i-3) + eating_cookies(i-2) + eating_cookies(i-1)
    return cache[n]



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
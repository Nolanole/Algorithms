#!/usr/bin/python

import sys

# def rock_paper_scissors(n):
#     rps = ['rock', 'paper', 'scisssors']

#     if n == 1:
#         return [['rock'], ['paper'], ['scissors']]
#     else:
#         base = rock_paper_scissors(n-1)
#         new_list = []
#         for i in range(3):
#             for j in range(len(base)):
#                 new_list += [base[j][:]]
#         for i in range(len(new_list)):
#             if i < len(new_list)/3:
#                 new_list[i].append('rock')
#             elif i < len(new_list)*2/3:
#                 new_list[i].append('paper')
#             else:
#                 new_list[i].append('scissors')
#         return new_list

def rock_paper_scissors(n):
    rps = [['rock'], ['paper'], ['scissors']]
    if n == 1:
        return rps
    else:
        base = rock_paper_scissors(n-1)
        new_list = []
        for i in range(3):
            for j in range(len(base)):
                new_list += [base[j][:]]
        for i in range(len(new_list)):
            if i < len(new_list)/3:
                new_list[i].insert(0, 'rock')
            elif i < len(new_list)*2/3:
                new_list[i].insert(0, 'paper')
            else:
                new_list[i].insert(0, 'scissors')
        return new_list


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
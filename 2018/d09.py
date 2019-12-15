import sys
import re
from blist import blist  # not strictly necessary, but speeds things up immensely 

players, last_marble = map(int, re.findall('\d+', sys.stdin.read()))
next_marble = 1
curr_marble = 0 
i = 0
circle = blist([curr_marble])
scores = [0] * players
player = 0 

while next_marble - 1 != last_marble:
    if next_marble % 23 == 0: 
        m = circle.pop((i - 7) % len(circle))
        scores[player] += next_marble + m

        if i >= 7:
            i -= 1
        i = (i-6) % len(circle)
        curr_marble = circle[i]
    else: 
        i = (i+1) % len(circle) + 1 
        circle.insert(i, next_marble)
        curr_marble = next_marble

    next_marble += 1
    player = (player + 1) % players

print(max(scores))

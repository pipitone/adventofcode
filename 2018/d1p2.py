import sys
import itertools

last_freq = 0
freqs = set([last_freq])

for freq in itertools.accumulate(map(int, itertools.cycle(sys.stdin))):
    if freq in freqs: 
        print(freq)
        break
    freqs.add(freq)
    last_freq = freq
        



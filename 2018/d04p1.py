import sys
import re
import datetime
import collections
import itertools
records = map(lambda r: re.findall('\[(.*)\] (.*)', r)[0], sys.stdin)
records = sorted( [(datetime.datetime.fromisoformat(d), m) for (d,m) in records], 
        key = lambda x: x[0]) 

minutes = collections.defaultdict(list)
guards = collections.defaultdict(list)

pos = 0
guard = None
while pos < len(records): 
    if "#" in records[pos][1]: 
        guard = re.findall('#(\d+)', records[pos][1])[0]
        pos += 1

    start_min = records[pos][0].minute
    end_min = records[pos+1][0].minute
    for m in range(start_min, end_min):
        minutes[m].append(int(guard))
        guards[int(guard)].append(m)
    pos += 2 

def max_freq(l):
    " returns element, freq"
    return collections.Counter(l).most_common(1)[0]
    
# part 1
sleepy_guard, _ = max_freq(itertools.chain(*minutes.values()))
sleepy_minute, _ = max_freq(guards[sleepy_guard])
print(sleepy_guard*sleepy_minute)

# part 2
m, guard, freq = sorted([ (m, *max_freq(v)) for m,v in minutes.items()], key = lambda x: x[2])[-1]
print(guard * m)



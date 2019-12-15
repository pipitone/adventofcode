import sys
import re
import collections

def step_duration(step): 
    return ord(step) - ord('A') + 1

steps = map(lambda x: re.findall('[A-Z]', x[1:]), sys.stdin)
depends = collections.defaultdict(set)
for pre,post in steps:
    depends[pre].update([])
    depends[post].add(pre)

bonus = 60 
num_workers = 5
jobs = {} # step -> end time
time = 0

while len(depends) > 0: 
    for step, time in [ (s,t) for s,t in jobs.items() if t == min(jobs.values()) ]:
        del jobs[step]
        del depends[step]
        for i in depends.keys(): 
            depends[i].discard(step)

    next_steps = sorted([ k for k,v in depends.items() if not v and k not in jobs.keys()])
    for step in next_steps[:num_workers - len(jobs)]:
        jobs[step] = time + bonus + step_duration(step)

print(time)

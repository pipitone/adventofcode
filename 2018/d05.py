import sys
import re
import string

def react(poly):
    return re.sub(r'([a-z])\1-','', 
                re.sub(r'([a-z])-\1([^-])',r'\2', poly))

def fully_react(poly): 
    reacted_polymer = None

    while True:
        reacted_polymer = react(poly)
        if poly == reacted_polymer: 
            break
        poly = reacted_polymer

    return len(reacted_polymer.replace('-',''))-1

polymer = sys.stdin.read().strip()+"0" #sentinel
polymer = re.sub('([A-Z])', lambda p: p.group(1).lower() + "-",polymer)
print(fully_react(polymer))

experiments = []
for c in string.ascii_lowercase: 
    new_polymer = polymer.replace(c+'-','').replace(c,'')
    reacted_length = fully_react(new_polymer)
    experiments.append([c,reacted_length])

print(min(experiments, key = lambda x:x[1]))


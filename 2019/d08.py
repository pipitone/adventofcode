import sys
import textwrap

w = int(sys.argv[1])#25 
h = int(sys.argv[2]) #6
imagedata = sys.stdin.read().strip()

lcounts = {l.count('0') : l for l in textwrap.wrap(imagedata, w*h)}
print([l.count('1')*l.count('2') for c,l in lcounts.items() if c == min(lcounts.keys())])

layers = [list(x) for x in textwrap.wrap(imagedata, w*h)]
visible = [ [p for p in l if p != '2'][0] for l in zip(*layers)]
print('\n'.join(textwrap.wrap(''.join(visible), w)).replace('0',' '))

import sys
start, end = 278384, 824795

allnumbers = [str(i) for i in range(start, end+1)]
monotonic = [s for s in allnumbers if s == ''.join(sorted(s))]

doublets = [s for s in monotonic if any(str(d)*2 in s for d in range(10))]
print(len(doublets))

notriplets = [s for s in doublets if any(str(d)*2 in s and not str(d)*3 in s for d in range(10))]
print(len(notriplets))

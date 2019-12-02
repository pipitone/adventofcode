import sys
print reduce(lambda p, n: int(n) + p, sys.stdin, 0)

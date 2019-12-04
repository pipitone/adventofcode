start, end = 278384, 824795
e = 6
p1 = 0
p2 = 0
for i in range(start, end+1): 
    k = i 
    d0 = -1      # 2nd previous digit
    d1 = -1      # 1st previous digit
    monotonic = True  
    repeated = False   # true if there are repeated digits
    double = -1        # digit appearing in a strict doublet
    for j in range(e+1):
        d2 = i // 10**(e - j)  # get the jth digit
        if d2 < d1: 
            monotonic = False
            break
        if d2 == d1: 
            repeated = True
            if double == -1:  # only need one doublet
                double = d2  
        if d2 == d1 and d1 == d0 and double == d2:  # if a doublet is actually a triplet...
            double = -1
        i -= d2 * (10**(e-j)) # subtract the jth digit
        d0 = d1
        d1 = d2
    p1 += monotonic and repeated
    p2 += monotonic and (double != -1)
print(p1)
print(p2)

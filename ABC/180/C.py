import sys
import os
f = open('test.txt','r')
sys.stdin = f

import math
n = int(input())

smaller = [i for i in range(1,int(math.sqrt(n))+1) if n%i==0]
bigger = [n//j for j in smaller]

smaller.extend(bigger)
ans = list(set(smaller))
ans.sort()
for a in ans:
    print(a)

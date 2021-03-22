import sys
import os
f = open('test.txt','r')
sys.stdin = f

s = input()
print('x'*len(s))

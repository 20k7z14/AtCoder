import sys
import os
f = open('test.txt','r')
sys.stdin = f

a,b = map(str,input().split())
print(min(a*int(b),b*int(a)))

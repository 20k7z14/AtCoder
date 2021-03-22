import sys
import os
f = open('test.txt','r')
sys.stdin = f

n,k = map(int,input().split())
d = set(map(int,input().split()))

num = {0,1,2,3,4,5,6,7,8,9}

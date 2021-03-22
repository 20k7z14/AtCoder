import sys
import os
f = open('test.txt','r')
sys.stdin = f

n = int(input())
a = list(map(int,input().split()))

even = [i for i in a if i % 2 == 0]
judge = [j for j in even if j%3==0 or j%5==0]

if len(even)==len(judge):
    print('APPROVED')
else:
    print('DENIED')

import sys
import os
f = open('test.txt','r')
sys.stdin = f

n = int(input())
vote = []
for i in range(n):
    vote.append(list(map(int,input().split())))

print(vote)

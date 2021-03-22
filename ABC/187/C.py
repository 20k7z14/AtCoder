import sys
import os
f = open('test.txt','r')
sys.stdin = f

n = int(input())
S = [input() for i in range(n)]

a = set([i[1:] for i in S if i[0]=='!'])
b = set([j for j in S if j[0]!='!'])

if len(a&b) > 0:
    print((a&b).pop())
else:
    print('satisfiable')

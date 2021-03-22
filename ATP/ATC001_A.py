import sys
import os
f = open('test.txt','r')
sys.stdin = f

sys.setrecursionlimit(10**7)
H,W = map(int,input().split())
C = []
for h in range(H):
    C.append(list(input()))

def dfs(x,y,):
    if not(0<=x<H) or not(0<=y<W) or C[x][y] == '#':
        return
    elif C[x][y] == 'g':
        return True
    else:
        C[x][y] = '#'
        dfs(x+1,y) # right
        dfs(x-1,y) # left
        dfs(x,y+1) # down
        dfs(x,y-1) # up

for i in range(H):
    for j in range(W):
        if C[i][j] == 's':
            sx,sy = i,j

if dfs(sx,sy):
    print('Yes')
else:
    print('No')

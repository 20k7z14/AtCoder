import sys
import os
f = open('test.txt','r')
sys.stdin = f

sys.setrecursionlimit(10**7)
H,W = map(int,input().split())
C = []
for h in range(H):
    C.append(list(input()))

def dfs(x,y):
    if not 0 <= x < H or not 0 <= y < W  or C[x][y] == '#':
        return
    elif C[x][y] == 'g':
        print('Yes')
        sys.exit()
    else:
        C[x][y] = '#'
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)

for i in range(H):
    for j in range(W):
        if C[i][j] == 's':
            sx,sy = i,j

dfs(sx,sy)
print('No')

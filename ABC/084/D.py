import sys
import os
f = open('test.txt','r')
sys.stdin = f

h,w = map(int,input().split())
fig = [list(input()) for i in range(h)]
flag = [[0]*w]*h

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def dfs(bx,by,area,rnd):
    for x,y in zip(dx,dy):
        if 0 <= bx+x < h and 0<= by+y < w and fig[bx+x][by+y] == '#':
            fig[bx][by] = '.'
            if flag[bx+x][by+y] == 0:
                rnd += 1
            area += 1
            flag[bx][by]=1
            for f in fig:
                print(*f)
            print()
            return dfs(bx+x,by+y,area,rnd)
        else:
            continue
    return area,rnd

ans = []
for i in range(h):
    for j in range(w):
        if fig[i][j] == '#':
            flag[i][j] = 1
            a,c = dfs(i,j,1,0)
            ans.append([a,4*a-2*c])
for a in ans:
    print(*a)

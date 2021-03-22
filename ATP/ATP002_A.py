import sys
import os
f = open('test.txt','r')
sys.stdin = f

h,w = map(int,input().split())
sy,sx = map(int,input().split())
gy,gx = map(int,input().split())

maze = []
step = []
for i in range(h):
    maze.append(list(input()))
    step.append([None for c in maze[i]])

step[sy-1][sx-1] = 0
queue = [(sx-1,sy-1)]

while queue:
    x, y = queue.pop()
    for dx,dy in [(-1, 0),(0, 1),(1, 0),(0, -1)]:
        if step[y+dy][x+dx] is not None:
            continue

        if maze[y+dy][x+dx] == '.':
            step[y+dy][x+dx] = step[y][x]+1
            queue.insert(0,(x+dx,y+dy))

    if step[gy-1][gx-1] is not None:
        break
print(step[gy-1][gx-1])

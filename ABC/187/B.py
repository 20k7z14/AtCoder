import sys
import os
f = open('test.txt','r')
sys.stdin = f

n = int(input())
point = []
for i in range(n):
    point.append(list(map(int,input().split())))
ans = 0
for i in range(n):
    for j in range(i+1,n):
        s = (point[i][1] - point[j][1]) / (point[i][0] - point[j][0])
        if -1 <= s and s <= 1:
            ans += 1
print(ans)

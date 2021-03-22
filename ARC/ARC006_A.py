import sys
import os
f = open('test.txt','r')
sys.stdin = f

hit = set(map(int,input().split()))
bonas = set()
bonas.add(int(input()))
accept = set(map(int,input().split()))

check = accept - hit
if len(check) == 0:
    print(1)
elif len(check) == 1:
    if check == bonas:
        print(2)
    else:
        print(3)
elif len(check) == 2:
    print(4)
elif len(check) == 3:
    print(5)
else:
    print(0)

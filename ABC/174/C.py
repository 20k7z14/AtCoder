import sys
import os
f = open('test.txt','r')
sys.stdin = f

def main():
    k = int(input())
    a = [7%k]
    for i in range(1,k):
        a.append((10*a[i-1]+7)%k)
    for i in range(k):
        if a[i] == 0:
            print(i+1)
            return 0
    print(-1)
    return 0

main()

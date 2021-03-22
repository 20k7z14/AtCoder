import sys
import os
f = open('test.txt','r')
sys.stdin = f

def f():
    S = input()

    for bit in range(1 << 3):
        formula = S[0]

        for i in range(3):
            if bit &(1<<i):
                formula += '+'
            else:
                formula += '-'
            formula += S[i+1]

        if eval(formula) == 7:
            print(formula + '=7')
            return

if __name__ == '__main__':
    f()

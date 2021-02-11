import sys
import copy
sys.stdin = open('input.txt', 'r')
N=int(input())
dr=list(input().split())

def checker(lc, R, C):
    if lc[0]>=R or lc[0]<0 or lc[1]>=C or lc[1]<0:
        return False
    else:
        return True

def mover(dr, lc, R, C):
    lc_t = copy.deepcopy(lc)
    if dr == 'U':
        lc_t[0] -= 1
    elif dr == 'D':
        lc_t[0] += 1
    elif dr == 'L':
        lc_t[1] -= 1
    elif dr == 'R':
        lc_t[1] += 1

    if checker(lc_t, R, C):
        return lc_t
    else:
        return lc


# 시작은 1, 1
lc = [0, 0]
R, C = N, N
for d in dr:
    lc=mover(d, lc, R, C)
    print(lc)
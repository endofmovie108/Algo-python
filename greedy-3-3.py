# 96p
# greedy

import sys
sys.stdin=open('input.txt', 'r')
N, M = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]

maxv = -1
maxi = 0
for r in range(N):
    t = min(mat[r][:])
    if t > maxv:
        maxi = r
        maxv = t

print(maxi, maxv)
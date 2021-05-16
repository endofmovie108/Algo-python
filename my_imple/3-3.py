import sys
sys.stdin = open('input.txt', 'rt')
N, M = map(int, input().split())

dats = []
max_val = 0
for r in range(N):
    dat = list(map(int, input().split()))
    tmp_val = min(dat)
    if tmp_val > max_val: max_val = tmp_val

print(max_val)

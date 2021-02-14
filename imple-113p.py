import sys
sys.stdin = open('input.txt', 'r')
N = int(input())
cnt=0
for h in range(N+1):
    hs = '%02d' % h
    for m in range(60):
        ms = '%02d' % m
        for s in range(60):
            ss = '%02d' % s
            if '3' in hs+ms+ss:
                cnt += 1
                continue

print(cnt)

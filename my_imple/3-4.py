import sys
sys.stdin = open('input.txt', 'rt')
N, K = map(int, input().split())
cnt = 0
while True:
    cnt += 1
    if N % K == 0:
        N /= K
    else:
        N -= 1

    if N == 1:
        print(cnt)
        break
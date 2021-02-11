# p99
# 문제의 조건에서 K>=2 이며
# 따라서 1을 빼는것 보다 K로 나누는것이 우선이다.
# 따라서 그리디로 해결 가능
# greedy

import sys
sys.stdin=open('input.txt', 'rt')

n, k = map(int, input().split())

cnt = 0
while True:
    if n == 1: break
    cnt += 1
    t = n % k
    if t == 0:
        n /= k
    else:
        n -= 1

print(cnt)
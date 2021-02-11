# 92p
# greedy
import sys
sys.stdin = open("input.txt", "r")
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
cnt = 0
res = 0
for i in range(m):
    cnt += 1
    if cnt > k:
        cnt = 0
        res += data[1]
    else:
        res += data[0]
print(res)
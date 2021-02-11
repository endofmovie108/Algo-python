# 92p
# greedy
import sys
sys.stdin = open("input.txt", "r")
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
cnt = 0
res = []
for i in range(k+1):
    cnt += 1
    if cnt > k:
        cnt = 0
        res.append(data[1])
    else:
        res.append(data[0])

print(sum(res)*m//(k+1) + sum(res[:m%(k+1)]))

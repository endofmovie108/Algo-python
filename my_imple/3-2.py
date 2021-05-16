import sys
sys.stdin = open('input.txt', 'rt')

N, M, K = map(int, input().split())
dats = list(map(int, input().split()))
dats.sort(reverse = True)
print(dats)

D1 = dats[0]
D2 = dats[1]

tot_iter_quo = int(M / (K+1)) # 몫
tot_iter_rem = M - tot_iter_quo*(K+1) # 나머지

res_val = (D1 * K + D2)*tot_iter_quo + D1*tot_iter_rem
print(res_val)
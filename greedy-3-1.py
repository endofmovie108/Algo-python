# greedy
# greedy 가 꼭 정당한것은 아니다,
# 해당 문제는 500원이 100, 50, 10원의 배수이며
# 100원이 50, 10원의 배수이고
# 50원이 10원의 배수이므로 그리디로 해결이 가능한 것.
# 87p

N = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += N//coin
    N %= coin

print(count)

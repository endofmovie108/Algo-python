import sys
sys.stdin=open('input.txt', 'rt')
c_loc = input()
n_loc = [ord(c_loc[0])-ord('a'), ord(c_loc[1])-ord('1')]
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
cnt = 0
for s in steps:
    if 0 < n_loc[0]+s[0] < 8 and 0 < n_loc[1]+s[1] < 8:
        cnt += 1

print(cnt)
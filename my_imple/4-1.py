import sys
sys.stdin = open('input.txt', 'rt')
N=int(input())
moves = input().split()
ROW = 0
COL = 1
cur_loc = [0, 0]

for move in moves:
    nxt_loc = cur_loc.copy()
    if move == 'U':
        nxt_loc[ROW] -= 1
    elif move == 'D':
        nxt_loc[ROW] += 1
    elif move == 'L':
        nxt_loc[COL] -= 1
    elif move == 'R':
        nxt_loc[COL] += 1
    else:
        raise Exception('Direction error!')

    if 0 <= nxt_loc[ROW] < N and 0 <= nxt_loc[COL] < N:
        cur_loc = nxt_loc
    else:
        continue

print(cur_loc)
import sys
from collections import deque

sys.stdin=open('input.txt', 'rt')
N, M = map(int, input().split())
r, c, d = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
chks = [[0]*M for _ in range(N)]

cur_loc = [r, c, d]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def rotate(cur_loc):
    cur_loc[2] += 3
    cur_loc[2] %= 4
    return cur_loc

fail_cnt = 0
chk_cnt = 1
while True:
    # cond 3-1: 네 방향 모두 가보거나 벽인 경우
    if fail_cnt == 4:
        # cond 3-2: 후진이 가능하다면
        if maps[cur_loc[0]-dr[cur_loc[2]]][cur_loc[1]-dc[cur_loc[2]]] == 0 and \
                chks[cur_loc[0]-dr[cur_loc[2]]][cur_loc[1]-dc[cur_loc[2]]] == 0:
            chk_cnt += 1
            chks[cur_loc[0]-dr[cur_loc[2]]][cur_loc[1]-dc[cur_loc[2]]] = 1
            cur_loc[0] -= dr[cur_loc[2]]
            cur_loc[1] -= dc[cur_loc[2]]
        else:
            print(chk_cnt)
            break

    # cond 1: 왼쪽 방향으로 1회 회전
    cur_loc = rotate(cur_loc)

    # cond 2-1: 만약 방문하지 않은 칸이라면 전진
    if maps[cur_loc[0]+dr[cur_loc[2]]][cur_loc[1]+dc[cur_loc[2]]] == 0 and \
            chks[cur_loc[0]+dr[cur_loc[2]]][cur_loc[1]+dc[cur_loc[2]]] == 0:
        chk_cnt += 1
        chks[cur_loc[0]+dr[cur_loc[2]]][cur_loc[1]+dc[cur_loc[2]]] = 1
        cur_loc[0] += dr[cur_loc[2]]
        cur_loc[1] += dc[cur_loc[2]]
    # cond 2-2: 만약 이미 방문하였거나 벽이라면
    else:
        fail_cnt += 1
        continue

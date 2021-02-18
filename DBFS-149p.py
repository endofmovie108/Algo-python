import sys
sys.stdin=open('input.txt', 'rt')
N, M=map(int, input().split())
maps = [list(input()) for _ in range(N)]
chks = [[0]*M for _ in range(N)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def BFS(r, c, chks):
    global N, M
    for i in range(4):
        rt = r+dr[i]
        ct = c+dc[i]
        if (0<=rt<N and 0<=ct<M) and chks[rt][ct] == 0 and maps[rt][ct] == '0':
            chks[rt][ct] = 1
            BFS(rt, ct, chks)
    else:
        return

cnt = 0
for r in range(N):
    for c in range(M):
        if chks[r][c] == 0 and maps[r][c] == '0':
            cnt += 1
            BFS(r, c, chks)

print(cnt)

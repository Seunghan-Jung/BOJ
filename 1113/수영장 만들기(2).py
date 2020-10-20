import sys

sys.stdin = open('input.txt')

import sys

sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())

grid = [[*map(int, input())] for _ in range(N)]

delta = ((1, 0), (0, 1), (-1, 0), (0, -1))


def check(x, y):
    return 0 <= x < N and 0 <= y < M


def start(x, y):
    global answer

    li = {(x, y)}
    wall = dfs(x, y, li)

    if wall is False:
        for i, j in li:
            visit[i][j] = True
    else:
        for i, j in li:
            answer += wall - grid[i][j]
            grid[i][j] = wall
        start(x, y)


def dfs(x, y, li):
    h = grid[x][y]

    wall = float('inf')

    for dx, dy in delta:
        nx, ny = x + dx, y + dy

        if not check(nx, ny):
            return False

        if grid[nx][ny] < h:
            return False
        elif grid[nx][ny] == h and (nx, ny) not in li:
            li.add((nx, ny))
            res = dfs(nx, ny, li)
            if res is not False:
                wall = min(wall, res)
            else:
                return False
        elif grid[nx][ny] > h:
            wall = min(wall, grid[nx][ny])

    return wall


visit = [[False] * M for _ in range(N)]
answer = 0

for i in range(N):
    for j in range(M):
        if not visit[i][j]:
            start(i, j)

print(answer)

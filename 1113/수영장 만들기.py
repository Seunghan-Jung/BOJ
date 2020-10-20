# import sys
#
# sys.stdin = open('input.txt')
#
#
# class Ground:
#
#     def __init__(self, height):
#         self.size = 1
#         self.height = height
#         self.adj = set()
#         self.available = True
#
#
# N, M = map(int, input().split())
#
# grid = [[*map(int, input())] for _ in range(N)]
#
# pools = []
#
# delta = ((1, 0), (0, 1), (-1, 0), (0, -1))
#
#
# def dfs(x, y, ground: Ground):
#     for dx, dy in delta:
#         nx, ny = x + dx, y + dy
#
#         if nx < 0 or nx >= N or ny < 0 or ny >= M:
#             ground.adj.add(plain)
#             continue
#
#         if grid[nx][ny] == ground.height:
#             _ground = where[nx][ny]
#
#             if _ground is plain:
#                 where[nx][ny] = ground
#                 ground.size += 1
#                 dfs(nx, ny, ground)
#
#             elif _ground != ground:
#                 ground.size += _ground.size
#                 ground.adj.update(_ground.adj)
#                 G.remove(_ground)
#         else:
#             _ground = where[nx][ny]
#
#             if _ground is plain:
#                 create(nx, ny, ground)
#
#             else:
#                 ground.adj.add(_ground)
#                 _ground.adj.add(ground)
#
#
# def create(x, y, pre):
#     height = grid[x][y]
#     new = Ground(height)
#     pre.adj.add(new)
#     new.adj.add(pre)
#
#     G.add(new)
#
#     dfs(x, y, new)
#
#
# G = set()
# inf = float('inf')
# plain = Ground(inf)
#
# where = [[plain] * M for _ in range(N)]
# create(0, 0, plain)
#
# print(G)

import sys

sys.stdin = open('input.txt')

sys.setrecursionlimit(10 ** 4)


class Node:

    def __init__(self, height):
        self.size = 1
        self.height = height
        self.adj = set()

    # def __repr__(self):
    #     return f'높이 {self.height} 너비 {self.size}'


N, M = map(int, input().split())

grid = [[*map(int, input())] for _ in range(N)]

where = [[None] * M for _ in range(N)]

delta = ((-1, 0), (0, 1), (1, 0), (0, -1))


def check(x, y):
    return 0 <= x < N and 0 <= y < M


def dfs(x, y, node):
    for dx, dy in delta:
        nx, ny = x + dx, y + dy

        if not check(nx, ny):
            node.adj.add(ground)
            ground.adj.add(node)
            node_list.discard(node)
            continue

        if grid[nx][ny] == node.height:
            if where[nx][ny] is None:
                node.size += 1
                where[nx][ny] = node
                dfs(nx, ny, node)
        elif where[nx][ny] is not None:
            node.adj.add(where[nx][ny])
            where[nx][ny].adj.add(node)


def create(x, y):
    new_node = Node(grid[x][y])
    node_list.add(new_node)
    where[x][y] = new_node
    dfs(x, y, new_node)


ground = Node(float('-inf'))
node_list = set()

for i in range(N):
    for j in range(M):
        if where[i][j] is None:
            create(i, j)

answer = 0

while node_list:
    node = min(node_list, key=lambda n: n.height)
    min_node = min(node.adj, key=lambda n: n.height)

    if min_node.height < node.height:
        node_list.remove(node)
        continue
    answer += (min_node.height - node.height) * node.size

    node.adj.update(min_node.adj)
    node.size += min_node.size
    node.height = min_node.height

    for n in min_node.adj:
        n.adj.remove(min_node)
        n.adj.add(node)

    node.adj.remove(node)
    if min_node in node_list:
        node_list.remove(min_node)
    else:
        node_list.remove(node)

print(answer)

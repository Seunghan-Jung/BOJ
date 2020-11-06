import sys

sys.stdin = open('input.txt')

from collections import deque

input = sys.stdin.readline


def solve():
    V, E = map(int, input().split())

    K = int(input()) - 1

    adj = [{} for _ in range(V)]
    for _ in range(E):
        u, v, w = map(int, input().split())

        u -= 1
        v -= 1

        if v in adj[u]:
            adj[u][v] = min(adj[u][v], w)
        else:
            adj[u][v] = w

    min_dist = [float('inf')] * V
    min_dist[K] = 0
    q = deque([K])

    while q:

        cur = q.popleft()

        for next_node, weight in adj[cur].items():
            new_dist = min_dist[cur] + weight
            if new_dist < min_dist[next_node]:
                min_dist[next_node] = new_dist
                q.append(next_node)

    for v in range(V):
        if min_dist[v] < float('inf'):
            print(min_dist[v])
        else:
            print('INF')


if __name__ == '__main__':
    solve()

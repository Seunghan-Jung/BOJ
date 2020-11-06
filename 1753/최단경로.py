import sys

sys.stdin = open('input.txt')

from heapq import heappop, heappush

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
    H = [(0, K)]

    while H:

        dist, cur_node = heappop(H)

        if dist > min_dist[cur_node]:
            continue

        for adj_node, weight in adj[cur_node].items():
            new_dist = dist + weight
            if new_dist < min_dist[adj_node]:
                min_dist[adj_node] = new_dist
                heappush(H, (new_dist, adj_node))

    print('\n'.join(str(min_dist[v]) if min_dist[v] != float('inf') else 'INF' for v in range(V)))


if __name__ == '__main__':
    solve()

import sys

sys.stdin = open('input.txt')

from heapq import *

input = sys.stdin.readline


def dijkstra(adj, start, end):
    H = [(0, start)]
    min_cost = [float('inf')] * N
    min_cost[start] = 0

    while H:
        cur_cost, cur = heappop(H)

        if cur_cost > min_cost[cur]:
            continue

        for adj_node, cost in adj[cur]:

            new_cost = cur_cost + cost

            if new_cost < min_cost[adj_node]:
                min_cost[adj_node] = new_cost
                heappush(H, (new_cost, adj_node))

    return min_cost[end]


if __name__ == '__main__':
    N = int(input())
    M = int(input())

    adj = [[] for _ in range(N)]

    for _ in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1

        adj[a].append((b, c))

    start, end = map(lambda x: int(x) - 1, input().split())
    answer = dijkstra(adj, start, end)

    print(answer)

import sys
sys.stdin = open('input.txt')

from heapq import *

input = sys.stdin.readline

if __name__ == '__main__':
    N, M, K = map(int, input().split())

    edges = set()

    for m in range(1, M+1):
        x, y = map(int, input().split())
        edges.add((x, y, m))

    fail = False

    result = []
    for k in range(K):
        belongs_to = {}
        mst_edges = []
        total = 0
        cnt = N
        if fail:
            result.append(0)
            continue

        edge_list = sorted(edges, key=lambda edge: edge[2])
        for edge in edge_list:
            x, y, m = edge

            X = belongs_to.setdefault(x, {x})
            Y = belongs_to.setdefault(y, {y})

            if X is Y:
                continue

            if len(X) < len(Y):
                X, Y = Y, X

            X.update(Y)

            for y in Y:
                belongs_to[y] = X

            heappush(mst_edges, (m, x, y))
            total += m
            cnt -= 1
            if len(mst_edges) == N - 1:
                break

        if cnt != 1:
            result.append(0)
            fail = True
        else:
            result.append(total)
            m, x, y = heappop(mst_edges)

            edges.remove((x, y, m))

            total = 0

    print(*result)
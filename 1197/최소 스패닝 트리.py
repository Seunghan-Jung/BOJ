import sys
import heapq

sys.stdin = open('input.txt')

input = sys.stdin.readline


def MST():
    total = 0
    mst = set()

    min_val = [float('inf')] * V
    min_val[0] = 0

    H = [(0, 0)]
    while len(mst) < V:
        val, next = heapq.heappop(H)

        if min_val[next] < val:
            continue

        mst.add(next)
        total += val

        for node, val in adj[next]:
            if node in mst:
                continue

            if min_val[node] > val:
                min_val[node] = val
                heapq.heappush(H, (val, node))

    return total


if __name__ == '__main__':

    V, E = map(int, input().split())
    adj = [[] for _ in range(V)]

    for _ in range(E):
        a, b, val = map(int, input().split())
        a -= 1
        b -= 1

        adj[a].append((b, val))
        adj[b].append((a, val))

    answer = MST()

    print(answer)

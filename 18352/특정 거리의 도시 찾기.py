import sys

sys.stdin = open('input.txt')

from collections import deque

input = sys.stdin.readline


def solution():
    N, M, K, X = map(int, input().split())
    X = X - 1
    adj = [[] for _ in range(N)]

    for m in range(M):
        u, v = map(lambda x: int(x) - 1, input().split())
        adj[u].append(v)

    dist = [float('inf')] * N
    q = deque([X])
    dist[X] = 0
    d = 0

    while q:
        d += 1
        for _ in range(len(q)):
            cur = q.popleft()
            for next in adj[cur]:
                if dist[next] == float('inf'):
                    q.append(next)
                    dist[next] = d

    answer = [u + 1 for u in range(N) if dist[u] == K]
    print('\n'.join(map(str, answer)) if answer else -1)


if __name__ == '__main__':
    solution()

import sys
sys.stdin = open('input.txt')

from collections import deque

input = sys.stdin.readline

a, b = map(lambda x: int(x) - 1, input().split())

N, M = map(int, input().split())

adj = [[] for _ in range(N)]

for m in range(M):
    u, v = map(lambda x: int(x) - 1, input().split())
    adj[u].append(v)
    adj[v].append(u)

q = deque([a])
visit = [False] * N
visit[a] = True
d = 0

while q:

    for _ in range(len(q)):
        cur = q.popleft()
        if cur == b:
            print(d)
            exit()
        for next in adj[cur]:
            if not visit[next]:
                q.append(next)
                visit[next] = True
    d += 1

print(-1)

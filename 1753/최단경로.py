import sys
sys.stdin = open('input.txt')

import heapq

V, E = map(int, input().split())

K = int(input())

adj = [[] for _ in range(V)]

for _ in range(E):
    u, v, w = map(int, input().split())
    u, v = u - 1, v - 1
    adj[u].append((v, w))

visited = [False] * V

dist = [float('inf')] * V
dist[K] = 0
heap = [(0, K)]
cnt = 0
while cnt < V:

    for n, w, in adj[K]:

        dist[n] = min(dist[K] + w, dist[n])

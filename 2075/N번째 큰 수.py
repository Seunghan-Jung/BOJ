import sys
sys.stdin = open('input.txt')

N = int(input())

h = []
for n in range(N):
    li = map(int, input().split())
    h.extend(li)
    h = sorted(h, reverse=True)[:N]

print(min(h))


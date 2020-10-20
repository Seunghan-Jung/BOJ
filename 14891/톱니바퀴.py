import sys

sys.stdin = open('input.txt')

right = 1
left = -1
r = 2
l = 6


def rotate(n, direction, flow):
    if n < 0 or n >= 4:
        return

    if flow == left and P[n][r] != P[n + right][l]:
        rotate(n + flow, -direction, flow)
    elif flow == right and P[n][l] != P[n + left][r]:
        rotate(n + flow, -direction, flow)
    else:
        return

    P[n] = P[n][-direction:] + P[n][:-direction]


P = [[*map(int, input())] for _ in range(4)]
K = int(input())

for k in range(K):
    n, direction = map(int, input().split())
    n -= 1

    rotate(n + 1, -direction, right)
    rotate(n - 1, -direction, left)
    P[n] = P[n][-direction:] + P[n][:-direction]

score = sum(P[n][0] * 2 ** n for n in range(4))

print(score)

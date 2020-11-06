import sys

sys.stdin = open('input.txt')

from math import *

B, C, D = map(int, input().split())

A1, A2 = map(int, input().split())
E1, E2 = map(int, input().split())

min_y = floor(A1 * C / A2) + 1
max_y = ceil(C * E1 / E2) - 1

min_X = floor(A1 * B / A2) + 1
max_Z = ceil(E1 * D / E2) - 1

answer = 0

for Y in range(min_y, max_y + 1):
    max_X = ceil(B * Y / C) - 1
    min_Z = floor(D * Y / C) + 1

    answer += (max_X - min_X + 1) * (max_Z - min_Z + 1)

print(answer)
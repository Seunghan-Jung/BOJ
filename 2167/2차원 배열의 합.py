import sys

sys.stdin = open('input.txt')
from itertools import *

input = sys.stdin.readline

N, M = map(int, input().split())

psum = [chain([0], accumulate(map(int, input().split()))) for n in range(N)]
psum = [chain([0], accumulate(col)) for col in zip(*psum)]
psum = [*zip(*psum)]

print(psum)
K = int(input())


def query(K):
    for _ in range(K):
        yield map(lambda x: int(x) - 1, input().split())


print('\n'.join(map(str, (psum[x + 1][y + 1] - psum[x + 1][j] - psum[i][y + 1] + psum[i][j] for i, j, x, y in query(K)))))

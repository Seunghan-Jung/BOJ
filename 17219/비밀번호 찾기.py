import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline


def solve():
    N, M = map(int, input().split())
    d = dict(input().split() for _ in [0] * N)
    print('\n'.join(d[input().rstrip()] for _ in [0] * M))


if __name__ == '__main__':
    solve()

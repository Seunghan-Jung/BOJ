import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline


def solve():
    N, M = map(int, input().split())

    belongs_to = {}

    result = []
    for m in range(M):
        order, a, b = map(int, input().split())
        A = belongs_to.get(a, [a])
        B = belongs_to.get(b, [b])

        if order == 0:
            if A is B or a == b:
                continue

            if len(A) < len(B):
                A, B = B, A

            A += B

            for b in B:
                belongs_to[b] = A

            belongs_to[a] = A

        else:
            if A is B or a == b:
                result.append('YES')
            else:
                result.append('NO')

    return '\n'.join(result)


if __name__ == '__main__':
    answer = solve()
    print(answer)

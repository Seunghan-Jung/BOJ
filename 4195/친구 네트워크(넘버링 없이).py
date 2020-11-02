import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline


def solve():
    F = int(input())

    belongs_to = {}

    result = []
    for f in range(F):
        a, b = input().split()

        A = belongs_to.get(a, [a])
        B = belongs_to.get(b, [b])

        if A is B:
            result.append(len(A))
        else:
            if len(A) < len(B):
                A, B = B, A
            A += B

            for b in B:
                belongs_to[b] = A

            belongs_to[a] = A
            result.append(len(A))

    return result


if __name__ == '__main__':
    T = int(input())

    for t in range(T):

        answer = solve()

        print('\n'.join(map(str, answer)))

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline


def solve():
    F = int(input())

    numbering = {}
    number = 0
    belongs_to = {}

    result = []
    for f in range(F):
        a, b = input().split()

        if a not in numbering:
            numbering[a] = number
            number += 1
        if b not in numbering:
            numbering[b] = number
            number += 1

        a, b = numbering[a], numbering[b]

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

    return '\n'.join(map(str, result))


if __name__ == '__main__':
    T = int(input())

    for t in range(T):

        answer = solve()

        print(answer)

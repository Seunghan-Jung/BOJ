import sys
from collections import namedtuple

sys.stdin = open('input.txt')
input = sys.stdin.readline

Point = namedtuple('Point', ('x', 'y'))
Line = namedtuple('Line', ('P', 'Q'))


def solve():
    def ccw(P1: Point, P2: Point, P3: Point):
        x1, y1 = P1
        x2, y2 = P2
        x3, y3 = P3

        return (x1 * y2 + x2 * y3 + x3 * y1) - (y1 * x2 + y2 * x3 + y3 * x1)

    def is_cross(L: Line, M: Line):
        A = ccw(L.P, L.Q, M.P) * ccw(L.P, L.Q, M.Q)
        B = ccw(M.P, M.Q, L.P) * ccw(M.P, M.Q, L.Q)

        if A == 0 and B == 0:
            return M.P <= L.Q and L.P <= M.Q

        return A <= 0 and B <= 0

    N = int(input())

    lines = []
    belongs_to = {}

    for _ in range(N):

        x1, y1, x2, y2 = tuple(map(int, input().split()))

        P = Point(x1, y1)
        Q = Point(x2, y2)
        if P > Q:
            P, Q = Q, P

        a = Line(P, Q)

        belongs_to[a] = [a]

        for b in lines:

            if is_cross(a, b):
                A = belongs_to[a]
                B = belongs_to[b]

                if A is B:
                    continue

                if len(A) < len(B):
                    A, B = B, A

                A += B
                belongs_to[a] = A
                belongs_to[b] = A
                for b in B:
                    belongs_to[b] = A

        lines.append(a)

    count = len(set(map(id, belongs_to.values())))
    max_size = len(max(belongs_to.values(), key=len))

    return count, max_size


if __name__ == '__main__':
    C, S = solve()

    print(C, S, sep='\n')

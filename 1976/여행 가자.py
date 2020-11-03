import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())
M = int(input())

adj_matrix = [[*map(int, input().split())] for n in range(N)]

travel = [*map(lambda x: int(x) - 1, input().split())]

belongs_to = {}

for i in range(N):
    for j in range(i + 1, N):
        if adj_matrix[i][j] == 1:
            I = belongs_to.get(i, [i])
            J = belongs_to.get(j, [j])

            if I is J:
                continue

            if len(I) < len(J):
                I, J = J, I

            I += J

            belongs_to[i] = I

            for k in J:
                belongs_to[k] = I

T = belongs_to.get(travel[0], [travel[0]])

for t in travel:
    if t not in T:
        print('NO')
        break
else:
    print('YES')

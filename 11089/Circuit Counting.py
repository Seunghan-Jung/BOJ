import sys

sys.stdin = open('input.txt')


def subset(vectors):
    subsets = set()

    def dfs(n, N, cur):
        subsets.add(tuple(cur))

        if n == N:
            return

        for i in range(n, N):
            cur.append(vectors[i])
            dfs(i + 1, N, cur)
            cur.pop()

    dfs(0, len(vectors), [])

    result = {}

    for subset in subsets:
        temp = [0, 0]
        for vector in subset:
            temp[0] += vector[0]
            temp[1] += vector[1]

        temp = tuple(temp)
        result[temp] = result.get(temp, 0) + 1

    return result


N = int(input())

vectors = [tuple(map(int, input().split())) for _ in range(N)]

A_vectors = vectors[:N // 2]
B_vectors = vectors[N // 2:]

A = subset(A_vectors)
B = subset(B_vectors)

count = 0

for a in A:
    temp = (-a[0], -a[1])
    count += B.get(temp, 0) * A[a]

count -= 1

print(count)

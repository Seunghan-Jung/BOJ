import sys
sys.stdin = open('input.txt')

B, C, D = map(int, input().split())

A1, A2 = map(int, input().split())

E1, E2 = map(int, input().split())

x = A1 * B // A2 + 1

z = D * E1 // E2 - 1

X = [0] * 1000001
Y = [0] * 1000001

for k in range(x, ):
    X[C * k // B] += 1

for k in range(x, z + 1):

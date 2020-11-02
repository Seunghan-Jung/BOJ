import sys
sys.stdin = open('input.txt')

from bisect import bisect

def LIS(s):
    temp = []

    for n in s:
        i = bisect(temp, n)
        if len(temp) == i:
            temp.append(n)
        else:
            temp[i] = n

    return len(s) - len(temp)

N = int(input())
sequence = [*map(int, input().split())]

answer = LIS(sequence)

print(answer)
import sys
sys.stdin = open('input.txt')
import string
N = int(input())

_36_to_deci = {h: deci for deci, h in enumerate(string.digits + string.ascii_uppercase)}
deci_to_36 = {deci: h for deci, h in enumerate(string.digits + string.ascii_uppercase)}

count = {deci: 0 for deci in range(36)}

sum = 0
for n in range(N):
    num = input()[::-1]
    for i in range(len(num)):
        count[_36_to_deci[num[i]]] += 36 ** i

K = int(input())

sorted_list = [*sorted(count.items(), key=lambda x: (35 - x[0]) * x[1], reverse=True)]

for k in range(K):
    sum += _36_to_deci['Z'] * sorted_list[k][1]

for k in range(K, 36):
    sum += sorted_list[k][0] * sorted_list[k][1]

answer = []

if sum == 0:
    print(0)
else:
    while sum:
        answer.append(deci_to_36[sum % 36])
        sum //= 36

    print(''.join(reversed(answer)))






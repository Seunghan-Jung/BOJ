import sys

sys.stdin = open('input.txt')


class B:
    def __init__(self, color):
        self.color = color


def rotate(plane, d):
    colors = [[plane[i][j].color for j in range(3)] for i in range(3)]
    if d == '+':
        for i in range(3):
            for j in range(3):
                plane[j][2 - i].color = colors[i][j]
    else:
        for i in range(3):
            for j in range(3):
                plane[2 - j][i].color = colors[i][j]


T = int(input())

for _ in range(1, T + 1):
    n = int(input())
    o = input().split()

    cube = {
        plane: [[B(color) for _ in range(3)] for _ in range(3)] for plane, color in
        (('U', 'w'), ('D', 'y'), ('F', 'r'), ('B', 'o'), ('L', 'g'), ('R', 'b'))}

    rotation = {
        'U': cube['B'][2][:] + [cube[plane][0][i] for plane in ('R', 'F', 'L') for i in range(2, -1, -1)],
        'D': cube['B'][0][::-1] + [cube[plane][2][i] for plane in ('L', 'F', 'R') for i in range(3)],
        'R': [cube[plane][i][2] for plane in ('U', 'B', 'D', 'F') for i in range(2, -1, -1)],
        'L': [cube[plane][i][0] for plane in ('U', 'F', 'D', 'B') for i in range(3)],
        'F': cube['U'][2][:] + [cube['R'][i][0] for i in range(3)] + cube['D'][0][::-1] + [cube['L'][i][2] for i in
                                                                                           range(2, -1, -1)],
        'B': cube['U'][0][::-1] + [cube['L'][i][0] for i in range(3)] + cube['D'][2][::] + [cube['R'][i][2] for i in
                                                                                            range(2, -1, -1)],
    }

    for plane, d in o:
        p = cube[plane]
        l = rotation[plane]
        rotate(p, d)
        colors = [b.color for b in l]

        if d == '+':
            colors[:] = colors[-3:] + colors[:-3]
        else:
            colors[:] = colors[3:] + colors[:3]

        for i in range(12):
            l[i].color = colors[i]

    for i in range(3):
        for j in range(3):
            print(cube['U'][i][j].color, end='')
        print()

from math import sin

a = 20
omega = 0.1
phi = 0

for t in range(1000):
    pos = int(a*sin(omega*t+phi))
    if pos < 0:
        print(' '*(20+pos), '*'*(-pos))
    else:
        print(' '*20, '*'*pos)
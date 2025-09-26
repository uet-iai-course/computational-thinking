a, b, c = input("Nhập 3 hệ số (a, b, c): ").split()
a, b, c, = float(a), float(b), float(c)

delta = b**2 - 4*a*c
x1 = (-b + delta**0.5)/(2*a)
x2 = (-b - delta**0.5)/(2*a)
print("x1 = {:.4f} x2 = {:.8f}".format(x1, x2))

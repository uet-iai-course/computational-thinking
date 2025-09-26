a, b, c = input("Nhập 3 cạnh: ").split()
a, b, c = float(a), float(b), float(c)

half = (a+b+c)/2
area = (half*(half-a)*(half-b)*(half-c))**0.5 # heron formula

print("Area = {:.6f}".format(area))
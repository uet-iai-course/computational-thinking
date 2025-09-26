from math import log

rate = input("Nhập khoản lãi suất: ")
rate = float(rate)

n_year = log(2.0, 1 + rate/100)

print("Sau {:.1f} năm sẽ x2".format(n_year))
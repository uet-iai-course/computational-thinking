deposit, rate, n_year = input("Nhập khoản tiết kiệm, lãi suất và số năm:").split()
deposit, rate, n_year = float(deposit), float(rate), float(n_year)

total = deposit*(1+rate/100)**n_year

print("Tổng tiền sau {:.1f} năm là {:.4f}".format(n_year, total))
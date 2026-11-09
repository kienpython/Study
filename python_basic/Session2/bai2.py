p = float(input("Số tiền gửi: "))
r = float(input("Lãi suất (%/năm): "))
n = int(input("Số năm: "))
total = p * (1 + r/100)**n
print(f"Sau 3 năm bạn có {total:.0f} đồng, tiền lãi {total-p:.0f} đồng.")
try:
    so_a = float(input("Nhập a: "))
    so_b = float(input("Nhập b: "))
    print(f"{so_a} + {so_b} = {so_a + so_b}")
    print(f"{so_a} - {so_b} = {so_a - so_b}")
    print(f"{so_a} * {so_b} = {so_a * so_b}")
    print(f"{so_a} / {so_b} = {so_a / so_b}")
    print(f"{so_a} % {so_b} = {so_a % so_b}")
    print(f"{so_a} // {so_b} = {so_a // so_b}")
except:
    print("Số a hoặc số b không hợp lệ!")
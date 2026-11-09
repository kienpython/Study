import string
import random

n = int(input("Nhập vào độ dài mật khẩu: "))
password = string.ascii_letters + string.digits
print(password)
print("".join(random.choice(password) for _ in range(n)))

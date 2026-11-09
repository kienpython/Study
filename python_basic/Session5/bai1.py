raw_name = input("Nhập vào họ và tên: ")
normalized_name = raw_name.lower().title().strip()
last_name = normalized_name.split()[0]
middle_name = " ".join(normalized_name.split()[1:-1])
first_name = normalized_name.split()[-1]
print(f"Họ: {last_name}")
print(f"Tên đệm: {middle_name}")
print(f"Tên: {first_name}")
print(f"Tên viết tắt: {".".join([name[0] for name in normalized_name.split()])}")


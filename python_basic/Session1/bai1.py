name = input("Bạn tên gì? ")
try:
    birth_year = int(input("Bạn sinh năm nào? "))
    year_now = 2026
    print(f"Xin chào {name}! Năm {year_now} bạn {year_now-birth_year} tuổi.")
except:
    print("Năm sinh không hợp lệ!")
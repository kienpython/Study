from pathlib import Path
import json
import csv

def fill_info():
    name = input("Mời bạn nhập vào tên: ")
    phone_number = input("Mời bạn nhập vào số điện thoại: ")
    email = input("Mời bạn nhập vào email: ")
    return name, phone_number, email

def read_info(FILE:Path):
    if not FILE.exists():
        return []
    with open(FILE, mode="r" ,encoding="utf-8") as f:
        return json.load(f)

def get_info(FILE):
    email = input("Mời bạn nhập vào email muốn tìm: ")
    info = read_info(FILE)
    # print(info)
    if not info:
        print("Hiện tại đang không có dữ liệu!")
        return []
    finded = [data for data in info if data['Email'] == email]
    if not finded:
        print(f"Không tìm thấy thông tin của email {email}!")
        return []
    return finded[0], info

def find_by_email(FILE):
    finded, info = get_info(FILE)
    if not finded:
        return
    print(f"{'Name':<20} | {'Phone Number':<12} | {'Email':<20}")
    print(f"{finded['Name']:<20} | {finded['Phone Number']:<12} | {finded['Email']:<20}")

def delete_by_email(FILE):
    finded, info = get_info(FILE)
    if not finded:
        return
    info.remove(finded)
    update_file_json(FILE, info)
    print(f"Đã xóa thành công user có email là {finded['Email']}")

def update_file_json(FILE: Path, info_data):
    with open(FILE, "w", encoding='utf-8') as f:
        json.dump(info_data, f, ensure_ascii=False, indent=2)

def export_file_csv(FILE:Path):
    info_data = read_info(FILE)
    with open("danh_ba.csv", 'w', encoding='utf-8', newline="") as f:
        writer = csv.DictWriter(f, fieldnames=['Name', "Phone Number", "Email"])
        writer.writeheader()
        writer.writerows(info_data)
        print("Export file danh_ba.csv thành công!")

def add_info(FILE:Path, name, phone_number, email):
    info_data = read_info(FILE)
    info_data.append({
        "Name": name,
        "Phone Number": phone_number,
        "Email": email
    })
    update_file_json(FILE, info_data)
        


FILE = Path("danh_ba.json")
def main():
    while True:
        print("="*40)
        choice = input("""1. Thêm liên hệ
2. Tìm theo email
3. Xóa liên hệ theo email
4. Xuất toàn bộ ra file danh_ba.csv
0. Thoát
Vui lòng nhập vào lựa chọn của bạn: """)
        print("="*40)
        if choice == "1":
            name, phone_number, email = fill_info()
            add_info(FILE, name, phone_number, email)
        elif choice == "2":
            find_by_email(FILE)
        elif choice == "3":
            delete_by_email(FILE)
        elif choice == "4":
            export_file_csv(FILE)
        elif choice == "0":
            break
        else:
            print("Vui lòng chọn chức năng từ 0 đến 4!")

if __name__ == "__main__":
    main()
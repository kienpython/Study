
students = [("Kiên", 10), ("Hoàn", 7), ("Lê", 3)]


while True:
    print("==========================================")
    choice = input("""1. Thêm điểm
2. Xem danh sách
3. Thống kê (cao nhất, thấp nhất, trung bình)
4. Xóa điểm theo vị trí
5. Sắp xếp giảm dần
0. Thoát
Vui lòng nhập vào lựa chọn của bạn: """)
    print("==========================================")

    if choice == "1":
        student = tuple(input("Nhập vào thông tin sinh viên (name, điểm), VD: Kiên, 10: ").split(", "))
        students.append(student)
    elif choice == "2":
        print(f'STT | {"Họ và tên":<25} | {"Điểm":<20}')
        stt = 0
        for student in students:
            stt += 1
            print(f"{stt} | {student[0]:<25} | {student[1]:<20}")
    elif choice == "3":
        top_student = students[0]
        lowest_student = students[0]
        average_score = 0
        total_score = 0
        for student in students:
            if student[1] > top_student[1]:
                top_student = student
            elif student[1] < lowest_student[1]:
                lowest_student = student
            total_score += student[1]
        average_score = total_score/len(students)
        print(f"Sinh viên có điểm cao nhất là: {top_student}")
        print(f"Sinh viên có điểm thấp nhất là: {lowest_student}")
        print(f"Điểm trung bình của cả lớp là {average_score}")
    elif choice == "4":
        student_stt = int(input("Nhập vào STT sinh viên muốn xóa: "))
        students.pop(student_stt+1)
    elif choice == "5":
        students = sorted(students, key=lambda s:s[1])
    elif choice == "0":
        break
    else:
        print("Vui lòng chọn chức năng từ (0-5)")
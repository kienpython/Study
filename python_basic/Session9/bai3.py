from datetime import datetime, date

n = input("Ngày sinh (dd/mm/yyyy): ")
ngay_sinh = datetime.strptime(n, "%d/%m/%Y").date()
hom_nay = date.today()
sinh_nhat = ngay_sinh.replace(year=hom_nay.year)
if sinh_nhat < hom_nay:
    sinh_nhat = sinh_nhat.replace(year=hom_nay.year+1)
thu = ["Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ năm", "Thứ sáu", "Thứ bảy", "Chủ nhật"]
print(f"Còn {(sinh_nhat-hom_nay).days} ngày đến sinh nhật!")
print(f"Bạn sinh vào {thu[ngay_sinh.weekday()]}")
def TB(l):
    t = 0
    for i in range(1, len(l)):
        t += l[i]
    return t / len(l)

def dem_dat(l):
    d = 0
    for x in l:
        if x > 5:
            d =+ 1
    return d

diem = input("Nhập điểm cách nhau bởi dấu cách: ").split()
print("Trung bình:", TB(diem))
print("Số học sinh đạt:", dem_dat(diem))
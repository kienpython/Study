raw_pharse = input('Nhập vào đoạn văn bạn muốn format: ')

for punctuation in ".,!?;:":
    raw_pharse = raw_pharse.replace(punctuation, "")
raw_pharse = raw_pharse.lower().split(" ")

count = {}
for word in raw_pharse:
    if word not in count:
        count[word] = 1
    else:
        count[word] += 1

list_pharse = sorted(count.items(), key= lambda item: item[1], reverse=True)[:5]
for key, value in list_pharse:
    print(f"{key} - {value}")

print(f'Số từ khác nhau là: {len(set(raw_pharse))}')


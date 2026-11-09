string = input("Nhập một câu: ")
print(f"Số từ là: {len(string.split(" "))}")
max_len_word = ""
for word in string.split(" "):
    if len(word) > len(max_len_word):
        max_len_word = word

print(f"Từ dài nhất là: {max_len_word}")
print(f"Câu sau khi đã format là: {string.strip().lower().title()}")

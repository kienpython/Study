import random

secret_number = random.randint(1,100)
while True:
    guess = int(input("Bạn đoán số (1-100): "))
    if guess > secret_number:
        print("Lớn hơn")
    elif guess < secret_number:
        print("Nhỏ hơn")
    else:
        print("Bạn đã đoán đúng rồi!")
        break
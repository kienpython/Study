weight = int(input("Cân nặng (kg): "))
height = int(input("Chiều cao (cm): "))

bmi = weight/(height/100)**2
print(f"BMI của bạn là {bmi:.1f}")
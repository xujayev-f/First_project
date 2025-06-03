# a = "5"
# b = 2
# print(a + b)  # TypeError: str va int qo‘shib bo‘lmaydi

# print(x)  # NameError: x o‘zgaruvchisi aniqlanmagan

# nums = [1, 2, 3]
# print(nums[5])  # IndexError: 5-chi indeks yo‘q

# student = {"name": "Ali"}
# print(student["age"])  # KeyError: age kaliti yo‘q


# try:
#     x = int(input("Son kiriting: "))
#     y = 10 / x
#     print("Natija:", y)
# except:
#     print("Xatolik yuz berdi.")

# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)    
# except:
#     print("Butun son kiritmadingiz")
# else:
#     print(f"Siz {2025-yosh} yilda tug'ilgansiz")

try:
    x = int(input("Son kiriting: "))
    print(10 / x)
except ZeroDivisionError:
    print("0 ga bo‘lish mumkin emas.")
except ValueError:
    print("Faqat son kiriting.")
else:
    print("Hammasi yaxshi ishladi.")
finally:
    print("Dastur yakunlandi.")


# def baho_ber(baho):
#     if baho < 1 or baho > 5:
#         raise ValueError("Baho 1 dan 5 gacha bo‘lishi kerak.")
#     print("Berilgan baho:", baho)

# baho_ber(6)  # ValueError: noto‘g‘ri baho

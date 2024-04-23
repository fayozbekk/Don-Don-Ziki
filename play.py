import random

tqq = ["tosh", "qaychi", "qog'oz"]
diyor = input("Diyorbek tosh, qaychi yoki qog'ozdan birini tanlang-->")
ai = random.choice(tqq)
print("Botning tanlovi:", ai)

if ai == diyor:
    print("Durrang😉")

elif (ai == "tosh" and diyor == "qaychi"
      or ai == "qaychi" and diyor == "qog'oz"
      or ai == "qog'oz" and diyor == "tosh"):
    print("Siz yutqazdingiz🤣")

elif (diyor == "tosh" and ai == "qaychi"
      or diyor == "qaychi" and ai == "qog'oz"
      or diyor == "qog'oz" and ai == "tosh"):
    print("Siz yutdingiz😏")
else:
    print("Bu ishora mavjud emas🧐")

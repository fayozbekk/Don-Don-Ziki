import random

tqq = ["tosh", "qaychi", "qog'oz"]
ali = input("Tosh, qaychi yoki qog'ozdan birini tanlang-->")
bot = random.choice(tqq)
print('Botning tanlovi->', bot)

if bot == ali:
    print('Durrang😉')

elif (bot == "tosh" and ali == "qaychi"
      or bot == "qaychi" and ali == "qog'oz"
      or bot == "qog'oz" and ali == "tosh"):
    print("Siz yutqazdingiz🤣")

elif (ali == "tosh" and bot == "qaychi"
      or ali == "qaychi" and bot == "qog'oz"
      or ali == "qog'oz" and bot == "tosh"):
    print("Siz yutdingiz😏")

else:
    print("---->Bunday buyruq yo'q🧐<----")

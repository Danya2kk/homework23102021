print("Привет, давай поиграем в поросячую латынь)")

suf1 = "way"
suf2 = "ay"
while True:
    word = input("Введи слово на английском(ЭТО ВАЖНО!!!) или нажмите q для выхода:  ")
    if word == 'q':
        break
    if word.startswith('a') or word.startswith('e') or word.startswith('i') \
            or word.startswith('u') or word.startswith('y') or word.startswith('o'):
         print(word[1:] + word[0] + suf1)
    else:
        print(word[1:] +word[0] + suf2)
    continue

print("Хорошего дня, пока!")






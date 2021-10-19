word = input("Введите слово: ")

vowels = ['a', 'e', 'i', 'o', 'u', 'y']
suf1 = "way"
if word == word.startswith('a', 'e', 'i') or word.startswith('o', 'u', 'y'):
    print(word[1:] + word[0] + suf1)

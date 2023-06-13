words = input("Enter a list of words separated by commas: ").split(",") # Введите список слов через запятую:
word_set = set(words)
print("Number of words:", len(words)) # Количество слов:
second_list = input("Enter a list of words with the same number of characters: ").split(",") # Введите список слов такого же количества символов:
dictionary = dict(zip(words, second_list))
print(dictionary)

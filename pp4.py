def count_words(text):
    # Разбиваем текст на слова и убираем пустые
    words = [word for word in text.split() if word]
    word_count = {}
    # Считаем частоту каждого слова
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

# Пример использования
text = "я люблю кодить и я люблю учиться"
result = count_words(text)
for word, count in result.items():
    print(f"Слово '{word}' встречается {count} раз")
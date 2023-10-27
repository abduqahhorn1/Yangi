def repeat_words(s):
    words = s.split()
    unique_words = set(words)
    repeat_words = []
    for word in unique_words:
        if words.count(word) > 1:
            repeat_words.append(word)
    return repeat_words
s = "bugun kunduz ko'p ko'p ko'p yaqinlashdi"
repeat = repeat_words(s)
print(repeat)
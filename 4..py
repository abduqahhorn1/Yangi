def MaxWord(lst):
    max_word = ""
    for word in lst:
        if len(word) > len(max_word):
            max_word = word
    return max_word

lst = ['Python', 'Java', 'JavaScript', 'C++', 'Ruby', 'PHP', 'Swift']

result = MaxWord(lst)
print(result)
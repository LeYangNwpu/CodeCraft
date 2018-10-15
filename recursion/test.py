
words_set = list()
def perm(word, left, right):
    # word is not empty
    if word:
        if word not in words_set:
            words_set.append(word)
        for i in range(left, right+1):
            word_temp = word[0:i] + word[i+1:]
            perm(word_temp, 0, len(word_temp)-1)

s = list('china')
perm(s, 0, len(s)-1)
print(words_set)

# judge whether each element in words_set is real word

def delete_leter(word, i):
	return word[:i]+word[i+1:]

word_collection = []
def remove_leter(word):
    if len(word) == 1:
        # print(word)
        return
    else:
        for i in range(len(word)):
            word_rem = delete_leter(word, i)
            if word_rem not in word_collection:
                word_collection.append(word_rem)
            # print(word_rem)
            remove_leter(word_rem)

def is_shamble(word):
    if len(word) == 1:
        return True
    else:
        for i in range(len(word)):
            word_left = delete_leter(word, i)
            # if word_left not in word_collection:
            #     word_collection.append(word_left)
            if word_left in WordDict.item():
                print(word_left)
                is_shamble(word_left)
    return False

remove_leter('china')
print(word_collection)
print(len(word_collection))


def delete_cha(s, n):
    return s[:n] + s[n + 1:]

data_collection = []

def remove_cha(s):
    # print(s)
    if len(s) == 1:
        return s
    else:
        i = 0
        while i < len(s):
            temp = delete_cha(s, i)
            if temp not in data_collection:
                data_collection.append(temp)
            print(temp)
            i += 1
        if len(s) >= 2:
            remove_cha(s[1:])

s = 'china'
remove_cha(s)
print(data_collection)

arr = [1,8,3,2,7,4,5,6]
ind = [1,2,3,4,5,6,7,8]
sort_ind = [arr.index(x) for x in sorted(arr)]
ind_new = []
for order in sort_ind:
    ind_new.append(ind[order])

print(sort_ind)
print(ind_new)

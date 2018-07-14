def get_next_array(arr):
	value = 1
	for ilen in range(1, len(arr)):
		fore_prex = arr[:ilen]
		back_prex = arr[len(arr)-ilen:]
		if fore_prex == back_prex:
			value = ilen + 1
	return value

def get_next(array):
	next_array = [0] * len(array)
	for iarr in range(1, len(array)):
		next_array[iarr] = get_next_array(array[:iarr])
	return next_array

# a = 'abcabx'
# print(get_next(a))

str_pri = 'ABABABCABABABCABABABC'
str_tar = 'ABABAC'
next_val = get_next(str_tar)

jtar = 0
ipri = 0
while ipri < len(str_pri):
    if str_pri[ipri] == str_tar[jtar]:
        if jtar == len(str_tar) - 1:
            print('match at the place %d : %d' % (ipri - len(str_tar) + 1, ipri))
            jtar = 0
        else:
            ipri += 1
            jtar += 1
            continue
    else:
        ipri += 1
        jtar = next_val[jtar]






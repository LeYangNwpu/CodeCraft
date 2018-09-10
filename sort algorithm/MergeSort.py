def Merge(SR, TR, i, m, n):
	j = m + 1
	k = i
	while True:
		if (i > m) or (j > n):
			break
		if (SR[i-1] < SR[j-1]):
			TR[k-1] = SR[i-1]
			i += 1
		else:
			TR[k-1] = SR[j-1]
			j += 1
	if (i <= m):
		for l in range(m-i+1):
			TR[k+l-1] = SR[i+l-1]
	if (j <= n):
		for l in range(n-j+1):
			TR[k+l-1] = SR[j+l-1]
	return TR

def Msort(SR, TR1, s, t):
	# MAXSIZE = 11
	TR2 = [0] * 11
	if s == t:
		# change
		# print('reach here')
		# print(type(s))
		# print(s-1)
		TR1[s-1] = SR[s-1]
	else:
		m = int((s+t)/2)
		Msort(SR, TR2, s, m)
		Msort(SR, TR2, m+1, t)
		TR1 = Merge(TR2, TR1, s, m, t)
		print('sort result:')
		print(TR1)

def MergeSort(L):
	return Msort(L, L, 1, len(L))

SR = [0, 50, 10, 90, 30, 70, 40, 80, 60, 20]
result = MergeSort(SR)
print(result)



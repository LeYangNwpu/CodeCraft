def is_possible(max_hack, order):
	num = 0
	for s in order:
		if s == 'S':
			num += 1
	return num <= max_hack

def cal_hack(order):
	num = 0
	length = 1
	for cha in order:
		if cha == 'C':
			length *= 2
		else:
			num += length
	return num

def adjust_order(order):
	for i in range(len(order)-1, 0, -1):
		if order[i] == 'S' and order[i-1] == 'C':
			order[i], order[i-1] = order[i-1], order[i]
			break
	return order

def save_universe(max_hack, order):
	# check whether possible
	if not is_possible(max_hack, order):
		print('IMPOSSIBLE')
		return -1
	step = 0
	# calculate hack number for a given order
	cur_hack = cal_hack(order)
	while cur_hack > max_hack:
		# adjust the last 'CS' to 'SC'
		order = adjust_order(order)
		step += 1
		cur_hack = cal_hack(order)
	return step


max_hack = 3
order = list('CSCSS')
result = save_universe(max_hack, order)
print(result)




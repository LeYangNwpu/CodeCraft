'''
Problem:
	two number sum problem
Requires:
	use hash table to judge whether existing a desired value
	no need to dispose conflict
Ways:

'''

import numpy as np

MOD = 100
NULLVALUE = -32768

def hash(value):
	return value % MOD

def insert_hash(hash_table, value):
	add = hash(value)
	if hash_table[add] != NULLVALUE:
		print('key conflict')
		return
	hash_table[add] = value

def search_hash(hash_table, value):
	add = hash(value)
	if hash_table[0, add] == NULLVALUE:
		print('value %d not found' % value)
	return add

data = np.array([3, 5, 2, 8, 11, 13, 4])
sum = 7
pos_hash_table = np.ones(100) * NULLVALUE

proper_pairs = []
for idata in data:
	factor_another = sum - idata
	add = hash(factor_another)
	if pos_hash_table[add] != NULLVALUE:
		proper_pairs.append([idata, factor_another])
	else:
		insert_hash(pos_hash_table, idata)

print(proper_pairs)

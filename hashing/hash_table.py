import numpy as np

MOD = 12
NULLKEY = -32768

def Hash(key):
	return key % MOD

def InsertHash(HashTable, key):
	addr = Hash(key)
	while HashTable[addr] != NULLKEY:
		addr = (addr + 1) % MOD
	HashTable[addr] = key

def SearchHash(HashTable, key):
	addr = Hash(key)
	addr_begin = addr
	while HashTable[addr] != key:
		addr = addr+1 % MOD
		if (HashTable[addr] == NULLKEY) or (addr == addr_begin):
			return False
	return addr

data = np.array([12, 67, 56, 16, 25, 37, 22, 29, 15, 47, 48, 34])
HashTable = np.ones((1, 12)) * NULLKEY
for i in range(data.size[1]):
	InsertHash(HashTable, data[0, i])
print(HashTable)
for i in range(data.size[1]):
	addr = SearchHash(HashTable, data[0, i])
	print(addr)




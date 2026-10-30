tuple1 = ('周杰伦',11,['football','music'])
q = tuple1.index(11)
print(q)
b = tuple1[0]
print(b)
del tuple1[2][0]
print(tuple1)
tuple1[2].append('coding')
print(tuple1)

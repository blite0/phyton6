f = open('roma.txt', 'r')
for i in f:
	num = i.split()
	x = int(num[0])
	y = int(num[1])
	z = int(num[2])
	res = open('result.txt', 'a')
	res.write('Значение для:\n')
	res.write(i)
	for _ in range(1, z+1):
		if _%x==0 and _%y==0:
			res.write('FB\n')
		elif _%x==0:
			res.write('F\n')
		elif _%y==0:
			res.write('B\n')
		else:
			res.write(str(_) + str('\n'))
f.close()
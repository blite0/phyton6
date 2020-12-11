f = open("3_3.py", 'r')
print(f.read()[::-1])
print ("Hello world") 
for line in f: 
	print(line, end = "")
f.close()
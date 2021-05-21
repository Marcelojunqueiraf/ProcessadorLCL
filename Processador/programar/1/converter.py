mhs = []
lhs = []
while True:
	a = input()
	if a == "s":
		break
	a = a.split()
	mhs.append(a[0][2:])
	lhs.append(a[1])


f = open("lhs.drs", "w")
f.write("#A 0000h\n#H")
for c in lhs:
	f.write(f"{c} ")
f.write("\r\n")
f.close()

f = open("mhs.drs", "w")
f.write("#A 0000h\n#H")
for c in mhs:
	f.write(f"{c} ")
f.write("\r\n")
f.close()


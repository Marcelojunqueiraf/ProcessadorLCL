opCode = {"addi":"0", "subi":"1", "andi":"2", "oi":"3", "xoi":"4", "beq":"5", "bleu":"6", "bles":"7"}
padrao = "#R ROM4Kx16, id 0001\n#- Deeds Rom Source Format (*.drs)\n\n#A 0000h\n#H\n"
lsh = padrao
msh = padrao
while True:
	inst = input()
	inst = inst.lower()
	if inst == "s":
		break
	inst = inst.replace("r", "").replace(","," ")
	inst = inst.split()
	op = opCode[inst[0]]
	if int(op) >= 5: #branch
		rd = 0
		ra = int(inst[1])
		rb = int(inst[2])
		imm = int(inst[3])
		if imm < 0:
			imm = (-imm ^ 0xffff)+0x1
		lsh +=  hex(rd)[2:] + hex(ra)[2:] + hex(rb)[2:] + op + " "
		msh += hex(imm)[2:].zfill(4) + " "
	else:
		rd = int(inst[1])
		ra = int(inst[2])
		rb = int(inst[3])
		imm = int(inst[4])
		if imm < 0:
			imm = (-imm ^ 0xffff)+0x1
		lsh +=  hex(rd)[2:] + hex(ra)[2:] + hex(rb)[2:] + op + " "
		msh += hex(imm)[2:].zfill(4) + " "

f = open("lsh.drs", "w")
f.write(lsh)
f.close()

f = open("msh.drs", "w")
f.write(msh)
f.close()


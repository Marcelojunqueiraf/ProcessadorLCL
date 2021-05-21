
opCode = {"addi":"0000", "subi":"0001", "andi":"0010", "oi":"0011", "xoi":"0100", "beq":"0101", "bleu":"0110", "bles":"0111"}

while True:
	inst = input()
	if inst == "stop":
		break
	inst = inst.replace("r", "").replace(",","")
	inst = inst.split()
	op = opCode[inst[0]]
	rd = int(inst[1])
	ra = int(inst[2])
	rb = int(inst[3])
	imm = int(inst[4])
	print("op:"+op, "ra:"+str(ra), "rb:"+str(rb), "rd:"+str(rd), "imm:"+str(imm))
	result =  bin(rd)[2:].zfill(4) + bin(ra)[2:].zfill(4) + bin(rb)[2:].zfill(4) + op
	print(result)
	print(bin(imm)[2:].zfill(16))

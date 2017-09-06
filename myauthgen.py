def my_hash2(s=""):
	sbits = s.encode()
	i = 0
	j = 0
	if len(sbits) > 20:
		h_bits = [0]*20
		for c in sbits:
			h_bits[i%len(h_bits)] += ((c + i)**2)
			h_bits[i%len(h_bits)] =  h_bits[i%len(h_bits)]%240 + 16
			i += 1
	else:
		h_bits = [0]*len(sbits)
		for c in sbits:
			h_bits[i] = ((c + i)**2)
			h_bits[i] = h_bits[i]%240 + 16
			i += 1

	h_string = ""
	for h in h_bits:
		h_string += '{0:x}'.format(h)
	if len(s) < 20:
		h_string = my_hash2(h_string)
	return h_string
	
f = open(input("Enter in file name: "), 'w')
while 1:
	username = input("input username: ")
	if username == "stop":
		break
	password = input("input password: ")
	password = my_hash2(password)
	f.write(username + ' ' + password + '\n')
	
f.close()
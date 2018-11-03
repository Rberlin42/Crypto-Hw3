import sys
import math

#Global parameters
p = 499
q = 547
a = -57
b = 52

# Modular exponentiation to work with large numbers
# x^y mod n
def modexp(x, y, n):
	if y==0:
	    return 1
	z = modexp(x, int(y/2), n)
	if y%2 == 0:
	    return (z**2) % n
	else:
	    return (x*(z**2)) % n

# Encrypt a plaintext using the Blum Goldwater Probabilistic Encryption Algorithm
# uses the global parameters p, q, a, b, and X
# returns a tuple for the cyphertext (C, X_t+1)
def encrypt(m, n, seed):

	#compute k, h, and t
	k = int(math.log(n, 2))
	h = int(math.log(k, 2))
	t = math.ceil(m.bit_length() / h)

	#initialize X_0 with the seed
	X = [seed]

	#Create a mask to get h bits
	h_mask = 2**h - 1

	C = 0
	for i in range(0, t):
		# Get the block of h bits from m
		bitpos = (t-i-1)*h
		Mi = (m >> bitpos) & h_mask

		# Compute X_i
		Xi = modexp(X[i], 2, n)
		X.append(Xi)

		# Pi = h least significant bits of Xi
		Pi = Xi & h_mask
		# xor to get Ci		
		Ci = Pi ^ Mi
		# Append Ci to full cyphertext
		C += Ci * (2**bitpos)

	return C, X[t]


# Decrypts the cyphertext tuple and returns the plaintext
def decrypt(cyphertext):
	C, Xt = cyphertext

	#compute k, h, and t
	k = int(math.log(n, 2))
	h = int(math.log(k, 2))
	t = math.ceil(C.bit_length() / h)

	#Create a mask to get h bits
	h_mask = 2**h - 1

	# compute d1, d2, u, v, and X0
	d1 = modexp(int((p+1)/4), t+1, p-1)
	d2 = modexp(int((q+1)/4), t+1, q-1)
	u = modexp(Xt, d1, p)
	v = modexp(Xt, d2, q)
	X0 = (v*a*p + u*b*q) % n

	print(d1, d2)

	#initialize X with X0
	X = [X0]

	m = 0
	for i in range(t):
		#Get the block of h bits from C
		bitpos = (t-i-1)*h
		Ci = (C >> bitpos) & h_mask

		#Compute X_i
		Xi = modexp(X[i], 2, n)
		X.append(Xi)

		# Pi = h least significant bits of Xi
		Pi = Xi & h_mask
		# xor to get Mi		
		Mi = Pi ^ Ci
		# Append Mi to full plaintext
		m += Mi * (2**bitpos)

	return m



plaintext = "10011100000100001100"
#convert plaintext into an int
m = int("0b" + plaintext, 2)

print("Plaintext:", m, "or", plaintext)

#Compute public key and choose a seed
n = p * q
seed = 159201

cyphertext = encrypt(m, n, seed)
print("Cyphertext:", cyphertext, "or", "(" + bin(cyphertext[0])[2:] + ", " + bin(cyphertext[1])[2:] + ")")

decrypted = decrypt(cyphertext)
print("Decrypted ciphertext:", decrypted, "or", bin(decrypted)[2:])



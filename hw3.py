import sys
import math

#Global parameters
p = 499
q = 547
a = -57
b = 52
X = [159201]

# Encrypt a plaintext using the Blum Goldwater Probabilistic Encryption Algorithm
# uses the global parameters p, q, a, b, and X
# returns a tuple for the cyphertext (C, X_t+1)
def encrypt(m):
	# We'll use the global list X to store all Xi values
	# and use X[0] as our seed
	global X

	# calculate n, h and t
	n = p * q
	k = int(math.log(n, 2))
	h = int(math.log(k, 2))
	t = math.ceil(m.bit_length() / h)

	#Create a mask to get h bits
	h_mask = 2**h - 1

	C = 0
	for i in range(0, t):
		# Get the block of h bits from m
		bitpos = (t-i-1)*h
		Mi = (m >> (bitpos)) & h_mask

		# Compute X_i
		Xi = (X[i]**2) % n
		X.append(Xi)
		
		# Pi = h least significant bits of Xi
		Pi = Xi & h_mask
		# xor to get Ci		
		Ci = Pi ^ Mi
		# Append Ci to full cyphertext
		C += Ci * (2**bitpos)

	return C, X[t]

def decrypt(c):
	return



plaintext = "10011100000100001100"
#convert plaintext into an int
m = int("0b" + plaintext, 2)
print(m)
print(encrypt(m))


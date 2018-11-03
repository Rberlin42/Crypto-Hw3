# Crypto-Hw3
Cryptography and Network Security Hw3

## Implementation Details

For this homework I implemented a crypto system uing the Blum Goldwasser Probabilistic Encryption
Algorithm.  My program contains two main functions, `encrypt` and `decrypt`.  I also needed to make
use of modular exponentiation to work with larger numbers so I implemented a function to do that as
well.  The parameters and plaintext given for this homework are hard-coded in for simplicity.  The
program begins by converting the binary plaintext into an integer, as I figured it would be simpler
to work with actual numbers in the encryption function rather than strings of bits.  It then computes
the public key `n` to be used in both the encryption and decryption.  It then encrypts the plaintext,
and decrypts the cyphertext to ensure that D(E(m)) = m.

`encrypt` takes in the plaintext, `m`, as an integer, the public key, `n`, and the random seed.
The encryption algorithm breaks the plaintext into t blocks, and encrypts each one sequentially by
computing the xor with the h least significant bits of X<sub>i</sub>, which is computed at each step using the
previous one.  The first X<sub>i</sub> is computed using the seed, and the final X<sub>t+1</sub> is returned in a
tuple with the cyphertext.

`decrypt` takes in a tuple representing the cyphertext, where the first element is the cyphertext,
and the second element is X<sub>t+1</sub>, which we can use to compute the 'seed' for the decryption.
After computing the seed X<sub>0</sub>, the function acts very similar to the encryption function. It
breaks up the cyphertext in to t blocks, and decrypts each one sequentially by computing the xor with 
the h least significant bits of X<sub>i</sub>, which is computed the same way as in the encryption alg.
After decrypting each block, it will return the full plaintext as an integer.

Output:  
Plaintext: 639244 or 10011100000100001100  
Cyphertext: (134372, 139680) or (100000110011100100, 100010000110100000)  
Decrypted ciphertext: 639244 or 10011100000100001100  
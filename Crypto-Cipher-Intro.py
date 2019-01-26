"""
<<<<<<<<<<<<<<<<<<<<<< Crypto.Cipher package >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
	
	There are three types of encryption algorithms:
		- Symmetric ciphers (all use the same keys for both encryption and decryption)
		- Asymmetric ciphers (the sender and the receiver use separate keys for encryption and 
							decryption, and this is usually used to manipulate large amounts of data)
		- Hybrid ciphers (A cipher that is created that inherits benefits of both(less common))
		
		

These are the API applications of a cipher:

	Creation of a cipher object is done by calling the encryption algorithm followed by the new keyword
		ex ====> from CryptO.Cipher import Salsa20 (Salsa20 being the algorithm)
					cipher = Salsa20.new(your key)
					
		The first parameter a new cipher object is always the key (a key is explained later on)
		The second parameter depending on the program and cipher can either be a nonce (also called an
		Initialization Vector) or a mode of operation (will be explained later on)

			
	That was the creation of the cipher itself, however you are yet to actually encrypt the actual data,
	to do that you must then call the encrypt() method
		ex ====> (assuming your cipher object has already been initialized)	
						
						cipher.encrypt(your data to be encrypted)
		
		General note:
		*Calling of encryption method can only be used to encrypt a single piece of plaintext
		*Python 3 only allows for text converted to bytes to be encrypted
			- Simply declare your variable and place a single 'b' before your single quoted data
			ex ====>	data = b'this is my data turned into bytes!'
			
	The same goes for when you are decrypting a piece of data (assuming the use of a symmetric cipher)
	
						cipher.decrypt(your encrypted data)
						
	
"""
#basic encryption program
from Crypto.Cipher import Salsa20

key = b'16 this the key!'
cipher = Salsa20.new(key)
ciphertext = cipher.encrypt(b'The secret message to be sent')
print(ciphertext)




"""

There are two types of symmetric ciphers:
	- Stream Ciphers
		These are the most natural kinds of ciphers and encrypt one bit of data at a time (ex: Salsa20)
		
	- Block Ciphers	
		These can only operate on fixed amounts of data and the most important block cipher algorithm
		is AES (Advanced Encryption Standard ====> block size 128 bits (16 bytes))
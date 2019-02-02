"""
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Block Cipher>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

	Block ciphers are encryption methods that unlike stream ciphers encrypts data and information
	in chunks of data. One of the most widely used and most widely trusted methods of block ciphers
	is the Advanced Encryption Standard (AES). The keys that are produced for block ciphers can either be of 128, 192, or 256
	bit length (16 bytes => 128 bits for AES).
	
	
	Focusing on AES, encryption in PyCryptodome using AES is the same as using Salsa20 for stream ciphers.
	One would need to call the AES.new() function with very special parameters:
	
		- key ===> Used for encryption (usually sy,metric)
		
		- Mode of operation ===>(an algorithm that dictates the randomness of encryption for blocks of data)
			They are meant to ensure that the blocks that are being encrypted leaves no trace of a pattern.
			
		- Initialization Vector(IV) ===> This is essentially the same thing as a noce but specified for
			block ciphers to ensure that the actual encrypted data itself will always be different even if the
			blocks of data being encrypted are exactly the same.
	
"""

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = b"This is a swell day for some encryption!"	#Data to be encrypted
key = get_random_bytes(16)				#Generation of a 16 byte key (128 bits)
cipher = AES.new(key, AES.MODE_EAX)			#Generation of the AES cipher algorithm with IV EAX Mode
nonce = cipher.nonce					#Creation of the nonce object which is needed along with the IV

ciphertext = cipher.encrypt_and_digest(data)		#Encryption of the message stored in data
				



#Separate the following code into a seperate file in the same folder/working directory
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)				#Creation of the 16 byte key (128 bits)
cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)	#Creation of the AES cipher object for decryption using noce and IV
decrypted = cipher.decrypt(ciphertext)			#Prints out the decrypted data

try: 							#Checksum of authenticity of code ciphering
	cipher.verify(ciphertext)
	print("Authentic message: " + decrypted)
except ValueError:
	print("Wrong key pairing => data corrupted or incorrect")

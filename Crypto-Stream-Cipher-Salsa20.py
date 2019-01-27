"""
<<<<<<<<<<<<<<<<<<<<<<<<<< Stream Ciphers >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

	Stream ciphers are part of the symmetric cipher algorithms that deal with encrypting and decrypting
	data one bit at a time, two of the more popular stream cipher algorithms are ChaCha20 and Salsa20 (the 
	later will be used)
	
	As aforementioned creating a new cipher object using Salsa20 the new() keyword is required. The parameter 
	for this object include the follow:
		ex ====>	cipher = Salsa20.new(key, nonce)
		
			- The key is any plaintext converted to bits that either has to be 256 or 128 bits long
			- The nonce otherwise known as the initialization vector is a specific number or value
			  that is used for message or session authentication (nonce stands for number used once)
			  
				The Initialization Vector (IV) is a different kind of nonce that is used for data encryption
				as to ensure the prevention of repeating sequences of ciphertext. It is not always necessary
				for smaller ciphers 
				
				*Initialization vectors(IVs) are used for block ciphers mostly and nonces are usually used for
				stream ciphers*
				
				
	
			
			  
			  




"""
#encryption
from Crypto.Cipher import Salsa20


data = b'Hey there World! Hows it going?'	#data to be encrypted
key = b'*Thirty-two byte (256 bits) key*'	#random generation of a key which is needed for encryption based on the cipher algorithm
nonce = b'123456789012345'	#either of the nonce values should work (test both if necessary)
cipher = Salsa20.new(key)	#generation of the encryption algorithm
nonce = cipher.nonce		#generation of the nonce value to be used for authentication
message = nonce + cipher.encrypt(data)	#actual encryption of the message
print(message)

#decryption (separate this code into another file in the same working directory/folder)

from Crypto.Cipher import Salsa20


nonce = message[:8] #nonce from encryption file that will be used for decryption
ciphertext = message[8:]	#ciphered text that meant to be decrypted (could also import data from other file)
cipher = Salsa20.new(key, nonce)	#generation of the algorithm that is to be used for decryption
decrypt = cipher.decrypt(ciphertext)	#actual decryption of the ciphered data
print(decrypt)


"""
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Hashing>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
		
		Hashing is the action of encrypting data or information as like with ciphering. However, unlike 
		ciphering which is done with the intention of decryption at one point or another, hashing on the 
		other hand is known as one way encryption in that once something is hashed, it cannot be deciphered.
		This method of encryption is especially important for the security of passwords stored over the internet.
		Traditionally before hashing became standardized passwords and other sensitive information was stored
		as it is in databases and when hacked would give direct access to said sensitive information. Hashing allows
		for the encryption of the sensitive data which will be stored and compared rather than using the actual data.
		
		SHA (Secure Hash Algorithm) is one of the standardized hashing algorithms and it can either executed using varying bit sizes,, some 
		of which include:
			 - SHA-2 Family (SHA-224, SHA-256, SHA-384, SHA-512, SHA-512/224, SHA-512/256)
			 - SHA-3 Family  (SHA3-224, SHA3-256, SHA3-384, SHA3-512)
			 - BLAKE2 Family (BLAKE2s, BLAKE2b)
			 
		I will be utilizing and focusing on the SHA-256 hashing algorithm as it is of the more commonly used algorithms
		

"""

from Crypto.Hash import SHA256

data = b'This is my message to be hashed!'
hash = SHA256.new(data)
print("This is the hex value of the hashed data: " + hash.hexdigest())
hash.update(b'And this will also be hashed!!')
print("This is the regular value of the hashed data: " + str(hash.digest()))
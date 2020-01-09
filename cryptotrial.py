from Crypto.Cipher import AES

key = "YELLOW SUBMARINE" #needs to be 16bytes
plaintext = "Goodness great balls of fire!"

#Encode (string and key needs to be multiple of 16bytes)
padding = (16 - (len(plaintext) % 16))
plaintext = plaintext + (chr(3) * padding) # add 'End of Text' padding to plaintext

encryptor = AES.new(key, AES.MODE_ECB)
ciphertext = encryptor.encrypt(plaintext)
#ciph = hex(ciphertext)
print(ciphertext)

#Decode
decryptor = AES.new(key, AES.MODE_ECB)
plaintext = decryptor.decrypt(ciphertext)
plaintext = plaintext[ : -3]  #.strip(chr(3)) # remove 'End of Text' padding
print( plaintext)

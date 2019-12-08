'''
Vignere Cipher
Author: tukykarmakar
Original work
Example
	Plain Text: ATTACKATDAWN
	Keyword: LEMON
	Cipher Text: LXFOPVEFRNHR
'''

class VignereCipher:
	table = []
	def __init__ (self):
		charAscii = [i for i in range (65, 91)]
		for i in range (26):
			self.table.append (charAscii.copy ())
			l = charAscii.pop (0)
			charAscii.append (l)
		
	def encrypt (self, message, keyword):
		ml = len (message)
		kl = len (keyword)
		cipherText = []
		
		m = message.upper ()
		k = keyword.upper ()
			
		for i in range (ml):
			cipherCol = ord (m[i]) - 65
			cipherRow = ord (k[i%kl]) - 65
			cipherText.append (chr (self.table[cipherRow][cipherCol]))
			
		return cipherText
		
	def decrypt (self, cipher, keyword):
		cl = len (cipher)
		kl = len (keyword)
		plainText = []
		
		c = cipher.upper ()
		k = keyword.upper ()
			
		for i in range (cl):
			cipherEle = ord (c[i])
			cipherRow = ord (k[i%kl]) - 65
			plainText.append (chr (self.table[cipherRow].index(cipherEle) + 65))
			
		return plainText
		
VC = VignereCipher ()
choice = 0

while (choice != 3):
	print ("VIGNERE CIPHER")
	print ("Enter your Choice:-")
	print ("1. Encrypt")
	print ("2. Decrypt")
	print ("3. Exit")
	
	try:
		choice = int (input ("Choice: "))
		if (choice < 1 or choice > 3):
			raise ValueError
	except ValueError:
		print ("Invalid Choice! Try Again.\n")
		
	if choice == 1:
		message = str (input ("\nEnter the cipher text message: "))
		keyword = str (input ("Enter the encryption keyword: "))
		coded = "".join (VC.encrypt (message, keyword))
		print ("The encrypted message is", coded, "\n")
		
	elif choice == 2:
		coded = str (input ("\nEnter the plain text message: "))
		keyword = str (input ("Enter the encryption keyword: "))
		message = "".join (VC.decrypt (coded, keyword))
		print ("The decrypted message is", message, "\n")

	elif choice == 3:
		print ("\nGood Bye!")

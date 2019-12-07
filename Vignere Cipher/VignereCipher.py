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
coded = "".join (VC.encrypt ("ATTACKATDAWN", "LEMON"))
decoded = "".join (VC.decrypt (coded, "LEMON"))
print (coded)
print (decoded)
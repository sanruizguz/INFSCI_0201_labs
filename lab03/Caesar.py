
class Caesar:
    def __init__(self,key) -> None:
        self._key=int(key)

    # Setter
    def set_key(self, key_cipher):
        self._key=int(key_cipher)

    # Getter
    def get_key(self):
        return(self.key)
    
    # Encrypt method
    def encrypt(self,plain_text):
        # Get unicode
        no_space=[]
        for i in plain_text:
           unicode = (ord(i) + self._key)
           if unicode == (32 + self._key):
              unicode = 32
           else:
              pass
           no_space.append(unicode) 
        decode = ''.join([chr(c) for c in no_space])
        return decode.lower()
    
    # Decrypt method
    def decrypt(self,plain_text):
        # Get unicode
        no_space_de=[]
        for i in plain_text:
           unicode = (ord(i) - self._key)
           if unicode == 32 - self._key:
              unicode = unicode + self._key
           else:
              pass
           no_space_de.append(unicode) 
        decrypted = ''.join([chr(c) for c in no_space_de])
        return decrypted.lower()



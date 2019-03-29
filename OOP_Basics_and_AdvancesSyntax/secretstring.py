class SecretString:
    def __init__(self, plaintext, decrypt):
        self.__plaintext = plaintext
        self.__decrypt = decrypt
        
    def rundec (self, decrypt):
        if decrypt == self.__decrypt:
            return self.__plaintext
        else:
            return 'Get Lost'
        
        
newobj = SecretString("Moj","Roj")

print(newobj.rundec("Roj"))

print(newobj._SecretString__plaintext)
import simplecrypt

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

with open("passwords.txt", "r") as pw:
    for password in pw:
        try:
            print(password)
            info = simplecrypt.decrypt(password.strip(), encrypted)
            print(info)
        except:
            pass

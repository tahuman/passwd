import string
import secrets

def passwd(self):
    chars = string.ascii_letters + string.digits
    chars += '%&$#()'
    return ''.join(secrets.choice(chars) for i in range(self))

for x in range(10):
    print(passwd(16))
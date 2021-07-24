import random

password = ""
for i in range(8):
    i = chr(random.randint(32, 128))
    password = str(password) + i
print(password)

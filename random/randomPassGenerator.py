import random

chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!, @,#$%^&*.'
number = 3
length = 3
for P in range(number):
    password = ''
    for C in range(length):
        password += random.choice(chars)
    print(password)


txtFileWriter = open("passlist.txt", "a")
txtFileWriter.write(password)
txtFileWriter.close()

file = open('passlist', 'w')
file.write(password)
file.close()
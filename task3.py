import random
import string

length =int(input("enter the length of the password"))
characters= string.ascii_letters + string.digits

password= ''

for i in range(length):
    password+=random.choice(characters)
    
print("your password is",password)                      

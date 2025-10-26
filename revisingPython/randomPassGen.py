import random
import string   

'''
-> print(string.ascii_letters):  abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
-> similarly we have string.digits, string.punctuation, string.ascii_lowercase, string.ascii_uppercase, etc.
'''

charValues = string.ascii_letters + string.digits + string.punctuation
random.choice(charValues)  # This will return a random character from the combined string

passwordLength = int(input("Enter the desired length of the password: "))
password = ""
for i in range(passwordLength):
    password += random.choice(charValues)
print("Generated Password:", password)



'''
alternative way using list comprehension:

result = [random.choice(charValues) for i in range(passwordLength)]
print("Generated Password:", "".join(result))
'''

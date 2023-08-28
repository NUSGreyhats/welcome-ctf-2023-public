import pyminizip
import zipfile 
import os 

# Double encrypted Zipfile using two libraries
# for the operation's utmost secrecy 
password = os.urandom(16)
pyminizip.compress_multiple(['report.txt', 'secret.png'], ["", ""], "secret.zip", password, 0)

# Encrypt one more time
archive = zipfile.ZipFile("secret.zip", 'r')
password = os.urandom(16)
archive.setpassword(password)

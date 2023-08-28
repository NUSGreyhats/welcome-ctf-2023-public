#!/usr/bin/env python3

import torch 
import secrets 
import tempfile
import os 

os.environ['FLAG'] = "greyhats{are_you_perhaps_pickle_rick???}"

print("Can you solve my version of the ABC conjecture?")
print("To add a bit of challenge, please do this using PyTorch.")

try:
    content = bytes.fromhex(input("Enter the PyTorch saved model (in hex): "))
    if len(content) > 2048:
        print("Model too big")
except ValueError:
    print("Please try again!")
    exit(0)

# Create temp file for loading the model
temp = tempfile.TemporaryFile()
temp.write(content)
temp.seek(0)

# Loading the model
model = torch.load(temp)
model.eval()
data = torch.tensor([secrets.randbits(32), secrets.randbits(32)])
output = model(data)

if output == secrets.randbits(32):
    print("Nice, you have solved the conjecture")
    print(os.environ['FLAG'])
else:
    print("Nice attempt!")  
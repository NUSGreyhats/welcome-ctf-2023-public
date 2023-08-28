import random
import time

FLAG = "REDACTED"

def get_encrypted_flag(flag):
    t = int(time.time())
    random.seed((t ^ ((t & 0xFFFF) * (t >> 16)) ^ ((t << 5) & 0xFFFFFFFF) ^ ((t >> 3) & 0xFFFFFFFF) ^ ((t << 4) & 0xFFFFFFFF)) & 0xFFFFFFFF)

    encrypted_flag = []

    for char in flag:
        key = random.randint(1, 255)
        encrypted_char = ord(char) ^ key
        encrypted_flag.append(encrypted_char)

    with open("encrypted_flag.bin", "wb") as f:
        f.write(bytes(encrypted_flag))

get_encrypted_flag(FLAG)
import random
import time

def get_decrypted_flag():
    with open("encrypted_flag.bin", "rb") as f:
        encrypted_flag = list(f.read())

    t = int(time.mktime((2023, 8, 25, 22, 0, 0, 0, 0, 0))) # Start of CTF (25 Aug 2023 22:00 GMT+8) in UNIX Time
    dercypted_flag = ""

    # Bruteforce seed until flag is of valid format
    while True:
        random.seed((t ^ ((t & 0xFFFF) * (t >> 16)) ^ ((t << 5) & 0xFFFFFFFF) ^ ((t >> 3) & 0xFFFFFFFF) ^ ((t << 4) & 0xFFFFFFFF)) & 0xFFFFFFFF)
        dercypted_flag = ""

        for char in encrypted_flag:
            key = random.randint(1, 255)
            decrypted_char = chr(char ^ key)
            dercypted_flag += decrypted_char
        
        if "greyhats" in dercypted_flag:
            print(dercypted_flag)
            break

        t -= 1

get_decrypted_flag()

# Seed is 1692971243 (25 Aug 2023 21:47:23 GMT+8)
# Flag is greyhats{1_w15h_7H3r3_W45_4_r4nd0m_cH4ll3n93_93n3r470r}
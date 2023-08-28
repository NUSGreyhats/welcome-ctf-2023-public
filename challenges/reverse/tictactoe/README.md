# Challenge Details

Android app reversing. The app xor decrypts a list of strings into a list of Telegram channel invite links. The channel descriptions contain some values that are used for decrypting more code that are to be executed. Each channel description decrypts a dex module to be executed. One of the dex modules will print out the flag in the logs.

The catch is that by default, the app only decrypts and executes the 1st module then stops. The flag printing module is the 18th. Players should either patch/instrument/reverse engineer the app to get the flag from there.

# Setup Instructions

Attached tictactoe.apk
https://github.com/NUSGreyhats/greyctf23-challs/tree/daniel/re-tictactoe/final/re/tictactoe

# Key concepts

Android malware obfuscation
Android malware contacting external sites that controls its behaviour

# Learning Objectives

Learn Android reversing and about how Android malware hides their code.
Read code/use frida/capture network traffic to get the information needed.

---

# Part 1

## Description

This app decrypts some strings and makes an external network connection. What is the domain of the website that it contacts?

Flag format: [name].[tld], e.g. nus.edu (just something dot something, no subdomains expected)

## Hints

1. You need an Android decompiler. I recommend jadx-gui.
2. There are some possible approaches. Choose your favorite one. Either read the decompiled code or use some app to capture network traffic.
3. Use Medusa to log http traffic (https://cryptax.medium.com/tracking-android-joker-payloads-with-medusa-static-analysis-and-patience-672348b81ac2, https://www.youtube.com/watch?v=ffM5R2Wfl0A).
4. It is prefered to use either a real phone or an emulator that runs on an ARM machine. If you use an emulator that runs on x86, things may not work as expected (although for this chall it probably works fine). Consider setting this up: https://www.youtube.com/watch?v=fTT5hxiMv6I.
5. More guides - https://www.youtube.com/playlist?list=PLn_It163He3168Q21sPfiyb0j5K6_riG7

## Flag

`t.me`

# Part 2

## Description

From the external server, the app requests some information. It includes some data:
1. Hex string that is a key used to decrypt a file into a DEX module that will be loaded and invoked
2. Index of the file to decrypt

What is the key for the file at index 2?

Flag format: hex string (may contain both uppercase and lowercase letters)

## Hint

1. It may be useful to learn more about Android dynamic DEX loading to understand the code better.

## Flag

`hBc63dbs`

# Part 3

## Description

You are almost there. One of the DEX modules will print the flag.

## Hints

1. There are some possible ideas. You may modify the information returned from the server so that it continues to decrypt the next DEX module.
2. If you are stuck, really consider using Frida. https://www.youtube.com/watch?v=RJXsvAjZl9U


## Flag

`grey{dont_install_apps_outside_of_play_store!_1bdac4980ebd7}`

# Point Distribution - 100, 150, 250

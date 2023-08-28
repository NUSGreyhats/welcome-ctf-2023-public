# welcome-ctf-2023
the best beginner friendly local ctf in august

held for 48 hours from 24th to 26th of August 2023

# Challenge Creation

Things to include for each challenge:
- Dockerfile if challenge requires to be hosted as a remote service (Refer to the sample that is given in Templates, ping in the infrastructure chat if there is any issues)
- Challenge files
- README.md

## Challenge Scope

This year, we will primarily have 6 categories --- crypto, forensics, misc _(includes programming, OSINT, etc.)_, pwn, reverse engineering, web exploitation.

Challenge Creators are free to contribute challenges in any of the mentioned categories, but challenges should **NOT be entirely guessy** and should aim to be fun and educational.

## Things to include in README.md

| Things to include               | Example                                                                   |
| ------------------------------- | ------------------------------------------------------------------------- |
| Challenge Details               | `Caesar thought of the perfect cipher. Can you break it?`                 |
| Setup instructions              | `Step 1: Download the file`                                               |
| Possible hints (Optional)       | `Hint: What Caesar Cipher?`                                               |
| Key concepts                    | `Scripting`                                                               |
| Solution (Can also be a script) | `Write a script to brute force all the combinations of the caesar cipher` |
| Learning objectives             | `Learn about the Caesar Cipher`                                           |
| Flag                            | `greyhats{salad_is_great_but_cipher_is_not}`                              |

_the flag format is greyhats{FLAG}_

## How to add a challenge?

1. Create your own branch and commit to the branch
2. Make a pull request to merge the challenge (Skip this if you already have a PR)
   1. Add the correct labels accordingly
3. After checking your request will be merged or changes will be requested
   1. If changes are requested, back to 1.
   2. If approved go to 4
4. You are done :D

# For challenge testing

- Download [Docker](https://www.docker.com/)
- Clone the repository using `git clone https://github.com/crossctf/crossctf22-challs.git`
- Go into the PR of the challenge you want to test
- Follow build instructions
- Test the challenge
  - Assign yourself as reviewer for the PR, and provide the following information
    - Rating
    - Feedback
    - Category/Difficulty you think it should be in (If the category / difficulty is different)

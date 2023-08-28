**Challenge Details**

Your classic calculator 🙂

**Key concepts**

Python executable re, static analysis of the binary, python bytecode re

**Learning Objectives**

Participants will learn about reversing python executables back to their pyc files.

**Solution**

Convert executable to pyc (Tools like pyinstxtractor), and then to py script, find out the key to get back the flag (XOR) operation
Might need to rewrite the recovered py file if participants used https://tool.lu/en_US/pyc/ to reverse back.

```
def magic():
    flag = ""
    arr = [ 1374, 1355, 1372, 1344, 1361, 1368, 1357, 1354, 1346, 1353, 1344, 1370, 1382, 1387, 1290, 1382, 1288, 1354, 1382, 1353, 1401, 1360, 1367, 1407, 1388, 1365, 1304, 1348]
    
    for i in arr:
        flag += chr(i ^ 1337)
    print(flag)

magic()
```

**Author**

Tensor (Yong Liang)

**Flag**

`greyhats{pyc_R3_1s_p@inFUl!}`


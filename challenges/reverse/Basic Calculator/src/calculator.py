from tkinter import *

win = Tk()
win.geometry("312x324")
win.resizable(0, 0)
win.title("Calculator Model 1337C")

def create_button(frame, text, fg, width, height, bg, cursor, command, columnspan):
    button = Button(frame, text=text, fg=fg, width=width, height=height, bd=0, bg=bg, cursor=cursor, command=command)
    return button

def string_reverser(s):
    return s[::-1]

def list_average(nums):
    if not nums:
        return None
    return sum(nums) / len(nums)

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_sequence = [0, 1]
    for i in range(2, n):
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    
    return fib_sequence

def vowel_count(s):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    return count

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shifted = (ord(char) - ascii_offset + shift) % 26 + ascii_offset
            result += chr(shifted)
        else:
            result += char
    return result

def magic(x):
    arr = [1374, 1355, 1372, 1344, 1361, 1368, 1357, 1354, 1346, 1353, 1344, 1370, 1382, 1387, 1290, 1382, 1288, 1354, 1382, 1353, 1401, 1360, 1367, 1407, 1388, 1365, 1304, 1348]
    out = "".join([chr(i ^ x) for i in arr])
    return out

def deduplicate_list(lst):
    return list(set(lst))

def word_count(text):
    words = text.split()
    return len(words)

def even_numbers(nums):
    return [num for num in nums if num % 2 == 0]

def compress_list(lst):
    return [item for index, item in enumerate(lst) if index % 2 == 0]

def rectangle_area(width, height):
    return width * height

def title_case(s):
    return " ".join([word.capitalize() for word in s.split()])

def odd_numbers(nums):
    return [num for num in nums if num % 2 != 0]

def multiply_list_elements(lst, factor):
    return [item * factor for item in lst]

def count_unique_characters(s):
    unique_chars = set(s)
    return len(unique_chars)

def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def btn_clear(): 
    global expression 
    expression = "" 
    input_text.set("")

def btn_equal():
    global expression
    result = str(eval(expression))
    
    if result == "1337":
        if "*" in str(expression) and "191" in str(expression):
            string_reverser(result)
            list_average([int(result)])
            is_palindrome(result)
            fibonacci(3)
            vowel_count(result)
            caesar_cipher(result, 3)
            input_text.set(magic(int(result)))
            deduplicate_list([int(result)])
            word_count(result)
            even_numbers([int(result)])
            rectangle_area(int(result), int(result))
        else:
            input_text.set("Close enough :) RE IT")
    else:
        input_text.set(result)
    expression = ""
 
expression = ""
  
input_text = StringVar()
  
input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=TOP)
 
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

btns_frame = Frame(win, width=312, height=272.5, bg="grey")
btns_frame.pack()

button_params = [
    ("C", "black", 32, 3, "#eee", "hand2", btn_clear, 3),
    ("/", "black", 10, 3, "#eee", "hand2", lambda: btn_click("/"), 1),
    ("7", "black", 10, 3, "#fff", "hand2", lambda: btn_click(7), 1),
    ("8", "black", 10, 3, "#fff", "hand2", lambda: btn_click(8), 1),
    ("9", "black", 10, 3, "#fff", "hand2", lambda: btn_click(9), 1),
    ("*", "black", 10, 3, "#eee", "hand2", lambda: btn_click("*"), 1),
    ("4", "black", 10, 3, "#fff", "hand2", lambda: btn_click(4), 1),
    ("5", "black", 10, 3, "#fff", "hand2", lambda: btn_click(5), 1),
    ("6", "black", 10, 3, "#fff", "hand2", lambda: btn_click(6) ,1),
    ("-", "black", 10, 3, "#eee", "hand2", lambda: btn_click("-"), 1),
    ("1", "black", 10, 3, "#fff", "hand2", lambda: btn_click(1), 1),
    ("2", "black", 10, 3, "#fff", "hand2", lambda: btn_click(2), 1),
    ("3", "black", 10, 3, "#fff", "hand2", lambda: btn_click(3), 1),
    ("+", "black", 10, 3, "#eee", "hand2", lambda: btn_click("+"), 1),
    ("0", "black", 21, 3, "#fff", "hand2", lambda: btn_click(0), 2),
    (".", "black", 10, 3, "#eee", "hand2", lambda: btn_click("."), 1),
    ("=", "black", 10, 3, "#eee", "hand2", btn_equal, 1),
]

col, row = 0, 1
for params in button_params:
    button = create_button(btns_frame, *params)
    button.grid(row=row, column=col, padx=1, pady=1, columnspan=params[-1])
    col += params[-1]
    if col > 3:
        col = 0
        row += 1

win.mainloop()

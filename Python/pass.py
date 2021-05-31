import random
characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKL123456&''()"
#ARRAYS AND NESTING LOOPS
#random password generator
while 1:
    password_len=int(input(" input  password length : "))
    password_count=int(input(" input number of passwords: "))
    for x in range (0,password_count):
        password=""
        print(x)
        for x in range (0,password_len):
            password_char=random.choice(characters)
            print(password_char)
            password=password +password_char
        print("Your  password is : ", password)
import string
import random
import pyperclip

if __name__ == "__main__":
    print("Password Generator")
    passwd = None
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    while True:
        plen = input("\nEnter Your Password Length: ")
        if plen.isnumeric():
            plen = int(plen)
            break
        else:
            print("Given input was not a number, please enter a number.")
            continue
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    passwd = ("".join(random.choices(s,  k=plen)))
    print("Your Password is: %s" %(passwd))
    pyperclip.copy(passwd)
    print("And it has been copied to your clipboard.")
    

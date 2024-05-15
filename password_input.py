"""import sys
#import termios
#import tty

def getpass(prompt="Password: "):
    '''Prompt for password input without echoing characters.'''
    fd = sys.stdin.fileno()
#    old_settings = termios.tcgetattr(fd)
    try:
#        tty.setcbreak(fd)
        sys.stdout.write(prompt)
        sys.stdout.flush()
        password = ""
        while True:
            char = sys.stdin.read(1)
            sys.stdin.flush()
            sys.stdout.write("\b")
            sys.stdout.flush()
            sys.stdout.write(" ")
            sys.stdout.flush()
            sys.stdout.write("\b")
            sys.stdout.flush()
            
            print("\b",end='',flush=True)
            print(" ",end='',flush=True)
            print("\b",end='',flush=True)
            print("*",end='',flush=True)
            if char == "\r" or char == "\n":
                break
            password += char
        sys.stdout.write("\n")
        return password
    finally:
        #termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        pass

# Example usage:
password = getpass("Enter your password: ")
print("Password entered:", password)"""




"""import sys

password=""
sys.stdout.write("Enter Password:- ")
sys.stdout.flush()
while True:
    sys.stdin.__enter__
    #char=sys.stdin.read(1)
    char=sys.stdin.truncate(1)
    sys.stdin.__exit__
    #sys.stdin.flush()
    if char=="\r" or char=="\n" or char=="":
        break
    else:
        password+=char
        #sys.stdout.flush()
        #sys.stdout.write("123")
        #sys.stdout.flush()
        #sys.stdin.close()
        sys.stdout.write("\b")
        sys.stdout.flush()
        sys.stdout.write(" ")
        sys.stdout.flush()
        sys.stdout.write("\b")
        sys.stdout.flush()
        sys.stdout.write("*")
        sys.stdout.flush()
sys.stdout.write("\n")
print(password)"""

import msvcrt

def get_char():
    # Set stdin to non-blocking mode
    #sys.stdin = open(0)
    return msvcrt.getch().decode('utf-8')

# Example usage:
print("Press any key:")
password=""
for i in range(4):
    char = get_char()
    password+=char
    print("*",end='',flush=True)
print("You pressed:", password)




'''import sys

def getpass(prompt='Password: '):
    """Prompt for password input without echoing characters."""
    password = ''
    sys.stdout.write(prompt)
    sys.stdout.flush()
    for char in iter(lambda: sys.stdin.read(1), '\n'):
        password += char
        sys.stdout.write('*')
        sys.stdout.flush()
        sys.stdout.write('a')
        print('s',end='')
    return password

# Example usage:
password = getpass("Enter your password: ")
print("\nPassword entered:", password)'''


'''import sys

def getpass(prompt='Password: '):
    """Prompt for password input without echoing characters."""
    password = ''
    sys.stdout.write(prompt)
    sys.stdout.flush()
    while True:
        char = sys.stdin.read(1)
        if char == '\r' or char == '\n':
            sys.stdout.write('\n')
            return password
        elif char == '\b':  # Backspace
            if password:
                # Move cursor back by one character
                sys.stdout.write('\b \b')
                sys.stdout.flush()
                password = password[:-1]
        else:
            password += char
            sys.stdout.write('*')
            sys.stdout.flush()

# Example usage:
password = getpass("Enter your password: ")
print("Password entered:", password)'''

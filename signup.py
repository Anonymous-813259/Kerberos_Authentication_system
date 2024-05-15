import msvcrt

def get_char():
    return msvcrt.getch().decode('utf-8')

def add_record(record):
    db = open("database.dat","a")
    db.write(record)
    db.close()
    return "success"

def username_exist(username):
    db=open("database.dat","r")
    found=False
    for line in db:
        user=(line.split("&space"))[0]
        if user.lower() == username.lower():
            return True
    if not found:
        return False
    
def get_password(info):
    print(info,end='',flush=True)
    password=""
    while(True):
        char = get_char()
        if char=='\n' or char=='\r':
            print()
            break
        elif char=="\b":
            password=password[:-1]
            print("\b \b",end='',flush=True)
        else:
            password+=char
            print("*",end='',flush=True)
    return password

import msvcrt

def get_char():
    return msvcrt.getch().decode('utf-8')

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

def login():
    while True:
        username=input("Enter Username: ")
        password=get_password("Enter Password: ")
        db=open("database.dat","r")
        found=False
        for line in db:
            user=(line.split("&space"))[0]
            userpass=(line.split("&space"))[1]
            if user==username and password==userpass:
                found=True
        db.close()
        if found==True:
            return username, password
        else:
            print("Invalid Credentials")
        
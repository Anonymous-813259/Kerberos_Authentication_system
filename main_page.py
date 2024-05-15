import signup
import login
import socket
import operations

def connect_server(username,password,value):
    client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_ip="127.0.0.1"
    server_port=12345
    client_socket.connect((server_ip,server_port))
    print("\n\n\n\nConnection to "+server_ip+":"+str(server_port)+" --> Success")
    credentials=username+" "+password+" "+str(value)
    client_socket.send(credentials.encode())
    if(value==1):
        msg_a,msg_b=((client_socket.recv(1024)).decode()).split("&space")
        print("\n\nMessage a:- ",msg_a)
        print("\n\nMessage b:- ",msg_b)
        session_key=operations.decrypt(msg_a,operations.hashing(password))
        print("\n\nSession Key:- ",session_key)

        msg_c=msg_b
        msg_d=username+" "+client_socket.getsockname()[0]+" "+str(client_socket.getsockname()[1])
        messages=msg_c+"&space"+operations.encrypt(msg_d,session_key)
        client_socket.send(messages.encode())

        msg_e,msg_f=((client_socket.recv(1024)).decode()).split("&space")
        print("\n\nMessage e:- ",msg_e)
        print("\n\nMessage f:- ",msg_f)
        client_server_key=operations.decrypt(msg_f,session_key)
        print("\n\nClient - Server Key:- ",client_server_key)

        msg_g=msg_e
        msg_h=username+" "+client_socket.getsockname()[0]+" "+str(client_socket.getsockname()[1])
        messages=msg_g+"&space"+operations.encrypt(msg_h,client_server_key)
        client_socket.send(messages.encode())

        msg_i=(client_socket.recv(1024)).decode()
        if msg_i.lower()=="sucess":
            print("\n\nConnection to the Server ----> [+]Success")
        else:
            print("\n\nConnection to the Server ----> [-]Not Success")


    else:
        username=""
        password=""
        name=""
        email=""
        mobile=""
        while True:
            print("* fields are required")
            while True:
                username = input("Enter Username*: ")
                client_socket.send(username.encode())
                username_exist=(client_socket.recv(1024)).decode()
                if username_exist.lower()=="not exist":
                    break
                else:
                    print("Username already exist")
            password = signup.get_password("Enter Password*: ")
            name = input("Enter Name*: ")
            email = input("Enter Email*: ")
            mobile = input("Enter Mobile number*: ")
            if username and password and name and email and mobile:
                client_socket.send("break".encode())
                break
            client_socket.send("continue".encode())
        record = username+"&space"+password+"&space"+name+"&space"+email+"&space"+mobile+"\n"
        client_socket.send(record.encode())
        msg=(client_socket.recv(1024)).decode()
        if(msg.lower()=="success"):
            print(username," --> Account Creation Success")

    client_socket.close()

if __name__=="__main__":
    ch=0
    while(ch!=3):
        print("\t!Welcome To Our Site!")
        print("1. Login\n2. Sign Up\n3. Exit")
        try:
            ch = int(input("Please Select your option from the above(1/2/3):"))
        except:
            print("\n\nPlease Select the Correct Option (1/2/3)")
        if ch==1:
            username,password=login.login()
            connect_server(username,password,1)
        elif ch==2:
            connect_server("None","None",2)
        elif ch==3:
            print("\n\tThank You for Visiting Our Site")
            print("\n\t\tTHE END")
            break
import random
import operations
import socket
import signup

class Server:
    secret_key="pLmHt(5!3&"
    msg_i=""

    def __init__(self,msg_g,msg_f):
        if msg_g and msg_f:
            client_server_key,username1,client_ip1,client_port1=(operations.decrypt(msg_g,operations.hashing(self.secret_key))).split()
            username2,client_ip2,client_port2=(operations.decrypt(msg_h,client_server_key)).split()
            if username1.lower()==username2.lower() and client_ip1.lower()==client_ip2.lower() and client_port1.lower()==client_port2.lower():
                self.msg_i="sucess"
            else:
                self.msg_i="not sucess"
    
    def get_values(self):
        return self.msg_i

class TicketGrantingServer:
    secret_key="QsCfT!2#4%"
    client_server_key=""
    msg_e=""
    msg_f=""
    def __init__(self):
        pass
    
    def __init__(self,msg_c,msg_d):
        if msg_c and msg_d:
            session_key,username1,client_ip1,client_port1=(operations.decrypt(msg_c,operations.hashing(self.secret_key))).split()
            username2,client_ip2,client_port2=(operations.decrypt(msg_d,session_key)).split()
            if username1.lower()==username2.lower() and client_ip1.lower()==client_ip2.lower() and client_port1.lower()==client_port2.lower():
                for _ in range(3):
                    i=random.randint(0,len(username1)-1)
                    session_key+=username1[i]
                    i=random.randint(0,len(session_key)-1)
                    session_key+=session_key[i]
                    i=random.randint(0,len(client_ip1)-1)
                    self.client_server_key+=client_ip1[i]
                self.client_server_key=operations.hashing(self.client_server_key)
                print("\n\nGenerated Client - Server Key:- ",self.client_server_key)

                self.msg_e=self.client_server_key+" "+username1+" "+client_ip1+" "+client_port1
                self.msg_e=operations.encrypt(self.msg_e,operations.hashing(Server("","").secret_key))
                self.msg_f=operations.encrypt(self.client_server_key,session_key)
        
    def get_values(self):
        return self.msg_e,self.msg_f

        pass

class AuthenticationServer:

    msg_a=""
    msg_b=""

    def __init__(self,username,password):
        found=False
        name=""
        email=""
        mobile=""
        db=open("database.dat","r")
        for record in db:
            arr=record.split("&space")
            user,userpass=arr[0],arr[1]
            if user==username and userpass==password:
                found=True
                name=arr[2]
                email=arr[3]
                mobile=arr[4]
                break
        if found==True:
            session_key=""
            for _ in range(3):
                i=random.randint(0,len(name)-1)
                if name[i]!=" ":
                    session_key+=name[i]
                i=random.randint(0,len(email)-1)
                session_key+=email[i]
                i=random.randint(0,len(mobile)-1)
                session_key+=mobile[i]
            session_key=operations.hashing(session_key)
            print("\n\nGenerated Session Key:- ",session_key)
            encrypted_session_key=operations.encrypt(session_key,operations.hashing(password))
            msg_a=encrypted_session_key
            ticket_granting_ticket=session_key+" "+username+" "+client_addr[0]+" "+str(client_addr[1])

            self.msg_a=msg_a
            self.msg_b=ticket_granting_ticket

        
    def get_values(self):
            return self.msg_a,operations.encrypt(self.msg_b,operations.hashing(TicketGrantingServer("","").secret_key))
    

if __name__=="__main__":
    server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_port=12345
    server_ip="127.0.0.1"
    server_socket.bind((server_ip,server_port))
    server_socket.listen(5)
    while True:
        print(server_ip+":"+str(server_port)+" is ready to recive clients")
        client_socket,client_addr=server_socket.accept()
        print("\n\n\n\nConnection Established with --> ",client_addr)
        client_credentials=(client_socket.recv(1024)).decode()
        username,password,value=client_credentials.split()
        if(value=="1"):
            db=open("database.dat","r")
            found=False
            for line in db:
                user=(line.split("&space"))[0]
                userpass=(line.split("&space"))[1]
                if user==username and password==userpass:
                    found=True
            db.close()
            if found==True:
                AS=AuthenticationServer(username,password)
                msg_a,msg_b=AS.get_values()
                messages=msg_a+"&space"+msg_b
                client_socket.send(messages.encode())

                msg_c,msg_d=((client_socket.recv(1024)).decode()).split("&space")
                TGS=TicketGrantingServer(msg_c,msg_d)
                msg_e,msg_f=TGS.get_values()
                messages=msg_e+"&space"+msg_f
                client_socket.send(messages.encode())

                msg_g,msg_h=((client_socket.recv(1024)).decode()).split("&space")
                service=Server(msg_g,msg_h)
                msg_i=service.get_values()
                client_socket.send(msg_i.encode())
                #If sucess full authentication then connection with the service server will be from here
        
        else:
            while True:
                while True:
                    username=(client_socket.recv(1024)).decode()
                    if not signup.username_exist(username):
                        break
                    else:
                        client_socket.send("exist".encode())
                client_socket.send("not exist".encode())
                wanted=(client_socket.recv(1024)).decode()
                if wanted.lower()=="break":
                    break
            record=(client_socket.recv(1024)).decode()

            val = signup.add_record(record)
            client_socket.send(val.encode())



        print("\n\nConnection Disconnected with --> ",client_addr)
        client_socket.close()

            
            

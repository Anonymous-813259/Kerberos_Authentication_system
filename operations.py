def hashing(info):
    hashvalues = [1779033703, 1150833019, 1013904242, 1521486534, 1359893119, 1694144372, 528734635, 1541459225]

    bytes=[]

    for char in info:
        bytes.append(ord(char))

    hexavalue=dict()
    hexavalue[0]='0'
    hexavalue[1]='1'
    hexavalue[2]='2'
    hexavalue[3]='3'
    hexavalue[4]='4'
    hexavalue[5]='5'
    hexavalue[6]='6'
    hexavalue[7]='7'
    hexavalue[8]='8'
    hexavalue[9]='9'
    hexavalue[10]='a'
    hexavalue[11]='b'
    hexavalue[12]='c'
    hexavalue[13]='d'
    hexavalue[14]='e'
    hexavalue[15]='f'

    for byte in bytes:
        for i in range(len(hashvalues)):
            hashvalues[i]=(hashvalues[i] ^ byte)+(hashvalues[i]<<4)-(hashvalues[i]>>2)

    hashstring=""

    for i in range(len(hashvalues)):
        while hashvalues[i]>0:
            hashstring+=hexavalue[hashvalues[i]%16]
            hashvalues[i]=hashvalues[i]//16

    return hashstring

def encrypt(value,key):
    encrypted_value=""
    for i in range(len(value)):
        asci=ord(value[i])
        key_asci=ord(key[i%len(key)])
        encrypted_value+=chr(asci^key_asci)
    return encrypted_value

def decrypt(value,key):
    decrypted_value=""
    for i in range(len(value)):
        asci=ord(value[i])
        key_asci=ord(key[i%len(key)])
        decrypted_value+=chr(asci^key_asci)
    return decrypted_value

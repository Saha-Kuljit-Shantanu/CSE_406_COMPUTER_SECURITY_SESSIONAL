import socket
import os 
import pickle
from KEYS_FOR_BOB import *
import random as rand
from math import sqrt,cbrt,floor
import binascii
from AES_METHODS import schedule_key,decrypt



dir_path = os.path.dirname(os.path.realpath(__file__))

if __name__ == '__main__' :

    host = '127.0.0.1'
    port = 8081

    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    sock.bind((host,port))

    sock.listen(1)

    print("Initializing socket")

    conn = sock.accept()

    print('Connected')

    Alice_shared_key_tuple = conn[0].recv(1024*16)

    unpickled_tuple = pickle.loads(Alice_shared_key_tuple)

    # Receive curve parametres and shared key from Alice

    print(unpickled_tuple[0],unpickled_tuple[1],unpickled_tuple[2],unpickled_tuple[3],unpickled_tuple[4]) #p,a,b,G,rn

    p = unpickled_tuple[0]

    a = unpickled_tuple[1]

    b = unpickled_tuple[2]

    G = unpickled_tuple[3]

    round_num = unpickled_tuple[4]

    received_key = unpickled_tuple[5]

    IV_dec = unpickled_tuple[6]

    bt = rand.randrange(4,floor(sqrt(p-1)),7)


    # Send shared Key to Alice

    my_shared_key = [ Bob_public_key(G,p,a,b,bt) ]

    my_shared_key = pickle.dumps(my_shared_key)

    conn[0].send(my_shared_key)

    my_private_key = Bob_private_key(received_key,p,a,b,bt)

    print(my_private_key[0])

    key = my_private_key[0]

####################################################

    key_str_len = 4* (round_num-6)

    spacebar = " "
    key_in_hex = hex(key)[2:]
    space_padding = binascii.hexlify( bytes(spacebar,'utf-8') ).decode('utf-8')

    key_set_in_hex_pair = [key_in_hex[i:i+2] for i in range(0,len(key_in_hex), 2)]
    
    padding = [space_padding for i in range(len(key_in_hex),2*key_str_len, 2)]
    key_set_in_hex_pair = key_set_in_hex_pair + padding

    print ("In HEX: ")
    for i in key_set_in_hex_pair:
        print ( '%02X' % int(i,16) ,end=' ')
    #print ( hex( int(i) )[2:] )
    print("\n\n")

#####################################################

    IV_in_hex = hex(IV_dec)[2:]
    IV_set_in_hex_pair = [IV_in_hex[i:i+2] for i in range(0,len(IV_in_hex), 2)]

    print ("In HEX: ")
    for i in IV_set_in_hex_pair:
        print ( '%02X' % int(i,16) ,end=' ')
        #print ( hex( int(i) )[2:] )
    print("\n\n")

    round_key_set = schedule_key(key_set_in_hex_pair,round_num) 


########################################################

    file_b = open(dir_path + "\\1905119_bfile.txt","w")

    data = conn[0].recv(1024).decode('utf-8')


    file_b.write(data)

    # data = conn[0].recv(1024).decode('utf-8')

    # print(data)

    # data = conn[0].recv(16*1024).decode('utf-8')

    # print(data)

    # while data:

    #     if not data :

    #         break

    #     else :

    #         file_b.write(data)
    #         data = conn[0].recv(1024).decode('utf-8')

    # print()

    print('Received')

    file_b.close()

    conn[0].close()





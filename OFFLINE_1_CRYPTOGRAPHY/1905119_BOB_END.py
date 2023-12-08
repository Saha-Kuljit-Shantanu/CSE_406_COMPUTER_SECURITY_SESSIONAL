import socket
import os 
import pickle
from KEYS_FOR_BOB import *
import random as rand
from math import sqrt,cbrt,floor,ceil
import binascii
from AES_METHODS import schedule_key,encrypt,decrypt
import threading
import numpy as np

def full_encrypt(nonse,key,round,text,counter,lock) :

    

    enc_text = encrypt(nonse,key,round)

    lock.acquire()
    
    print( counter, enc_text )

    lock.release()

    enc_text = [item for row in np.array(enc_text) for item in row]

    enc_text = [int(byte,16) for byte in np.array(enc_text)]

    enc_text = enc_text[:len(text)]

    text = [int(byte,16) for byte in np.array(text)]

    lock.acquire()

    print(counter, enc_text)

    print(counter, text)

    ctr_text = np.bitwise_xor(enc_text,text)

    print(counter, ctr_text)

    lock.release()

    message_chunks[counter] = [hex(c) for c in ctr_text ]

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

    data = conn[0].recv(1024*1024)

    Alice_shared_key_tuple = data



    # while data :

    #     if not data :

    #         #print("Done")
    #         break

    #     else : 

    #         Alice_shared_key_tuple = Alice_shared_key_tuple + data
    #         data = conn[0].recv(1024)

    unpickled_tuple = pickle.loads(Alice_shared_key_tuple)

    # Receive curve parametres and shared key from Alice

    print(unpickled_tuple[0],unpickled_tuple[1],unpickled_tuple[2],unpickled_tuple[3],unpickled_tuple[4]) #p,a,b,G,rn

    p = unpickled_tuple[0]

    a = unpickled_tuple[1]

    b = unpickled_tuple[2]

    G = unpickled_tuple[3]

    round_num = unpickled_tuple[4]

    received_key = unpickled_tuple[5]

    nonse_val = unpickled_tuple[6]

    bt = rand.randrange(4,floor(sqrt(p-1)),7)

    print()

    print("From Alice : " , received_key)


    # Send shared Key to Alice

    my_shared_key = [ Bob_public_key(G,p,a,b,bt) ]

    print()

    print(my_shared_key)

    print()

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

    round_key_set = schedule_key(key_set_in_hex_pair,round_num) 

    print(round_key_set)


#####################################################

    # IV_in_hex = hex(IV_dec)[2:]
    # IV_set_in_hex_pair = [IV_in_hex[i:i+2] for i in range(0,len(IV_in_hex), 2)]

    # print ("In HEX: ")
    # for i in IV_set_in_hex_pair:
    #     print ( '%02X' % int(i,16) ,end=' ')
    #     #print ( hex( int(i) )[2:] )
    # print("\n\n")

    # round_key_set = schedule_key(key_set_in_hex_pair,round_num) 


########################################################

    data = conn[0].recv(1024)
    
    Alice_msg = data



    while data :

        if not data :

            #print("Done")
            break

        else : 

            Alice_msg = Alice_msg + data
            data = conn[0].recv(1024)
            # print(Alice_msg)
            # print()

    unpickled_msg = pickle.loads(Alice_msg)

    cipher_text = unpickled_msg[0]

    threads = []
    message_chunks = []
    counter = 0

    num_chunks = ceil( len(cipher_text)/16 )

    for i in range(0,num_chunks,1):

        if i == num_chunks-1 :

            message_chunks.append( cipher_text[i*16:] )

        else :

            message_chunks.append( cipher_text[i*16:(i+1) * 16] )

    #print(message_chunks)

    lock = threading.Lock()
    
    for cipher_text in message_chunks :

        nonse_in_hex = hex(nonse_val+counter)[2:]
        nonse_set_in_hex_pair = [nonse_in_hex[i:i+2] for i in range(0,len(nonse_in_hex), 2)]

        threads.append( threading.Thread(target = full_encrypt,args = (nonse_set_in_hex_pair,round_key_set,round_num,cipher_text,counter,lock)) )
        threads[counter].start()
        counter = counter + 1

    counter = 0

    for plain_text in message_chunks :
        threads[counter].join()
        counter = counter + 1
    
    #print(message_chunks)

    plain_text = ""

    for text in message_chunks:
    
        for byte in text:

            plain_text = plain_text + chr(int(byte,16))

    #print(plain_text)

    out_file_name = dir_path + "\\1905119_bfile.txt"

    file_b = open(out_file_name,"wb")

    file_b.write( bytes(plain_text,encoding="utf-8") )



#######################################################

    # file_b = open(dir_path + "\\1905119_bfile.txt","w")

    # data = conn[0].recv(1024).decode('utf-8')


    # file_b.write(data)

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





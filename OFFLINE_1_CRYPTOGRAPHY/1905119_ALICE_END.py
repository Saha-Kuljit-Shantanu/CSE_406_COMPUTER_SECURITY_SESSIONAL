import socket
import os 
import pickle
from KEYS_FOR_ALICE import *
import random as rand
from sympy import randprime
import numpy as np
from math import sqrt,cbrt,floor
from AES_METHODS import schedule_key,encrypt
import binascii
import threading


dir_path = os.path.dirname(os.path.realpath(__file__))

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



if __name__ == '__main__' :

    host = '127.0.0.1'
    port = 8081

    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    sock.connect((host,port))

    print("Number of bits in AES \n")
    print(" 1) 128 ","\n","2) 192 " ,"\n","3) 256 \n")
    round_num = 0
    aes = input("Select any of 1,2,3: ")
    print("\n")

    while aes != "1" and aes != "2" and aes != "3":
        aes = input("Type again: Select any of 1,2,3 : ")

    a = 0
    b = 0
    p = 0
    nonse_dec = 0
    L128 = 0x12345678901234567890123456789012
    U128 = 0xfffffffdfffffffdfffffffdfffffffd
    L192 = 0x123456789012345678901234567890123456789012345678
    U192 = 0xfffffffdfffffffdfffffffdfffffffdfffffffdfffffffd
    L256 = 0x1234567890123456789012345678901234567890123456789f9f9f9f9f9f9f9f
    U256 = 0xfffffffdfffffffdfffffffdfffffffdfffffffdfffffffd0000000100000001

    if aes == "1" :
        round_num = 10
        p = randprime(L128,U128)        
        #nonse_dec = rand.randrange(L128,U128)
       
        

    if aes == "2" :
        round_num = 12
        p = randprime(L192,U192)  
        #nonse_dec = rand.randrange(L192,U192) 

    

    if aes == "3" :
        round_num = 14
        p = randprime(L256,U256)
        #nonse_dec = rand.randrange(L256,U256)        

    n = 0
    while(n == 0) :
        a = rand.randrange(2,10000000,5)
        x = rand.randrange(2,10000000,5)
        y = rand.randrange(2,10000000,5)

        
        b = y*y - x*x*x - a*x 
        b = b%p 
        n = 4*a*a*a + 27* b*b
        n = n%p  

    nonse_dec = rand.randrange(L128,U128)

    G = [x,y]

    at = rand.randrange( 4,floor(sqrt(p-1)),7 )

    # Send curve parametres and shared key to Bob

    my_shared_key = Alice_public_key(G,p,a,b,at)

    #tuple = [ { 'a':10, 'b':20, 'g':22 ,'key' : "Thats my Kung Fu"} ] 

    Alice_shared_key_tuple = [p,a,b,G,round_num,my_shared_key,nonse_dec]

    print(Alice_shared_key_tuple)

    print()

    pickled_tuple = pickle.dumps(Alice_shared_key_tuple)

    sock.send(pickled_tuple)



    #Receive shared key from Bob

    _data = sock.recv(1024*1024)
    
    data = _data



    # while _data :

    #     if not _data :

    #         #print("Done")
    #         break

    #     else : 

    #         data = data + _data
    #         _data = sock.recv(1024)

    #data = sock.recv(1024)

    received_key = pickle.loads(data)

    print(received_key[0])

    my_private_key = Alice_private_key(received_key[0],p,a,b,at)

    print( my_private_key[0])

    key = my_private_key[0]

###############################################################

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

 ################################################################
 #    #data = encrypt()

    nonse_val = nonse_dec

    # print ("In HEX: ")
    # for i in IV_set_in_hex_pair:
    #     print ( '%02X' % int(i,16) ,end=' ')
    #     #print ( hex( int(i) )[2:] )
    # print("\n\n")

    round_key_set = schedule_key(key_set_in_hex_pair,round_num) 

    print(round_key_set)


 ###############################################################

    null = "\0"

    #= file_in = open(,"r")

    filename = dir_path + "\\1905119_afile.txt"

    with open(filename, "rb") as file_in:
        plain_text = file_in.read()

    message_in_hex = plain_text.hex()

    #message_in_hex = binascii.hexlify( bytes(plain_text, 'utf-8') ).decode('utf-8')
    null_padding = binascii.hexlify( bytes(null,'utf-8') ).decode('utf-8')

    msg_len = len(message_in_hex)
    pad_len = 31 - (msg_len-1)%32
    tot_len = msg_len + pad_len
    num_chunks = tot_len//32

    message_set_in_hex_pair = [message_in_hex[i:i+2] for i in range(0,msg_len, 2)]
    padding = [null_padding for i in range(msg_len,tot_len, 2)]

    #message_set_in_hex_pair = message_set_in_hex_pair + padding

    # print ("In HEX: ")
    # for i in message_set_in_hex_pair:
    #     print ( '%02X' % int(i,16) ,end=' ')
    #     #print ( hex( int(i) )[2:] )
    # print("\n\n")

    message_chunks = []


    for i in range(0,num_chunks,1):

        if i == num_chunks-1 :

            message_chunks.append( message_set_in_hex_pair[i*16:] )

        elif i == 0 :

            message_chunks.append( message_set_in_hex_pair[:(i+1)*16] )

        else:
        
            message_chunks.append( message_set_in_hex_pair[i*16:(i+1) * 16] )
            #print(len(message_chunks[i]))


    threads = []
    counter = 0

    #print(message_chunks)

    lock = threading.Lock()
    
    for plain_text in message_chunks :

        nonse_in_hex = hex(nonse_val+counter)[2:]
        nonse_set_in_hex_pair = [nonse_in_hex[i:i+2] for i in range(0,len(nonse_in_hex), 2)]

        threads.append( threading.Thread(target = full_encrypt,args = (nonse_set_in_hex_pair,round_key_set,round_num,plain_text,counter,lock)) )
        threads[counter].start()
        counter = counter + 1

    counter = 0

    for plain_text in message_chunks :
        threads[counter].join()
        counter = counter + 1
    
    #print(message_chunks)

    cipher_text = []

    for text in message_chunks:
    
        for byte in text:

            cipher_text.append( byte )

    #print(cipher_text)

        
    Alice_msg = [cipher_text]

    pickled_msg = pickle.dumps(Alice_msg)

    sock.send(pickled_msg)

    # while True :

    #     try : 

    #         file_in = open(dir_path + "\\1905119_afile.txt","r")

    #         data = file_in.read()

    #         if not data : 

    #             break

    #         while data :

    #             sock.send(str(data).encode('utf-8'))

    #             data = file_in.read()

    #         file_in.close()

    #         break

    #     except IOError :

    #         print("You have entered an invalid filename")


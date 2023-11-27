from RESOURCES import *
from AES_HELPER import add_round_key
from AES_HELPER import substitute_byte
from AES_HELPER import shift_row
from AES_HELPER import mix_columns
from AES_HELPER import update_text
import binascii
import numpy as np
import time as t




def g(w3,rc):

    w3 = np.roll(w3,-1)

    #print(w3)
    s = [Sbox[ int(w3[i],16) ] for i in range(0,len(w3), 1)]

    #print(s)

    #s_int = [ int(s[i],16) for i in range(0,len(s), 1)]
    g_int = [ rc[i]^s[i] for i in range(0,len(s), 1)]
    #g_hex = [ hex(g_int[i]) for i in range(0,len(g_int), 1)]
    return g_int


def expand_key_128(rk,rc):

    w_hex = []

    w_int = []

    w = []

    for i in range(0,4,1):

        w_hex.append( rk[i*(len(rk)//4):(i+1) * (len(rk)//4)] )

    #print(w[3])

    u = g(w_hex[3],rc)

    #print(w[3])

    #print(u)

    for i in range(0,4,1):

        w_int.append( [ int(w_hex[i][j],16) for j in range(0,len(w_hex[i]), 1)] )
        w_int[i] = [ u[j] ^ w_int[i][j] for j in range(0,len(w_int[i]), 1)]
        u = w_int[i]
        w.append( [ hex(w_int[i][j]) for j in range(0,len(w_int[i]), 1) ])

    #rk = [int(key_set_in_hex_pair[i],16) for i in range(0,len(key_set_in_hex_pair), 1)]

    #print(w)

    for i in range(0,4,1):

        for j in range(0,4,1):

            rk[4*i+j] = w[i][j]

    return rk


def schedule_key():

    rk = [round_key]
    
    #rk.append()
    #print(rk)

    for c in range(0,round_num,1) : 

        if round_num == 10:
            rcon = [r128[c], 0, 0 , 0]      

            temp_round_key = rk[c][:]

            #print(rk)
            
            temp_round_key = expand_key_128(temp_round_key,rcon)

            rk.extend( [temp_round_key] )
            #print(rk)

        if round_num == 12:
            rcon = [r192[c], 0, 0 , 0]

        if round_num == 14:
            rcon = [r256[c], 0, 0 , 0]

    return rk

def encrypt(text):

    for i in range (0,round_num,1):
    

    #print(key_set_in_hex_pair)

    #print( np.bitwise_xor(round_key , updated_text) )

    #print(round_key[i])

        xor_set_dec = add_round_key(round_key[i],text)

        sub_byte_set_dec = substitute_byte(xor_set_dec)

        shift_row_set_dec = shift_row(sub_byte_set_dec)

    

    #print(shift_row_set_dec)

    #print(sub_byte_set_dec)

    #print( np.bitwise_xor( np.array( round_key_matrix ) , np.array( updated_text_matrix ) ) )
   

        if( i != round_num-1 ) :
        
            mixed_col_set_dec = mix_columns(shift_row_set_dec)

            text = update_text(mixed_col_set_dec)

        else :

            text = update_text(shift_row_set_dec)

            text = np.mat(text).reshape(4,4)

            text.shape

            text = text.transpose()


            text = add_round_key(round_key[i+1],text)

            text = np.mat(text).reshape(4,4)

            text.shape

            text = text.transpose()

            #print(round_key_matrix_hex)

            text = [[hex(j) for j in row] for row in np.array(text)]

    return text       
    
print("Number of bits in AES \n")
print(" 1) 128 ","\n","2) 192 " ,"\n","3) 256 \n")
round_num = 0
aes = input("Select any of 1,2,3: ")
print("\n")

while aes != "1" and aes != "2" and aes != "3":
    aes = input("Type again: Select any of 1,2,3 : ")

if aes == "1" :
    round_num = 10

if aes == "2" :
    round_num = 12

if aes == "3" :
    round_num = 14



print("Key:")
key = input("In ASCII: ")

spacebar = " "
key_in_hex = binascii.hexlify( bytes(key, 'utf-8') ).decode('utf-8')
space_padding = binascii.hexlify( bytes(spacebar,'utf-8') ).decode('utf-8')

key_set_in_hex_pair = [key_in_hex[i:i+2] for i in range(0,len(key_in_hex), 2)]

if round_num == 10:
    
    padding_128 = [space_padding for i in range(len(key_in_hex),32, 2)]
    key_set_in_hex_pair = key_set_in_hex_pair + padding_128

print ("In HEX: ")
for i in key_set_in_hex_pair:
    print ( '%02X' % int(i,16) ,end=' ')
    #print ( hex( int(i) )[2:] )
print("\n\n")


print("Plain Text:")
plain_text = input("In ASCII: ")
null = "\0"

message_in_hex = binascii.hexlify( bytes(plain_text, 'utf-8') ).decode('utf-8')
null_padding = binascii.hexlify( bytes(null,'utf-8') ).decode('utf-8')

msg_len = len(message_in_hex)
pad_len = 31 - (msg_len-1)%32
tot_len = msg_len + pad_len
num_chunks = tot_len//32

message_set_in_hex_pair = [message_in_hex[i:i+2] for i in range(0,msg_len, 2)]
padding = [null_padding for i in range(msg_len,tot_len, 2)]

message_set_in_hex_pair = message_set_in_hex_pair + padding

print ("In HEX: ")
for i in message_set_in_hex_pair:
    print ( '%02X' % int(i,16) ,end=' ')
    #print ( hex( int(i) )[2:] )
print("\n\n")

# key_in_hex = hex( key )
# space_padding = hex( spacebar )

message_chunks = []


for i in range(0,num_chunks,1):

    message_chunks.append( message_set_in_hex_pair[i*(len(message_set_in_hex_pair))//num_chunks:(i+1) * (len(message_set_in_hex_pair))//num_chunks] )




#print(key_set_in_hex_pair,message_set_in_hex_pair)

round_key = key_set_in_hex_pair

key_schedule_time = 0

encryption_time = 0

decryption_time = 0

r128 = [1,2,4,8,16,32,64,128,27,54]
r192 = [1,1,1,2,4,4,8,16,16,32,32,32,64]
r256 = [1,1,1,1,2,2,4,4,8,8,8,8,16,16,32]

key_schedule_time = t.time()

round_key = schedule_key() 

key_schedule_time = t.time() - key_schedule_time

key_schedule_time = key_schedule_time * 1000

#print(round_key)

cipher_text_hex = []
cipher_text = []
cipher_text_str = ""

encryption_time = t.time()



for plain_text in message_chunks :

    #print(plain_text)

    cipher_text_hex = cipher_text_hex + encrypt(plain_text)

for text in cipher_text_hex:
    
    for byte in text:

        cipher_text.append( byte )

for byte in cipher_text :

    cipher_text_str = cipher_text_str + chr(int(byte,16)) 


print("Ciphered Text: ")

print("In HEX: ")

for i in cipher_text:
    print ( '%02X' % int(i,16) ,end=' ' )

print("\n")

print("In ASCII: ",cipher_text_str,"\n\n")

encryption_time = t.time() - encryption_time

encryption_time = encryption_time *1000

print("Key Schedule Time : " ,key_schedule_time," sec")
print("Encryption Time : ",encryption_time," sec")







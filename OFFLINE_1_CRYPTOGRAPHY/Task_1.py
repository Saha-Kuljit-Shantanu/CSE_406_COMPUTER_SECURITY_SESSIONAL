from RESOURCES import *
from AES_METHODS import schedule_key,encrypt,decrypt
import binascii
import time as t

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

key_str_len = 4* (round_num-6)



print("Key: (Maximum %d characters)" %(key_str_len))
key = input("In ASCII: ")

while(len(key) > key_str_len) :

    key = input("Your input exceeds %d characters. Please try again with appropriate length: " %(key_str_len) )



spacebar = " "
key_in_hex = binascii.hexlify( bytes(key, 'utf-8') ).decode('utf-8')
space_padding = binascii.hexlify( bytes(spacebar,'utf-8') ).decode('utf-8')

key_set_in_hex_pair = [key_in_hex[i:i+2] for i in range(0,len(key_in_hex), 2)]
    
padding = [space_padding for i in range(len(key_in_hex),2*key_str_len, 2)]
key_set_in_hex_pair = key_set_in_hex_pair + padding

print ("In HEX: ")
for i in key_set_in_hex_pair:
    print ( '%02X' % int(i,16) ,end=' ')
    #print ( hex( int(i) )[2:] )
print("\n\n")

print("Initializing Vector: (Maximum 16 characters)")
init_vector = input("In ASCII: ")

while(len(init_vector) > 16) :

    init_vector = input("Initial Vector cannot be exceeding 16 characters, please try again with appropriate length: ")

init_vector_in_hex = binascii.hexlify( bytes(init_vector, 'utf-8') ).decode('utf-8')

init_vector_in_hex_pair = [init_vector_in_hex[i:i+2] for i in range(0,len(init_vector_in_hex), 2)]
    
padding = [space_padding for i in range(len(init_vector_in_hex),32, 2)]
init_vector_in_hex_pair = init_vector_in_hex_pair + padding

print ("In HEX: ")
for i in init_vector_in_hex_pair:
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

key_schedule_time = t.time()

round_key_set = schedule_key(round_key,round_num) 

# for key in round_key_set:
#     for byte in key:
#         print ( '%02X' % int(byte,16) ,end=' ' )
#     print("\n")

key_schedule_time = t.time() - key_schedule_time

key_schedule_time = key_schedule_time * 1000

#print(round_key)

cipher_text_hex = []
cipher_text = []
cipher_text_str = ""



encryption_time = t.time()

carry_out_text = init_vector_in_hex_pair



for plain_text in message_chunks :

    #print(plain_text)
    plain_text = [int(byte,16) for byte in np.array(plain_text)]

    carry_out_text = [int(byte,16) for byte in np.array(carry_out_text)]

    plain_text = np.bitwise_xor(plain_text,carry_out_text)

    plain_text = [hex(byte) for byte in np.array(plain_text)]

    carry_out_text = encrypt(plain_text,round_key_set,round_num)

    cipher_text_hex = cipher_text_hex + carry_out_text

    carry_out_text = [item for row in np.array(carry_out_text) for item in row ]

for text in cipher_text_hex:
    
    for byte in text:

        cipher_text.append( byte )

for byte in cipher_text :

    cipher_text_str = cipher_text_str + chr(int(byte,16)) 

    #pass cipher_text to decrypt


print("Ciphered Text: ")

print("In HEX: ")

for i in cipher_text:
    print ( '%02X' % int(i,16) ,end=' ' )

print("\n")

print("In ASCII:",cipher_text_str,"\n\n")

encryption_time = t.time() - encryption_time

encryption_time = encryption_time *1000

plain_text_hex = []
plain_text = []
plain_text_str = ""

decryption_time = t.time()

cipher_text_chunks = []

for i in range(0,num_chunks,1):

    cipher_text_chunks.append( cipher_text[i*(len(message_set_in_hex_pair))//num_chunks:(i+1) * (len(message_set_in_hex_pair))//num_chunks] )


carry_out_text = init_vector_in_hex_pair

for cipher_text in cipher_text_chunks :

    #print(plain_text)
    appendive_plain_text_matrix = decrypt(cipher_text,round_key_set,round_num)

    appendive_plain_text = [item for row in np.array(appendive_plain_text_matrix) for item in row]

    appendive_plain_text = [int(byte,16) for byte in np.array(appendive_plain_text)]

    carry_out_text = [int(byte,16) for byte in np.array(carry_out_text)]

    appendive_plain_text = np.bitwise_xor(appendive_plain_text,carry_out_text)

    #appendive_plain_text = [hex(byte) for byte in np.array(appendive_plain_text)]

    carry_out_text = cipher_text

    appendive_plain_text_matrix = np.mat(appendive_plain_text).reshape(4,4)

    appendive_plain_text_matrix.shape

    appendive_plain_text_matrix = update_text(appendive_plain_text_matrix)

    plain_text_hex = plain_text_hex + appendive_plain_text_matrix



for text in plain_text_hex:
    
    for byte in text:

        plain_text.append( byte )

for byte in plain_text :

    plain_text_str = plain_text_str + chr(int(byte,16)) 

    #pass cipher_text to decrypt


print("Deciphered Text: ")

print("In HEX: ")

for i in plain_text:
    print ( '%02X' % int(i,16) ,end=' ' )

print("\n")

print("In ASCII:",plain_text_str,"\n\n")

decryption_time = t.time() - decryption_time

decryption_time = decryption_time *1000

print("Key Schedule Time :" ,key_schedule_time,"sec")
print("Encryption Time   :",encryption_time,"sec")
print("Decryption Time   :",decryption_time,"sec")

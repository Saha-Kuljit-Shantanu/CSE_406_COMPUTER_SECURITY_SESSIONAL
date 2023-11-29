from RESOURCES import *
from AES_HELPER_METHODS import add_round_key
from AES_HELPER_METHODS import substitute_byte,inv_substitute_byte
from AES_HELPER_METHODS import shift_row,inv_shift_row
from AES_HELPER_METHODS import mix_columns
from AES_HELPER_METHODS import update_text

r128 = [1,2,4,8,16,32,64,128,27,54]
r192 = [1,1,1,2,4,4,8,16,16,32,32,32,64]
r256 = [1,1,1,1,2,2,4,4,8,8,8,8,16,16,32]


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


def schedule_key(key,round_num):

    rk = [key]
    
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

def encrypt(text,keyset,round_num):

    for i in range (0,round_num,1):
    

    #print(key_set_in_hex_pair)

    #print( np.bitwise_xor(round_key , updated_text) )

    #print(round_key[i])

        xor_set_dec = add_round_key(keyset[i],text)

        sub_byte_set_dec = substitute_byte(xor_set_dec)

        shift_row_set_dec = shift_row(sub_byte_set_dec)

    

    #print(shift_row_set_dec)

    #print(sub_byte_set_dec)

    #print( np.bitwise_xor( np.array( round_key_matrix ) , np.array( updated_text_matrix ) ) )
   

        if( i != round_num-1 ) :
        
            mixed_col_set_dec = mix_columns(shift_row_set_dec,0)

            text = update_text(mixed_col_set_dec)

        else :

            text = update_text(shift_row_set_dec)

            text = transpose(text)


            text = add_round_key(keyset[i+1],text)

            text = transpose(text)

            #print(round_key_matrix_hex)

            text = update_text(text)

    return text     

def decrypt(text,keyset,round_num) :

    #reverse the key
    #text = transpose(text)

    #text = text.tolist()

    pass_dec = add_round_key(keyset[round_num],text)

    #print(pass_dec)

    for i in range(round_num-1,-1,-1):

        # pass_dec = transpose(pass_dec)

        # pass_dec = pass_dec.tolist()

        inv_shift_row_set_dec = inv_shift_row(pass_dec)
        
        #print("After Shift Row: " ,inv_shift_row_set_dec)

        inv_sub_byte_set_hex = inv_substitute_byte(inv_shift_row_set_dec)

        #print("After Sub Byte: " ,inv_sub_byte_set_hex)

        inv_sub_byte_set_hex = transpose(inv_sub_byte_set_hex)

        pass_dec = add_round_key(keyset[i], inv_sub_byte_set_hex)

        #pass_dec = transpose( pass_dec )

        #print("After Round Key: " ,pass_dec)

        

        if( i != 0 ) :
        
            pass_dec = mix_columns(pass_dec,1)

            pass_dec = transpose(pass_dec)

            #print("After Mix Col: " ,pass_dec)

        pass_dec = pass_dec.tolist()


    pass_dec = transpose(pass_dec)
    pass_text =  update_text(pass_dec)

    #print(pass_text)

    return pass_text





    







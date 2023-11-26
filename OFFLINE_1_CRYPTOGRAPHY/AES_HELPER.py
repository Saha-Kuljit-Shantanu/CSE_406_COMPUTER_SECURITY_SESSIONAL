import numpy as np
from RESOURCES import *

def add_round_key(key,text) :

    round_key_matrix_hex = np.mat(key).reshape(4,4)

    round_key_matrix_hex.shape

    round_key_matrix_hex = round_key_matrix_hex.transpose()

    updated_text_matrix_hex = np.mat(text).reshape(4,4)

    updated_text_matrix_hex.shape

    updated_text_matrix_hex = updated_text_matrix_hex.transpose()

    #print(round_key_matrix_hex)

    round_key_set_dec = [[int(i,16) for i in row] for row in np.array(round_key_matrix_hex)]

    updated_text_set_dec = [[int(i,16) for i in row] for row in np.array(updated_text_matrix_hex)]

    updated_text_set_dec = np.bitwise_xor( round_key_set_dec, updated_text_set_dec)

    #updated_text_set_hex = [[hex(i) for i in row] for row in np.array(updated_text_set_dec)]

    #updated_text_matrix_hex = np.mat(updated_text_set_hex).reshape(4,4)

    #updated_text_matrix_hex.shape

    return updated_text_set_dec

    

    #print(updated_text_matrix_hex)

def substitute_byte(xor_set_dec):

    sub_byte_set_dec = []

    for i in range(0,4,1):
        
        sub_byte_set_dec.append( [Sbox[ xor_set_dec[i][j] ] for j in range(0,len(xor_set_dec), 1) ] )
        

    #print(sub_byte_set)

    return sub_byte_set_dec

def shift_row(sub_byte_set_dec):

    shift_row_set_dec = sub_byte_set_dec

    for i in range(0,len(shift_row_set_dec),1):

        shift_row_set_dec[i] = np.roll(shift_row_set_dec[i],-i)

    return shift_row_set_dec

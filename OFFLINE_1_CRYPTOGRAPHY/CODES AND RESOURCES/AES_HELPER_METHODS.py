from RESOURCES import *





def add_round_key(key,text) :

    # round_key_matrix_hex = np.mat(key).reshape(4,4)

    # round_key_matrix_hex.shape

    # round_key_matrix_hex = round_key_matrix_hex.transpose()

    round_key_matrix_hex = transpose(key)

    # updated_text_matrix_hex = np.mat(text).reshape(4,4)

    # updated_text_matrix_hex.shape

    # updated_text_matrix_hex = updated_text_matrix_hex.transpose()

    updated_text_matrix_hex = transpose(text)

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

def inv_substitute_byte(inv_shift_row_set_dec):

    inv_sub_byte_set_hex = []

    for i in range(0,4,1):
        
        inv_sub_byte_set_hex.append  (   [ hex( InvSbox[ inv_shift_row_set_dec[i][j] ] ) for j in range(0,4, 1 ) ] )

        
    # for i in range(0,len(inv_shift_row_set_dec),1):
        
    #     inv_sub_byte_set_hex.append(  [hex( InvSbox[ inv_shift_row_set_dec[j][i] ] ) for j in range(0,4, 1) ] )
    # #print(sub_byte_set)

    return inv_sub_byte_set_hex



def shift_row(sub_byte_set_dec):

    shift_row_set_dec = sub_byte_set_dec

    for i in range(0,len(shift_row_set_dec),1):

        shift_row_set_dec[i] = np.roll(shift_row_set_dec[i],-i)

    return shift_row_set_dec

def inv_shift_row(sub_byte_set_dec):

    inv_shift_row_set_dec = sub_byte_set_dec

    # inv_shift_row_matrix = np.mat(inv_shift_row_set_dec).reshape(4,4)

    # inv_shift_row_matrix.shape

    # inv_shift_row_matrix = inv_shift_row_matrix.transpose()

    # inv_shift_row_matrix = transpose(inv_shift_row_set_dec)

    # inv_shift_row_set_dec = inv_shift_row_matrix.tolist()

    for i in range(0,len(inv_shift_row_set_dec),1):

        inv_shift_row_set_dec[i] = np.roll(inv_shift_row_set_dec[i],i)

    return inv_shift_row_set_dec

def galois_multiplication(a, b):

    #b = b.intValue()

    if b == 1:
        return a
    
    tmp = (a << 1) & 0xff
    if b == 2 and a < 128:
        return tmp  
    
    if b == 2 and a >= 128:
        return tmp ^ 0x1b

    if b == 3:
        return galois_multiplication(a, 2) ^ a
    
    if b == 9:
        return galois_multiplication( galois_multiplication( galois_multiplication( a,2 ),2 ),2) ^a 
    
    if b == 11:
        return galois_multiplication( galois_multiplication( galois_multiplication( a,2 ),2 ) ^ a,2 ) ^a
    
    if b == 13:
        return galois_multiplication( galois_multiplication( galois_multiplication( a,2 ) ^ a,2 ) ,2 ) ^a
    
    if b == 14:
        return galois_multiplication( galois_multiplication( galois_multiplication( a,2 ) ^ a,2 ) ^a ,2 ) 
    
def mix_columns_set(shift_row_vector,is_Inverting):

    mcolset =[]
    entry = 0

    for i in range( 0, 4, 1 ):

        for j in range( 0, 4, 1 ):

            if is_Inverting == 0 :
                entry = entry ^ galois_multiplication(shift_row_vector[j],Mixer[i][j].intValue() )

            else :

                entry = entry ^ galois_multiplication(shift_row_vector[j],InvMixer[i][j].intValue() )
        
        #print( int( Mixer[i][j] ) )

        mcolset.append(entry)

        entry = 0

    return mcolset

def mix_columns(shift_row_set_dec,is_Inverting):

    # shift_row_set_dec = np.mat(shift_row_set_dec).reshape(4,4)

    # shift_row_set_dec.shape

    # shift_row_set_dec = shift_row_set_dec.transpose()

    shift_row_mat = transpose(shift_row_set_dec)

    mixed_column_dec = []

    for x in np.array(shift_row_mat):

        mixed_column_dec.append( mix_columns_set(x,is_Inverting) )
        #print(x)

    # mixed_column_dec = np.mat(mixed_column_dec).reshape(4,4)

    # mixed_column_dec.shape

    # mixed_column_dec = mixed_column_dec.transpose()

    #print(mixed_column_dec)

    return mixed_column_dec






    

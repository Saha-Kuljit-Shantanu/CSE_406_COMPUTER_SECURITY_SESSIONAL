from ECDH_HELPER_METHODS import key_gen

def Bob_public_key(G,p,a,b,bob) :

    bobG = key_gen(G,p,a,b,bob)   
    return bobG
    


def Bob_private_key(alice_public_key,p,a,b,bob) :

    return key_gen(alice_public_key,p,a,b,bob)
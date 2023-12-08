from ECDH_HELPER_METHODS import key_gen

def Alice_public_key(G,p,a,b,alice) :

    aliceG = key_gen(G,p,a,b,alice)
    return aliceG

def Alice_private_key(bob_public_key,p,a,b,alice) :

    return key_gen(bob_public_key,p,a,b,alice)
from ECDH_HELPER_METHODS import key_gen
import random as rand
import time

p128 = 0xfffffffdffffffffffffffffffffffff
a128 = 0xfffffffdfffffffffffffffffffffffc
b128 = 0xe87579c11079f43dd824993c2cee5ed3
E128 = 0xfffffffe0000000075a30d1b9038a115
G128 = [0x161ff7528b899b2d0c28607ca52c5b86, 0xcf5ac8395bafeb13c02da292dded7a83]

p256 = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff
a256 = 0xffffffff00000001000000000000000000000000fffffffffffffffffffffffc
b256 = 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b
E256 = 0xffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551
G256 = [0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296, 0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5]


def Alice_public_key(G,p,a,b,alice) :

    aliceG = key_gen(G,p,a,b,alice)
    return aliceG

def Bob_public_key(G,p,a,b,bob) :

    bobG = key_gen(G,p,a,b,bob)   
    return bobG
    
def Alice_private_key(bob_public_key,p,a,b,alice,) :

    return key_gen(bob_public_key,p,a,b,alice)

def Bob_private_key(alice_public_key,p,a,b,bob) :

    return key_gen(alice_public_key,p,a,b,bob)

# print( "Result: ", Alice_public_key() )
# print( "Result: ", Bob_public_key() )
# print( "Result: ", Alice_private_key() )
# print( "Result: ", Bob_private_key() )

alice_time = 0
bob_time = 0
secret_key_time = 0
trial_num = 5


for i in range (0,trial_num,1) :

    alice = rand.randrange(2,E128-1,i+1)

    _time = time.time()
    Ka = Alice_public_key(G128,p128,a128,b128,alice)
    alice_time = alice_time + time.time() - _time

    bob = rand.randrange(2,E128-1,i+2)

    _time = time.time()
    Kb = Bob_public_key(G128,p128,a128,b128,bob)
    bob_time = bob_time + time.time() - _time

    _time = time.time()
    U = Alice_private_key(Kb,p128,a128,b128,alice)
    V = Bob_private_key(Ka,p128,a128,b128,bob)
    secret_key_time = secret_key_time + time.time() - _time

    if U[0] == V[0] and U[1] == V[1] :
        print(" 128 bit keys for Trial", i+1, "are matching")

print("Average time for generating a 128 bit public key for Alice in", trial_num, "trials :" , alice_time*1000/trial_num , "seconds")
print("Average time for generating a 128 bit public key for Bob in", trial_num ,"trials :" , bob_time*1000/trial_num , "seconds")
print("Average time for generating a 128 bit secret key for both in", trial_num ,"trials :" , secret_key_time*500/trial_num , "seconds")

print("\n")

for i in range (0,trial_num,1) :

    alice = rand.randrange(2,E256-1,i+1)

    _time = time.time()
    Ka = Alice_public_key(G256,p256,a256,b256,alice)
    alice_time = alice_time + time.time() - _time

    bob = rand.randrange(2,E256-1,i+2)

    _time = time.time()
    Kb = Bob_public_key(G256,p256,a256,b256,bob)
    bob_time = bob_time + time.time() - _time

    _time = time.time()
    U = Alice_private_key(Kb,p256,a256,b256,alice)
    V = Bob_private_key(Ka,p256,a256,b256,bob)
    secret_key_time = secret_key_time + time.time() - _time

    if U[0] == V[0] and U[1] == V[1] :
        print(" 256 bit keys for Trial", i+1, "are matching")

print("Average time for generating a 256 bit public key for Alice in", trial_num ,"trials :" , alice_time*1000/trial_num , "seconds")
print("Average time for generating a 256 bit public key for Bob in", trial_num ,"trials :" , bob_time*1000/trial_num , "seconds")
print("Average time for generating a 256 bit secret key for both in", trial_num ," trials :" , secret_key_time*500/trial_num , "seconds")


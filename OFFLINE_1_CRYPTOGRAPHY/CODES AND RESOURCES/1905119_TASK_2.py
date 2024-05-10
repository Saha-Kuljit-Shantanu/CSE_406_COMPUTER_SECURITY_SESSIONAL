from RESOURCES import *
from EC_VALUES import *
from KEYS_FOR_ALICE import *
from KEYS_FOR_BOB import *
import random as rand
import time

# print( "Result: ", Alice_public_key() )
# print( "Result: ", Bob_public_key() )
# print( "Result: ", Alice_private_key() )
# print( "Result: ", Bob_private_key() )

alice_time = 0
bob_time = 0
secret_key_time = 0
trial_num = 10


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
        print(" 128 bit private keys for Trial", i+1, "are matching")

print("Average time for generating a 128 bit public key for Alice in", trial_num, "trials :" , alice_time*1000/trial_num , "seconds")
print("Average time for generating a 128 bit public key for Bob in", trial_num ,"trials :" , bob_time*1000/trial_num , "seconds")
print("Average time for generating a 128 bit secret key for both in", trial_num ,"trials :" , secret_key_time*500/trial_num , "seconds")

print("\n")

for i in range (0,trial_num,1) :

    alice = rand.randrange(2,E192-1,i+1)

    _time = time.time()
    Ka = Alice_public_key(G192,p192,a192,b192,alice)
    alice_time = alice_time + time.time() - _time

    bob = rand.randrange(2,E192-1,i+2)

    _time = time.time()
    Kb = Bob_public_key(G192,p192,a192,b192,bob)
    bob_time = bob_time + time.time() - _time

    _time = time.time()
    U = Alice_private_key(Kb,p192,a192,b192,alice)
    V = Bob_private_key(Ka,p192,a192,b192,bob)
    secret_key_time = secret_key_time + time.time() - _time

    if U[0] == V[0] and U[1] == V[1] :
        print(" 192 bit private keys for Trial", i+1, "are matching")

print("Average time for generating a 192 bit public key for Alice in", trial_num, "trials :" , alice_time*1000/trial_num , "seconds")
print("Average time for generating a 192 bit public key for Bob in", trial_num ,"trials :" , bob_time*1000/trial_num , "seconds")
print("Average time for generating a 192 bit secret key for both in", trial_num ,"trials :" , secret_key_time*500/trial_num , "seconds")

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
        print(" 256 bit private keys for Trial", i+1, "are matching")

print("Average time for generating a 256 bit public key for Alice in", trial_num ,"trials :" , alice_time*1000/trial_num , "seconds")
print("Average time for generating a 256 bit public key for Bob in", trial_num ,"trials :" , bob_time*1000/trial_num , "seconds")
print("Average time for generating a 256 bit secret key for both in", trial_num ," trials :" , secret_key_time*500/trial_num , "seconds")


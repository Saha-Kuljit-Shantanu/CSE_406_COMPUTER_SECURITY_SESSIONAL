from RESOURCES import *

def MOD(numerator,denominator,p) :

    t = 0
    r = p
    new_t = 1
    new_r = denominator

    while new_r != 0: 

        fraction = r//new_r
        #print(fraction)

        t_temp = new_t
        r_temp = new_r

        new_t = t -fraction*new_t
        new_r = r -fraction*new_r

        t = t_temp
        r= r_temp

    if t<0 :

        t = t+ p

    return (numerator*t)%p

def slope_Point(U,V,p,a,b):

    if U[0] == V[0] and U[1] == V[1] :
        
        numerator = 3 * U[0] * U[0] + a
        denominator = 2 * U[1]

    else :

        numerator = V[1] - U[1]
        denominator = V[0] - U[0]

    # if numerator < 0:

    #     numerator = - numerator

    if denominator < 0:

        numerator = - numerator
        denominator = - denominator


    fraction = numerator/denominator

    if numerator%denominator == 0 :

        return fraction%p
        
    else:

        return MOD(numerator,denominator,p)


def mul_Point(U,V,p,a,b):

    #print(slope_Point(U,V,p,a,b),U,V)

    W = [0,0]
    W[0] = slope_Point(U,V,p,a,b)* slope_Point(U,V,p,a,b) - U[0] -V[0]
    
    W[0] = W[0]%p

    W[1] = slope_Point(U,V,p,a,b)*(U[0] - W[0]) - U[1]

    W[1] = W[1]%p

    return W

def key_gen(G,p,a,b,k):

    T = G[:]

    x = BitVector(intVal = k)

    for i in range(1,len(x),1):

        T = mul_Point(T,T,p,a,b)

        if x[i] == 1: 

            T = mul_Point(T,G,p,a,b)

        #print(T)

        

    return T

#print(MOD(-5,-9,17))
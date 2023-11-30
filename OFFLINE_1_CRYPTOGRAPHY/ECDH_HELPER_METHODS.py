from RESOURCES import *

def MOD(numerator,denominator,p) :

    t = 0
    r = p
    new_t = 1
    new_r = denominator

    while new_r != 0: 

        fraction = int(r/new_r)
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

        fraction = numerator/denominator

        if numerator/denominator == 0 :

            return fraction%p

    else :

        numerator = V[1] - U[1]
        denominator = V[0] - U[0]

        fraction = numerator/denominator

        if numerator/denominator == 0 :

            return fraction%p


def mul_Point(U,V,p,a,b):

    W =[0,0]
    W[0] = slope_Point(U,V,p,a,b)* slope_Point(U,V,p,a,b) - U[0] -U[1]
    W[0] = W[0]%p
    W[1] = slope_Point(U,V,p,a,b)*(U[0] - W[0]) - U[1]
    W[1] = W[1]%p

#print(MOD(1,2,11))
# -*- coding : utf-8 -*-
import math

####################
###Excercice 1.a####
####################
def polynome(x):
    #retourner la formule
    return x**3 - 1.5 * (x** 2) - 6 * x + 5


#test la function
print(polynome(5))

####################
###Excercice 1.b####
####################

def factorielle(n):
    #on utilise la récursif
    if n == 1:
        return 1
    else:
        return n * factorielle(n-1)


#test la factorielle
print(factorielle(6))

####################
###Excercice 1.c####
####################

def fibonnaci(n):
	#on utilise la récursif
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else: 
        return fibonnaci(n-1) + fibonnaci(n-2)


#test la factorielle
print(fibonnaci(8))
 
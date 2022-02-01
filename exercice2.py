# -*- coding : utf-8 -*-
import math 

####################
###Excercice 2####
####################

"""
       Make a function of the exercise in the previous notebook: Given the dictionary `dd`,
       check if a key is already existing in the dictionary and raise an exception if the key 
       already exist. Otherwise, return the dict with the element added.
 """
def check_key(dd,key):
    if key in dd.keys():
        raise Exception('key is already existing')
    dd[key] = 0

def hypotenuse(a,b):
    #calcluer l'hypoténuse de a et b
    return math.sqrt(a**2 + b**2)

def check(data): #vérifier le type de chiffre
    """
    Gestion des exceptions pours les cas suivants:
        1.Saisie d'une str dans les arguments de la fonction
        2.Sasie un nombre complexe
        3.Saisie d'un nombre négatif
        4.Saisie d'un très grand nombre
        5.Saisie d'un très petit nombre
    """
    if data.isdigit():  #data est chiffre ou non
        if int(data) >= 10000: #dta est très grand ou non
            raise Exception('{} must be between 1 and 10000.'.format(data)) #on lance un exception si data est très grand
        elif int(data) < 1 : #data est très petit ou non
            raise Exception('{} must be superior 0.'.format(data)) #on lance un exception si data est très petit
        return int(data) #on convertis data à un chiffre et le revoie
    
    elif isinstance(data,str):
        if data.startswith('-'):
            if '.' in data:
                try:
                    if isinstance(float(data[1:]),float):
                        raise Exception('{} is lower 0.'.format(data)) #on lance un exception si data est négatif
                except ValueError:
                    raise Exception('{} is a string.'.format(data)) #on lance un exception si data est un chaîne de carctère                   
            elif data[1:].isdigit():
                raise Exception('{} is lower 0.'.format(data)) #on lance un exception si data est négatif
            elif '+' in data : #vérifier la forme est complex ou non
                try:
                    if isinstance(complex(data[1:]),complex):#data est un chaîne de caractère ou non: sa forme comme a+bj(-1+2j)
                        raise Exception('{} is a complex'.format(data))
                except ValueError:
                    raise Exception('{} is a string'.format(data))#les autres formes qu'on considére comme string
            elif '-' in data : #vérifier la forme est complex ou non
                try:
                    if isinstance(complex(data[1:]),complex):#data est un chaîne de caractère ou non: sa forme comme a+bj(-1-2j)
                        raise Exception('{} is a complex'.format(data))
                except ValueError:
                    raise Exception('{} is a string'.format(data))#les autres formes qu'on considére comme string
            else:
                raise Exception('data is a string.') #on lance un exception si data est un chaîne de carctère
        elif '-' in data : #vérifier la forme est complex ou non
            try:
                if isinstance(complex(data[1:]),complex):#data est un chaîne de caractère ou non: sa forme comme a+bj(1-2j)
                    raise Exception('{} is a complex'.format(data))
            except ValueError:
                    raise Exception('{} is a string'.format(data))#les autres formes qu'on considére comme string
        elif '+' in data :
            try:
                if isinstance(complex(data),complex):#data est un chaîne de caractère ou non: sa forme comme a+bj(1+2j)
                    raise Exception('{} is a complex'.format(data))
            except ValueError:
                raise Exception('{} is a string'.format(data))#les autres formes qu'on considére comme string
        elif '.' in data: #vérifier la data est float ou non
            try:
                if isinstance(float(data),float):#si data est float,retourner float
                    if float(data) == 0:
                        raise Exception('{} must be superior 0.'.format(data)) #on lance un exception si data est très petit
                    return float(data)
            except ValueError:
                raise Exception('{} is a string'.format(data)) #les autres formes qu'on considére comme string
        else:
                raise Exception('{} is a string'.format(data))#les autres formes qu'on considére comme string
    else:
        raise Exception('{} is a other error.'.format(data))#les autres formes qu'on considére comme string


if __name__ == '__main__': 
    while True:
        try:
            a = input('enter first digit: ') #saisire premier chiffre
            a = check(a)  #vérifier son type
            break
        except Exception as e1:
            print(str(e1))
            continue
    while True:
        try:
            b = input('enter seconde digit: ') #saisire deuxième chiffre
            b = check(b) #vérifier son type
            break
        except Exception as e1 :
            print(str(e1))
            continue
    c = hypotenuse(a,b) #calculer les deux chiffres
    print(c) # afficher le résultat



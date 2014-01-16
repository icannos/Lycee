# Script cryptage césar
#
# Version ne prenant en compte que les minuscules lettres (a-z)


#=========================
#Fonction ordre retournant la la valeur associée à une lettre, valeur comprise entre 0 et 25 avec a=0 et z=25
def ordre(char):
    assert "a" <= char <= "z" #Sécurité pour vérifier que char est bien une lettre minuscule
    return ord(char) - 97
#La fonction python ord renvoie le code ASCII d'un caractère avec a= 97 et z=122,
#donc on retranche 97 pour obtenir une valeur comprise entre 0 et 25

#=========================
#Renvoie le cractère correspondant au nombre compris entre 0 et 25 (réciproque de la fonctin ordre)
def lettre(nb):
    assert 0 <= nb <= 25 #Sécurité: nb compris entre 0 et 25
    return chr(nb + 97);
#On effectue l'opération inverse: nb + 97 pour obtenir le code ASCII du caractère
#On passe ensuite ce code dans la fonction chr de python qui à partir du code ASCII retoure un caractère
#=========================
#Fonction pour remplacer un caractère par un autre par décallage
def crypte_char(key, char):
    assert "a" <= char <= "z" #Sécrurité
    assert "a" <= key <= "z" #Sécurité

#On ajoute les codes de la clef et du caractère à crypter, on vérifie si l'on ne dépasse pas "z/25"
    if((ordre(char) + ordre(key)) > 25):
        #Si on dépasse, on retranche 26, pour boucler et donc reprendre au début de l'alphabet
        #On retourne ensuite le caractère via la fonction lettre
        return lettre((ordre(char) + ordre(key)) - 26) 
    else:
        #Sinon on retourne telle quelle le charactère en utilisant la fonction lettre 
        return lettre(ordre(char) + ordre(key))
    
#=========================
#Fonction réciproque de crypte_char
def decrypte_char(key, char):
    assert "a" <= char <= "z"
    assert "a" <= key <= "z"

    #On retranche le code de la clef au code du caractère crypté
    if((ordre(char) - ordre(key)) < 0): #On vérifie que l'on n'obtienne pas un code inférieur à 0
        #Si c'est inférieur à 0, on ajoute 26 pour reprendre à la fin de l'alphabet
        #On retourne ensuite le caractère via la fonction lettre
        return lettre((ordre(char) - ordre(key)) + 26)
    else:
        #Si on ne passe pas en dessous de 0 alors on retourne directement le caractère
        return lettre(ordre(char) - ordre(key))

#=========================
#Cette fonction lit chaque caractère d'un message et modifie chacuns d'eux via la fonction crypte_char
def crypte_msg(key, msg):
    assert "a" <= key <= "z"

    string = ""; #Chaine de caractère qui contiendra la réponse
    for char in msg: # Littéralement cela signifie: "prend chaque caractère[char] dans la chaine[msg]"
        if(char == " "): #si le caractère actuellement lu est un espace
            string += char #Alors on ajoute un espace dans la réponse
        else:
            #si c'est un caractère alors on le crypte via la fonction crypte_char et on l'ajoute à la suite
            #de la réponse
            string += crypte_char(key, char)

    return string #On renvoie la réponse après avoir parcouru tous les caractères du message

#=========================

def decrypte_msg(key, msg):
    assert "a" <= key <= "z"

    string = ""; #Chaine de caractère qui contiendra la réponse
    
    for char in msg:# Littéralement cela signifie: "prend chaque caractère[char] dans la chaine[msg]"
        if(char == " "):#si le caractère actuellement lu est un espace
            string += char #Alors on ajoute un espace dans la réponse
        else:
            #si c'est un caractère alors on le decrypte via la fonction decrypte_char et on l'ajoute à la suite
            #de la réponse
            string += decrypte_char(key, char)

    return string #On retourne la réponse
        
#=========================
    
    

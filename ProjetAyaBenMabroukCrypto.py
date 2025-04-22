"""
PyCryptoLab - Classical Cryptography Toolkit
Copyright (c) 2025 Aya Ben Mabrouk
License: MIT (see LICENSE for details)
"""

from six.moves import input as raw_input
from pprint import pprint




alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"




def cleanText(text, alphabet="abcdefghijklmnopqrstuvwxyz"):
    """
    Cette méthode nettoie et normalise le texte en remplaçant les caractères spéciaux selon les règles définies
    et en supprimant tous les caractères qui ne font pas partie de l'alphabet entrée en paramètre.

    Args:
        text (str): Le texte à nettoyer et normaliser.
        alphabet (str): L'alphabet à utiliser pour la normalisation. !! Par défaut, l'alphabet latin en minuscules.

    Returns:
        str: Le texte nettoyé et normalisé.
    """

    # Vérifie si les lettres majuscules et minuscules sont présentes dans l'alphabet donnée
    if 'A' not in alphabet or 'a' not in alphabet:
        # Convertir le texte en majuscules et l'alphabet en majuscules également
        text = text.upper()
        alphabet = alphabet.upper()

    # Remplacer les lettres accentuées par leurs équivalents non accentués si elles ne sont pas présentes dans l'alphabet donnée en paramètre
    if 'é' not in alphabet:
        text = text.replace("é", "e").replace("è", "e").replace("ê", "e").replace("ë", "e")

    # Remplacer la lettre 'ç' par 'c' si elle n'est pas présente dans l'alphabet donnée en paramètre
    if 'Ç' not in alphabet:
        text = text.replace("ç", "c")

    # Remplacer les autres lettres accentuées par leurs équivalents non accentués si elles ne sont pas présentes dans l'alphabet donnée en paramètre
    if 'ù' not in alphabet:
        text = text.replace("û", "u").replace("ü", "u").replace("ù", "u")
    if 'î' not in alphabet:
        text = text.replace("î", "i").replace("ï", "i")
    if 'à' not in alphabet:
        text = text.replace("à", "a").replace("â", "a").replace("ä", "a")
    if 'ô' not in alphabet:
        text = text.replace("ô", "o").replace("ö", "o")
    if 'ÿ' not in alphabet:
        text = text.replace("ŷ", "y")
    if 'œ' not in alphabet:
        text = text.replace("œ", "oe")

    # Supprimer tous les caractères qui ne font pas partie de l'alphabet donnée en paramètre
    for i in text:
        if i not in alphabet:
            text = text.replace(i, "")

    return text






def formatage(text, alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", estChiffre=True):
    """
    Formater le texte en groupant les caractères par blocs de 5 et en ajoutant des espaces entre les blocs.

    Args:
        text (str): Le texte à formater
        alphabet (str): L'alphabet utilisée pour la casse. !! Par défaut, l'alphabet latin en minuscules et majuscules.
        estChiffre (bool): Indique si le texte est chiffré. !! Par défaut, True.

    Returns:
        str: Le texte formaté
    """

    text2 = ""

    # Vérifie si les majuscules et minuscules sont présentes dans l'alphabet
    if 'A' in alphabet and 'a' in alphabet:
        # Si l'alphabet contient un espace, retourne le texte sans formatage
        if " " in alphabet:
            return text
        else:
            # Formate le texte en groupant les caractères par blocs de 5 avec un espace entre chaque bloc
            for i in range(0, len(text), 5):
                text2 += text[i:i + 5] + " "
            return text2
    else:
        # Si l'alphabet contient un espace, retourne le texte en majuscules ou minuscules selon estChiffre
        if " " in alphabet:
            if estChiffre:
                return text.upper()
            else:
                return text.lower()
        else:
            # Formater le texte en groupant les caractères par blocs de 5 avec un espace entre chaque bloc
            for i in range(0, len(text), 5):
                text2 += text[i:i + 5] + " "
            # Retourne le texte formaté en majuscules ou minuscules selon ischiffre
            if estChiffre:
                return text2.upper()  # chiffré
            else:
                return text2.lower()  # clair




##################################CESAR############################################

def cesar(text, cle, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ", ischiffre=True):
    text2 = ""
    #dechiffrement
    if ischiffre:
        for i in text:
            text2 += alphabet[(alphabet.index(i) + cle) % len(alphabet)]
    else:
        #chiffrement
        for i in text:
            text2 += alphabet[(alphabet.index(i) - cle) % len(alphabet)]
    return formatage(text2, alphabet, ischiffre)




##################################Longueur d'une clé donnée############################################

def longeurdecle(text):
    x=1
    while(True):
        nbchar=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for i in range(0,len(text),x):
            nbchar[alphabet.index(text[i])]+=1
        n=0
        for i in nbchar:
            n+=i
        s=0
        for i in range(len(nbchar)):
            s+=(nbchar[i]*(nbchar[i]-1))/(n*(n-1))
        if s>0.06:
            return x
        else :
            x+=1




def dechiffavecCe(text):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    alphabet2 = "STUVWXYZABCDEFGHIJKLMNOPQR "
    cal = []
    lon = longeurdecle(text)
    for j in range(lon):
        x = []
        for i in range(26):
            x.append(0)
        cal.append(x)
    for j in range(lon):
        for i in range(j, len(text), lon):  # 2 3 4 5 6 7 8 9 10 ... longeurdecle=7
            cal[j][alphabet.index(text[i])] += 1
    text2=""
    for i in text:
        text2 += alphabet2[alphabet.index(i)]
    return text2


##################################TRANSPOSITION############################################

def cleTransposition(cle):
    cle = cle.upper()
    ordr = sorted(cle)
    trans = []
    j = 0
    for i in ordr:
        trans.append(ordr.index(cle[j]))
        ordr[ordr.index(cle[j])] = '*'
        j += 1
    return trans


def transposition(text, cle, isformatNumerique=True, ischiffrer=True):
    text2 = ""
    if not isformatNumerique:
        cle = cleTransposition(cle)
    if ischiffrer:
        while (len(text) % len(cle) != 0):
            text += 'X'
        for i in range(0, len(text), len(cle)):
            v = text[i:i + len(cle)]
        for i in range(len(cle)):
            text2 += v[cle[i]]
    else:
        for i in range(0, len(text), len(cle)):
            v = text[i:i + len(cle)]
            for i in range(len(cle)):
                text2 += v[cle.index(i)]
    return text2



##################################CONSTRUCTION HORIZONTALE############################################

def constHorizontal(cle, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    cle2 = ""
    for i in cle:
        if i not in cle2:
            cle2 += i
    if 'a' not in alphabet or 'A' not in alphabet:
        cle2 = cle2.upper()
        alphabet = alphabet.upper()

    alpha2 = cle2 + alphabet
    alpha3 = ""
    for i in alpha2:
        if i not in alpha3:
            alpha3 += i
    return alpha3



##################################CONTRUCTION VERTICALE############################################

def constVertical(cle, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    cle2 = ""
    for i in cle:
        if i not in cle2:
            cle2 += i
    if 'a' not in alphabet or 'A' not in alphabet:
        cle = cle.upper()
        alphabet = alphabet.upper()
    alpha2 = ""
    alphaH = constHorizontal(cle, alphabet)
    for i in range(len(cle)):
        for j in range(i, len(alphaH), len(cle)):
            alpha2 += alphaH[j]
    return alpha2



##################################ALPHABET DESORDONNEE############################################

def alphabet_desordonne(text, chiffre=True, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                        alphabet_des="MEDNASRBCFGHIJKLOPQTUVWXYZ"):
    text2 = ""
    if chiffre:
        for i in text:
            text2 += alphabet_des[alphabet.index(i)]
    else:
        for i in text:
            text2 += alphabet[alphabet_des.index(i)]
    return text2



##################################CESAR############################################

def inverseBModuloN(n, b):
    n0 = n

    b0 = b


    q = int(n0 / b0)

    r = n0 - q * b0

    return r

    t0 = 0

    t = 1

    while r > 0:

        temp = t0 - q * t

        if temp >= 0:

            temp = temp % n

        else:

            temp = ((n - (-temp)) % n)

        t0 = t

        t = temp

        n0 = b0

        b0 = r

        q = int(n0 / b0)

        r = n0 - q * b0

    if (b0 != 1):

        return "b n'a pas d'inverse modulo n "

    else:

        return t



    

##################################AFFINE############################################

def chiffre_affine(text, a, b, chiffrer=True, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    text2 = ""
    if chiffrer:
        for i in text:
            text2 += alphabet[((((alphabet.index(i)) * a) + b)) % len(alphabet)]
    else:
        ap = inverseBModuloN(len(alphabet), a)
        for i in text:
            index = alphabet.index(i)
            val1 = int(index) - int(b)
            val2 = int(val1) * int(ap)
            val3 = int(val2) % len(alphabet)
            text2 += alphabet[val3]
    return text2



##################################ALGO RSA############################################

def RSAd(p,q,e):
    n=(p-1)*(q-1)
    b=e
    n0 = n
    b0 = b
    t0 = 0
    t = 1
    q = int(n0 / b0)
    r = n0 - q * b0

    while r > 0:
        temp = t0 - q * t
        if temp >= 0:
            temp = temp % n
        else:
            temp = ((n - (-temp)) % n)
        t0 = t
        t = temp
        n0 = b0
        b0 = r
        q = int(n0 / b0)
        r = n0 - q * b0
    if (b0 != 1):
        print("b n'a pas d'inverse modulo n ")
    else:
        return t


##################################CHIFFREMENT RSA############################################


def RSAchiffrement(p, q, e, text):  # M modulo E exposant

    cleM = p * q
    cleE = e
    alphabet = "#ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz"
    encodee1 = []
    for i in text:
        encodee1.append(alphabet.index(i))

    encodee1_chaine = ""
    for i in encodee1:
        encodee1_chaine += str(i)

    while len(encodee1_chaine) % 3:
        encodee1_chaine = "0" + encodee1_chaine

    encodee2 = []
    for i in range(0, len(encodee1_chaine), 3):
        encodee2.append(int(encodee1_chaine[i:i + 3]))
    chiffree = []

    for i in encodee2:
        x = (i ** cleE) % cleM
        chiffree.append(x)

    return chiffree



##################################DECHIFFREMENT RSA############################################


def RSAdechiffrement(p,q,e,chiff):
    cleM=p*q
    cleD=RSAd(p,q,e)
    alphabet = "#ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz"
    claire=[]
    for i in chiff:
        x = (i ** cleD) % cleM
        claire.append(x)

    claire_chaine=""
    for i in claire:
        x=str(i)
        while len(x)%3 != 0:
            x="0"+x
        claire_chaine+=x
    while claire_chaine[0]=="0":
        claire_chaine=claire_chaine[1:]

    claire2=[]
    for i in range(0,len(claire_chaine),2):
        claire2.append(int(claire_chaine[i:i+2]))
    claire_text=""

    for i in claire2:
        claire_text+=alphabet[i]
    return claire_text


from pprint import pprint



##################################ADFGVX############################################

def cryptage_adfgvx(cle,text):
    cle2="ADFGVX"
    ch=""
    for i in text:
        pos=cle.index(i)
        ch += cle2[int(pos/6)]
        ch+=cle2[pos%6]
    return ch

def cryptage_adfgvx2(cle,text):
    dif=len(text)%len(cle)
    if dif!=0:
        for i in range (len(cle)-dif):
            text+="x"
    tab=[]
    for i in range (len(cle)):
        tab.append("")
    for i in range (len(cle)):
        for j in range(i,len(text),len(cle)):
            tab[i]+=text[j]
    alphabet="abcdefghijklmnopqrstuvwxyz"
    chiffrer=""
    for i in alphabet:
        if i in cle :
            chiffrer+=tab[cle.index(i)]
    return chiffrer

def dechiffreradf(cle,text):
    text.lower()
    tab=[]
    for i in range (len(cle)):
        tab.append("")
    for i in range (len(cle)):
        tab[i]=text[i*len(text)//len(cle):len(text)//len(cle)+i*len(text)//len(cle)]
    clo=sorted(list(cle))
    tab2=[]
    for i in range (len(cle)):
        tab2.append("")
    for i in cle:
        tab2[cle.index(i)]+=tab[clo.index(i)]
        clo[clo.index(i)]="#"
        cle=cle.replace(i,"#",1)
    return tab2



##################################PORTA############################################

def dchiffrerPorta(cle, text):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha = ['ABCDEFGHIJKLM', 'NOPQRSTUVWXYZ']
    x = 1
    al = ''
    for j in range(12):
        for i in range(13):
            al += alpha[1][(i + (13 - x)) % 13]
        alpha.append(al)
        al = ''
        x += 1
    chiff = ""
    for i in range(len(text)):
        c = cle[i % len(cle)]
        if alphabet.index(c) % 2 == 0:
            a = (alphabet.index(c) / 2) + 1
        else:
            a = (alphabet.index(c) + 1) / 2

        if text[i] in alpha[0]:
            chiff += alpha[int(a)][alpha[0].index(text[i])]
        else:
            chiff += alpha[0][alpha[int(a)].index(text[i])]
    return ( chiff)




##################################MAIN############################################

ans = True
while ans:
    print("""
    1.Chiffrement.
    2.Dechiffrement.
    3.Quitter.
    """)
    ans = raw_input("Votre choix")
    if ans == "1":
        choix = True
        while choix:
            print("""
            1.Chiffrement Cesar.
            2.Chiffrement Porta.
            3.Chiffrement par Transposition.
            4.Chiffrement ADFGVX.
            5.Chiffrement désordonnée.
            6.Chiffrement affine.
            7.Chiffrement RSA.
            8.Quitter.
            """)
            choix = raw_input("Votre choix de chiffrement:\n")
            if choix == "1":
                text = input("\nDonner votre texte à chiffrer:\n")
                cle = int(input("Donner le clé voulu:\n"))
                text = cleanText(text)
                print(text)
                chiffre = cesar(text, cle, ischiffre=True)
                print("Le text chiffré est:\n" + formatage(chiffre))


            elif choix == "2":
                print("\n Student Deleted")
            elif choix == "3":
                cle = input("Donner le clé de chiffrement:\n")
                cle = cleTransposition(cle)
                # print(cle)
                text = input("Donner votre texte à chiffrer:\n")
                text = cleanText(text)
                # print(text)1
                text = transposition(text, cle, isformatNumerique=True, ischiffrer=True)
                print("\nle texte chiffré est : " + formatage(text))
            elif choix == "4":
                text = input("Donner votre texte à chiffrer:\n")
                cle1 = input("Donner le premier clé :\n")
                cle2 = input("Donner le deuxième clé :\n")
                print("\nle texte chiffré est : " +cryptage_adfgvx2(cle2, cryptage_adfgvx(cle1,text) ))

            elif choix == "5":
                choixAlphabet = True
                while choixAlphabet:
                    print("""
                    1.Construction horizontale.
                    2.Construction verticale.
                    3.Arbitraire.
                    """)
                    choixAlphabet = raw_input("Votre choix d'alphabet désordonnée:\n")
                    if choixAlphabet == "1":
                        cle = input("\nDonner le clé :\n")
                        alphabet = constHorizontal(cle)
                        text = input("Donner le texte à chiffrer")
                        text = alphabet_desordonne(cleanText(text), chiffre=True, alphabet_des=alphabet)
                        print("le texte chiffré est: " + formatage(text))
                    elif choixAlphabet == "2":
                        cle = input("\nDonner le clé :\n")
                        alphabet = constVertical(cle)
                        text = input("Donner le texte à chiffrer")
                        text = alphabet_desordonne(cleanText(text), chiffre=True, alphabet_des=alphabet)
                        print("le texte chiffré est: " + formatage(text))
                    elif choixAlphabet == "3":
                        alphabet = input("Donner l'alphabet désordonnée voulue:(26 caractères)\n")
                        text = input("Donner le texte à chiffrer")
                        text = alphabet_desordonne(cleanText(text), chiffre=True, alphabet_des=alphabet)
                        print("le texte chiffré est: " + formatage(text))

            elif choix == "6":
                text = input("Donner votre texte à chiffrer:\n")
                a = int(input("\nDonner la valeur du a qui n'est pas divisible par 2 et 13:\n"))
                b = int(input("\nDonner la valeur du b:\n"))
                text = chiffre_affine(text, a, b, chiffrer=True)
                print("\nle texte chiffré est : " + formatage(text))

            elif choix == "7":
                text = input("Donner le texte à chiffrer:\n")
                p = int(input("Donner p:\n"))
                q = int(input("Donner q:\n"))
                e = int(input("Donner e:\n"))
                text = RSAchiffrement(p,q,e, text)
                print(text)



            elif choix == "8":
                print("\n Au revoir")
                quit()
            elif choix != "":
                print("\n Votre choix est incorrecte")






    elif ans == "2":

        choix = True
        while choix:
            print("""
                   1.Déchiffrement Cesar.
                   2.Déchiffrement Porta.
                   3.Déchiffrement par Transposition.
                   4.Déchiffrement ADFGVX.
                   5.Analyse de fréquence.
                   6.Déchiffrement désordonnée.
                   7.Déchiffrement affine.
                   8.Déchiffrement RSA.
                   9.Quitter.
                   """)
            choix = raw_input("Votre choix de Déchiffrement")
            if choix == "1":
                text = input("\nDonner votre texte à déchiffrer:\n")
                cle = int(input("Donner le clé voulu:\n"))
                text = cleanText(text)
                chiffre = cesar(text, cle, ischiffre=False)
            elif choix == "2":
                cle = input("Donner le clé de déchiffrement:\n")
                text = input("Donner votre texte à déchiffrer:\n")
                text=dchiffrerPorta(cle.upper(),cleanText(text).upper())
                print("\nle texte déchiffré est : " + text)
            elif choix == "3":
                cle = input("Donner le clé de déchiffrement:\n")
                cle = cleTransposition(cle)
                # print(cle)
                text = input("Donner votre texte à déchiffrer:\n")
                text = cleanText(text)
                # print(text)1
                text = transposition(text, cle, isformatNumerique=True, ischiffrer=False)
                print("\nle texte déchiffré est : " + text)
            elif choix == "4":
                text = input("Donner votre texte à déchiffrer:\n")
                cle = input("Donner le clé voulu:\n")
                liste=dechiffreradf(cle,text)
                print("\nle texte déchiffré est : ")
                print(liste)
            elif choix == "5":
                text = input("Donner votre texte à déchiffrer:\n")
                print("\nle texte déchiffré est : "+dechiffavecCe(text))
            elif choix == "6":
                choixAlphabet = True
                while choixAlphabet:
                    print("""
                                   1.Construction horizontale.
                                   2.Construction verticale.
                                   3.Arbitraire.
                                   """)
                    choixAlphabet = raw_input("Votre choix d'alphabet désordonnée:\n")
                    if choixAlphabet == "1":
                        cle = input("\nDonner le clé :\n")
                        alphabet = constHorizontal(cle)
                        text = input("Donner le texte à déchiffrer")
                        text = alphabet_desordonne(cleanText(text), chiffre=False, alphabet_des=alphabet)
                        print("le texte déchiffré est: " + text.lower())
                    elif choixAlphabet == "2":
                        cle = input("\nDonner le clé :\n")
                        alphabet = constVertical(cle)
                        text = input("Donner le texte à déchiffrer")
                        text = alphabet_desordonne(cleanText(text), chiffre=False, alphabet_des=alphabet)
                        print("le texte déchiffré est: " + text.lower())
                    elif choixAlphabet == "3":
                        alphabet = input("Donner l'alphabet désordonnée voulue:(26 caractères)\n")
                        text = input("Donner le texte à déchiffrer")
                        text = alphabet_desordonne(cleanText(text), chiffre=False, alphabet_des=alphabet)
                        print("le texte déchiffré est: " + text.lower())


            elif choix == "7":
                text = input("Donner votre texte à déchiffrer:\n")
                a = int(input("\nDonner la valeur du a qui n'est pas divisible par 2 et 13:\n"))
                b = int(input("\nDonner la valeur du b:\n"))
                text = chiffre_affine(text, a, b, chiffrer=False)
                print("\nle texte déchiffré est : " + text)
            elif choix == "8":
                text = input("Donner le texte à déchiffrer:\n")
                p = int(input("Donner p:\n"))
                q = int(input("Donner q:\n"))
                e = int(input("Donner e:\n"))
                text = RSAdechiffrement(p,q,e, text)
                print(text)
            elif choix == "9":
                print("\n Au revoir")
                quit()
            elif choix != "":
                print("\n Votre choix est incorrecte")


    elif ans == "3":
        print("\n Au revoir")
        quit()
    elif ans != "":
        print("\n Votre choix est incorrecte")

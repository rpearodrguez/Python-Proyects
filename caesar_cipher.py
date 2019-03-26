'''
*Caesar cipher** - Implement a Caesar cipher, both encoding and decoding. The key is an integer from 1 to 25.
This cipher rotates the letters of the alphabet (A to Z). The encoding replaces each letter with the 1st to 25th
next letter in the alphabet (wrapping Z to A). So key 2 encrypts "HI" to "JK", but key 20 encrypts "HI" to "BC".
This simple "monoalphabetic substitution cipher" provides almost no security, because an attacker who has the encoded
message can either use frequency analysis to guess the key, or just try all 25 keys
'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
code = ""
lag = 0
def cipher(code, key):
    #funcion para cifrar texto
    print("Su palabra original era: \n"+code)
    cifrado = ''
    #revisa el texto
    for letter in code.lower():
        #busca letra por letra en el alfabeto
        if letter == ' ':
            cifrado = cifrado+' '

        if letter in alphabet:
            #revisa el indice, si supera al numero de letras del alfabeto, vuelve atrás
            if alphabet.index(letter)+key<= 25:
                cifrado = cifrado+alphabet[alphabet.index(letter) + key]
            elif alphabet.index(letter)+key > 25:
                cifrado = cifrado+alphabet[alphabet.index(letter) + key - 26]
    print("Su cifrado ya realizado es: \n"+cifrado)
    #devuelve el texto ya cifrado
    return cifrado


def decipher(code, key):
    # funcion para cifrar texto
    print("Su palabra original era: \n" + code)
    cifrado = ''
    # revisa el texto
    for letter in code.lower():
        # busca letra por letra en el alfabeto
        if letter == ' ':
            cifrado = cifrado + ' '

        if letter in alphabet:
            # revisa el indice, si supera al numero de letras del alfabeto, vuelve atrás
            if alphabet.index(letter) + key <= 25:
                cifrado = cifrado + alphabet[alphabet.index(letter) - key]
            elif alphabet.index(letter) + key > 25:
                cifrado = cifrado + alphabet[alphabet.index(letter) - key + 26]
    print("Su cifrado ya realizado es: \n" + cifrado)
    # devuelve el texto ya cifrado
    return cifrado



cipher("Todo el mundo coma tierra",2)
cipher("hi",20)
cipher("az",1)
decipher("ba",1)
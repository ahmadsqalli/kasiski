import math
from kasiski.helper_func import substitute

alphabet = list("abcdefghijklmnopqrstuvwxyz")
reverse_alphabet = alphabet[::-1]
affine_dict = dict(zip(alphabet, range(0, 26)))
r_affine_dict = dict(zip(range(0, 26), alphabet))
atbash_cipher_dict = dict(zip(alphabet, reverse_alphabet))
gematria_dict = dict(zip(alphabet, range(1, 27)))
plaintext_message = "ahmad sqalli (Ahmed SQALLI HOUSSAINI) born 1997 @ 05:30 in the morning"

# reverse alphabet
# supports spaces, numbers, and special characters
def atbash_cipher(plaintext):

    ciphertext = substitute(plaintext, atbash_cipher_dict)

    return ciphertext


# alphabet shifted by n steps
# can be used as ROT13, set steps to 13
# supports spaces, numbers, and special characters
# decipher: True or False or 'brutforce'
def caesar_cipher(decipher, plaintext, steps):
    
    plaintext = plaintext
    if steps > 25:
        return "error: steps can't be higher than 25"
        
    if decipher == False:
        caesar_alphabet = alphabet[steps:] + alphabet[:steps]
        caesar_alphabet_dict = dict(zip(alphabet, caesar_alphabet))
        ciphertext = substitute(plaintext, caesar_alphabet_dict)
        
    if decipher == True:
        caesar_alphabet = alphabet[steps:] + alphabet[:steps]
        caesar_alphabet_dict = dict(zip(caesar_alphabet, alphabet))
        ciphertext = substitute(plaintext, caesar_alphabet_dict)
        
    if decipher == "brutforce":
        ciphertext = {}
        
        for i in range(0, 25):
            
            caesar_alphabet = alphabet[i:] + alphabet[:i]
            caesar_alphabet_dict = dict(zip(caesar_alphabet, alphabet))
            ciphertext[i] = substitute(plaintext, caesar_alphabet_dict)

    return ciphertext


# (ax+b) -> mod26: if mod > 26
# supports spaces, numbers, and special characters
def affine_cipher(decipher, plaintext):
    
    a, b, m = 5, 8, 26
    
    def affine_func(x, decipher):
        
        if decipher == False:
            
            #(ax+b) mod: if m > 26
            #(5x+8) mod 26
            d = ( a * x ) + b
            if d > m:
                d = d % m
            return d
            
        if decipher == True:
            
            #21(x−b) mod m
            #21(x-8) mod 26
            return 21 * ( x - b ) % m
            
    ciphertext = ''

    for char in list(plaintext):
        if char.isalpha():
            if char.isupper():
                x = affine_dict[char.lower()]
                ciphertext += r_affine_dict[affine_func(int(x), decipher)].upper()
            else:
                try:
                    x = affine_dict[char]
                    ciphertext += r_affine_dict[affine_func(int(x), decipher)]
                except Exception as e:
                    ciphertext = "error: cipher supports only English letters"
                    break
        else:
            ciphertext += char
    return ciphertext


# key/matrix based cipher
# key must contain only letters
# doesn't support uppercases, spaces, numbers, and special characters
def vigenere_cipher(decipher, cipher_key, plaintext):
    
    plaintext = plaintext.lower()
    vigenere_matrix = {}
    i = 0
    for char in alphabet:
        vigenere_matrix[char] = alphabet[i:] + alphabet[:i]
        i=i+1
        
    mapped_key = str(cipher_key*math.ceil(len(plaintext)/len(cipher_key)))[:len(plaintext)]
    try:
        if decipher == False:
            ciphertext = ""
            for ct, ck  in zip(plaintext,mapped_key):
                ciphertext += vigenere_matrix[ck][alphabet.index(ct)]
                
            return ciphertext
        if decipher == True:
            ciphertext = ""
            for vc, ck in zip(plaintext, mapped_key):
                ciphertext += alphabet[vigenere_matrix[ck].index(vc)]
            
            return ciphertext
    except Exception as e:
        return 'error: cipher, and cipher key support lowercase Enlish letters only, no spaces, uppercases, special characters'


# not reversable
# doesn't support uppercase, spaces, numbers, and special characters
def gematria(plaintext):
    
    numeric_val = 0
    ciphertext = []
    
    try:
        for cw in plaintext.split(' '):
            c_len = len(cw)
            for i, c in enumerate(cw):
                numeric_val = numeric_val+gematria_dict[c]
                if int(i+1) == c_len:
                    ciphertext.append(numeric_val)
                    numeric_val = 0
    except Exception as e:
        return f'error: {e}\ncipher support only lowercase Enlish letters and spaces'
    
    return ciphertext


# doesn't support spaces
def rail_fence_cipher(decipher, plaintext, rails):

    rail = 1
    r = len( range( rails ) ) # = 5
    rail_fence = [''] * r
    
    if decipher == False:
        
        for _, char in enumerate(list(plaintext)):
            
            rail_fence[rail-1] = rail_fence[rail-1] + char
            
            if rail == 1:
                rail_operation = '+'
            elif rail == r:
                rail_operation = '-'
                
            if rail_operation == '+':
                rail += 1
            if rail_operation == '-':
                rail -= 1
        
        return(' '.join(rail_fence))
    
    
    if decipher == True:
        
        x = plaintext.split(' ')
        output = ""
        
        for _ in range(len(plaintext)):
            
            output += x[int(rail-1)][:1]
            x[int(rail-1)] = x[int(rail-1)][1:]
            
            if rail == 1:
                rail_operation = '+'
            elif rail == r:
                rail_operation = '-'
                
            if rail_operation == '+':
                rail += 1
            if rail_operation == '-':
                rail -= 1
        
        return(output)


# chaos baesd cipher
# cipher supports only lowercase letters
# any other characters will be omitted
# any uppercase letter will be transformed into lowercase
def chaocipher(decipher, plaintext, ciphertext_disk, plaintext_disk):
    
    ciphertext = ""
    ct_disk = list(ciphertext_disk)
    pt_disk = list(plaintext_disk)
    
    def perform_chaos(pt_disk_id, ct_disk, pt_disk):
        
        # ciphertext_disk:
        # ct_letter -> zenith
        # zenith+1  -> nadir
        ct_disk = ct_disk[pt_disk_id:] + ct_disk[:pt_disk_id]
        ct_disk = list(ct_disk[0] + ''.join(ct_disk[2:14]) + ct_disk[1] + ''.join(ct_disk[14:26]))
        
        # plaintext_disk:
        # target_letter -> zenith+1
        # zenith+2  -> nadir
        
        pt_disk = pt_disk[pt_disk_id+1:] + pt_disk[:pt_disk_id+1]
        pt_disk = list(''.join(pt_disk[0:2]) + ''.join(pt_disk[3:14]) + pt_disk[2] + ''.join(pt_disk[14:26]))
        # print(pt_disk)
        
        return ct_disk, pt_disk
        
    
    # map and extract pt_letter from ct_disk
    if decipher == False:
        for target_char in list(plaintext.lower()):
            for pt_disk_id, pt_disk_letter in enumerate(pt_disk):
                if pt_disk_letter == target_char:
                    ciphertext += ct_disk[ pt_disk_id ]
                    # print(ct_disk[ pt_disk_id ])
                    
                    ct_disk, pt_disk = perform_chaos(pt_disk_id, ct_disk, pt_disk)
                    
    if decipher == True:
        for target_char in list(plaintext.lower()):
            for pt_disk_id, pt_disk_letter in enumerate(ct_disk):
                if pt_disk_letter == target_char:
                    ciphertext += pt_disk[ pt_disk_id ]
                    # print(ct_disk[ pt_disk_id ])
                    
                    ct_disk, pt_disk = perform_chaos(pt_disk_id, ct_disk, pt_disk)
                    
    return ciphertext


if __name__ == "__main__":
    # test cases
    print( 'atbash test::\n' + atbash_cipher('hello world') + '\n' )
    print( 'caeser test::\n' + caesar_cipher(False, 'hello world', 13) + '\n' )
    print( 'affine test::\n' + affine_cipher(False, 'hello world') + '\n' )
    print( 'vigenere test::\n' + vigenere_cipher(False, 'lemon', 'attackatdawn') + '\n' )
    print( 'gematria test::\n' + str(gematria('hello world')) + '\n' )
    print( 'rail fence test::\n' + rail_fence_cipher(False, 'helloworld', 3) + '\n' )
    print( 'chaocipher test::\n' + chaocipher(False, 'helloworld', 'abcdefghijklmnopqrstuvwxyz', 'etaoinshrdlcumwfgypbvkjxqz') + '\n' )

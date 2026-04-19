from collections import Counter

alphabet = list("abcdefghijklmnopqrstuvwxyz")


# finds all repeated sequences of length >= min_seq in the ciphertext
# returns a dict of {sequence: [positions]}
def find_sequences(ciphertext, min_seq=3):

    ciphertext = ciphertext.lower().replace(' ', '')
    sequences = {}

    for length in range(min_seq, len(ciphertext) // 2 + 1):
        for i in range(len(ciphertext) - length + 1):
            seq = ciphertext[i:i + length]
            if seq not in sequences:
                sequences[seq] = []
            sequences[seq].append(i)

    return {seq: pos for seq, pos in sequences.items() if len(pos) > 1}


# computes pairwise distances between all occurrences of repeated sequences
def get_spacings(sequences):

    spacings = []

    for positions in sequences.values():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                spacings.append(positions[j] - positions[i])

    return spacings


# returns all factors of n greater than 1
def factorize(n):

    factors = []

    for i in range(2, n + 1):
        if n % i == 0:
            factors.append(i)

    return factors


# counts how often each factor appears across all spacings
def count_factors(spacings):

    factor_counts = Counter()

    for s in spacings:
        for f in factorize(s):
            factor_counts[f] += 1

    return factor_counts


# main kasiski examination function
# ciphertext must be lowercase letters only, no spaces or special characters
# returns a list of (key_length, score) tuples sorted by likelihood
# top_n: number of key length candidates to return
def kasiski_examination(ciphertext, min_seq=3, top_n=5):

    ciphertext = ciphertext.lower().replace(' ', '')
    
    if not ciphertext.isalpha():
        return 'error: ciphertext supports only lowercase English letters and spaces'

    sequences = find_sequences(ciphertext, min_seq)

    if not sequences:
        return 'error: no repeated sequences found, ciphertext may be too short'

    spacings = get_spacings(sequences)
    factor_counts = count_factors(spacings)

    return factor_counts.most_common(top_n)


if __name__ == "__main__":
    import math

    def vigenere_cipher(decipher, cipher_key, plaintext):
        plaintext = plaintext.lower()
        vigenere_matrix = {}
        i = 0
        for char in alphabet:
            vigenere_matrix[char] = alphabet[i:] + alphabet[:i]
            i = i + 1
        mapped_key = str(cipher_key * math.ceil(len(plaintext) / len(cipher_key)))[:len(plaintext)]
        try:
            if decipher == False:
                ciphertext = ""
                for ct, ck in zip(plaintext, mapped_key):
                    ciphertext += vigenere_matrix[ck][alphabet.index(ct)]
                return ciphertext
            if decipher == True:
                ciphertext = ""
                for vc, ck in zip(plaintext, mapped_key):
                    ciphertext += alphabet[vigenere_matrix[ck].index(vc)]
                return ciphertext
        except Exception as e:
            return 'error: cipher and cipher key support only lowercase English letters'

    import random, string
    random.seed(0)

    key = 'secret'
    plaintext = ''.join(random.choices(string.ascii_lowercase, k=500))
    ciphertext = vigenere_cipher(False, key, plaintext)

    print( f'key used: {key} (length {len(key)})\n' )
    print( 'kasiski examination results::' )
    print( kasiski_examination(ciphertext) )
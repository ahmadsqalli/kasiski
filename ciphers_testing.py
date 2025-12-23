from kasiski import *
import random, time

global_start_time = time.time()

test_runs = 10

'''
ATBASH CIPHER
the cipher supports uppercase and lowercase letters, numbers, spaces, and punctuation
'''
start_time = time.time()

error, match_count, err_count = [], 0, 0

for _ in range(test_runs):

    rand_string_param = dict(
        # lowercase is True by default
        uppercase = True,
        spaces = True,
        digits = True,
        punctuation = True
    )
    random_plaintext = random_word_gen( rand_string_param, range(80) )

    ciphered = atbash_cipher(random_plaintext)
    deciphered = atbash_cipher(ciphered)

    if random_plaintext == deciphered:
        match_count += 1
    else:
        error.append({
            'plaintext': random_plaintext,
            'ciphered': ciphered,
            'deciphered': deciphered,
        })
        err_count += 1

print(f"\natbash cipher: {match_count} - {err_count}\n{error}")
end_time = time.time()
print(f"\nTotal atbash testing time for {test_runs} runs: {end_time - start_time} seconds")

'''
CAESAR CIPHER
the cipher supports uppercase and lowercase letters, numbers, spaces, and punctuation
'''
start_time = time.time()

error, match_count, err_count = [], 0, 0

for i in range(test_runs):

    rand_string_param = dict(
        # lowercase is True by default
        uppercase = True,
        spaces = True,
        digits = True,
        punctuation = True
    )
    random_plaintext = random_word_gen( rand_string_param, range(80) )

    steps = random.randint(1,25)

    ciphered = caesar_cipher(False, random_plaintext, steps)
    deciphered = caesar_cipher(True, ciphered, steps)

    if random_plaintext == deciphered:
        match_count += 1
    else:
        error.append({
            'plaintext': random_plaintext,
            'steps': steps,
            'ciphered': ciphered,
            'deciphered': deciphered,
        })
        err_count += 1

print(f"\ncaesar cipher: {match_count} - {err_count}\n{error}")
end_time = time.time()
print(f"\nTotal caesar testing time for {test_runs} runs: {end_time - start_time} seconds")

'''
AFFINE CIPHER
supports spaces, numbers, and special characters
'''
start_time = time.time()

error, match_count, err_count = [], 0, 0

for i in range(test_runs):

    rand_string_param = dict(
        # lowercase is True by default
        uppercase = True,
        spaces = True,
        digits = True,
        punctuation = True
    )
    random_plaintext = random_word_gen( rand_string_param, range(80) )

    ciphered = affine_cipher(False, random_plaintext)
    deciphered = affine_cipher(True, ciphered)

    if random_plaintext == deciphered:
        match_count += 1
    else:
        error.append({
            'plaintext': random_plaintext,
            'ciphered': ciphered,
            'deciphered': deciphered,
        })
        err_count += 1

print(f"\naffine cipher: {match_count} - {err_count}\n{error}")
end_time = time.time()
print(f"\nTotal affine testing time for {test_runs} runs: {end_time - start_time} seconds")

'''
VIGENERE CIPHER
key must contain only lowercase letters
doesn't support uppercase, spaces, numbers, and special characters
any uppercase letters in be converted to lowercase before processing
'''
start_time = time.time()

error, match_count, err_count = [], 0, 0

for i in range(test_runs):

    rand_string_param = dict(
        # lowercase is True by default
        uppercase = False,
        spaces = False,
        digits = False,
        punctuation = False
    )

    random_plaintext = random_word_gen( rand_string_param, range(80) )

    rand_string_param = dict(
        # lowercase is True by default
        uppercase = False,
        spaces = False,
        digits = False,
        punctuation = False
    )
    
    cipher_key = random_word_gen( rand_string_param, range(8, 20) )

    ciphered = vigenere_cipher(False, cipher_key, random_plaintext)
    deciphered = vigenere_cipher(True, cipher_key, ciphered)

    if random_plaintext == deciphered:
        match_count += 1
    else:
        error.append({
            'plaintext': random_plaintext,
            'cipher_key': cipher_key,
            'ciphered': ciphered,
            'deciphered': deciphered,
        })
        err_count += 1

print(f"\nvigenere cipher: {match_count} - {err_count}\n{error}")
end_time = time.time()
print(f"\nTotal vigenere testing time for {test_runs} runs: {end_time - start_time} seconds")

'''
RAIL FENCE CIPHER
key: number of rails
doesn't support spaces
'''
start_time = time.time()

error, match_count, err_count = [], 0, 0

for i in range(test_runs):

    rand_string_param = dict(
        # lowercase is True by default
        uppercase = True,
        spaces = False,
        digits = True,
        punctuation = True
    )

    random_plaintext = random_word_gen( rand_string_param, range(80) )
    
    rails = random.randint(2,25)
    ciphered = rail_fence_cipher(False, random_plaintext, rails)
    deciphered = rail_fence_cipher(True, ciphered, rails)

    if random_plaintext == deciphered:
        match_count += 1
    else:
        error.append({
            'plaintext': random_plaintext,
            'rails': rails,
            'ciphered': ciphered,
            'deciphered': deciphered,
        })
        err_count += 1

print(f"\nrail fence cipher: {match_count} - {err_count}\n{error}")
end_time = time.time()
print(f"\nTotal rail fence testing time for {test_runs} runs: {end_time - start_time} seconds")

'''
CHAOSCIPHER
keyS: two 26-letter strings representing the left and right disks
cipher supports only lowercase letters
any other characters will be omitted
any uppercase letter will be transformed into lowercase
'''
start_time = time.time()

error, match_count, err_count = [], 0, 0

for i in range(test_runs):

    rand_string_param = dict(
        # lowercase is True by default
        uppercase = False,
        spaces = False,
        digits = False,
        punctuation = False
    )

    random_plaintext = random_word_gen( rand_string_param, range(80) )

    alphabet = list('abcdefghijklmnopqrstuvwxyz')

    random.shuffle(alphabet)
    shuffled_alphabet = "".join(alphabet)
    right_disk = ''.join(shuffled_alphabet)

    random.shuffle(alphabet)
    shuffled_alphabet = "".join(alphabet)
    left_disk = ''.join(shuffled_alphabet)

    ciphered = chaocipher(False, random_plaintext, left_disk, right_disk)
    deciphered = chaocipher(True, ciphered, left_disk, right_disk)

    if random_plaintext == deciphered:
        match_count += 1
    else:
        error.append({
            'plaintext': random_plaintext,
            'left_disk': left_disk,
            'right_disk': right_disk,
            'ciphered': ciphered,
            'deciphered': deciphered,
        })
        
        err_count += 1

print(f"\nchaocipher: {match_count} - {err_count}\n{error}")
end_time = time.time()
print(f"\nTotal chaocipher testing time for {test_runs} runs: {end_time - start_time} seconds") 
print("\n----------------------------------")
global_end_time = time.time()
print(f"Total testing time:: {test_runs} runs for each cipher is: {global_end_time - global_start_time} seconds")
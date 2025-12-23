def substitute(original_text, subtitution_dict):

    ciphertext = ''
    
    try:
        for char in list(original_text):
            if char.isalpha():
                if char.isupper():
                    ciphertext += subtitution_dict[char.lower()].upper()
                else:
                    ciphertext += subtitution_dict[char]
            else:
                ciphertext += char
    except Exception as e:
        return f"error: ciphers supports only English alphabet"
    return ciphertext

def text_match_rate(text_1, text_2, format='all'):
    
    len_1, len_2 = len(text_1), len(text_2)
    constant, changed = 0, 0
    if len_1 == len_2:
        for t1, t2 in zip(text_1, text_2):
            if t1 != t2 and t1.isalpha() and t2.isalpha():
                changed += 1

            if t1 == t2 and t1.isalpha() and t2.isalpha():
                constant += 1

    if format == 'percent':
        return constant/len(text_1)*100
    if format == 'value':
        return (constant, changed)
    else:
        return constant/len(text_1)*100, constant, changed

rand_string_param = dict(
        # lowercase is True by default
        uppercase = False,
        spaces = False,
        digits = False,
        punctuation = False
    )

def random_word_gen(rand_string_param, word_length):
    import string
    import random

    if isinstance(word_length, (list, range)):
        actual_length = random.choice(word_length)
    else:
        actual_length = word_length
    
    random_string = string.ascii_lowercase

    if (rand_string_param['uppercase'] is True):
        random_string += string.ascii_uppercase
    if (rand_string_param['spaces'] is True):
        random_string += ' '*int(actual_length*0.12)
    if (rand_string_param['digits'] is True):
        random_string += string.digits
    if (rand_string_param['punctuation'] is True):
        random_string += string.punctuation
    
    random_string = ''.join(random.choices(random_string, k=actual_length))
    
    return random_string
from kasiski.helper_func import substitute

unigram_freq = list('etaoinsrhldcumfpgwybvkxjqz')
bigram_freq = ["th","he","in","er","an","re","on","at","en","nd","ti","es","or","te","of","ed","is","it","al","ar","st","to","nt","ng","se","ha","as","ou","io","le","ve","co","me","de","hi","ri","ro","ic","ne","ea","ra","ce"]
digram_freq = ['ll', 'ee', 'ss', 'oo', 'tt', 'ff', 'rr', 'nn', 'pp', 'cc']
trigram_freq = ["the","and","tha","ent","ing","ion","tio","for","nde","has","nce","edt","tis","oft","sth","men"]

def frequency_analysis(plaintext, return_format='dict'):
    
    unigram, digram, bigram, trigram = {}, {}, {}, {}
    plaintext_arr = list(plaintext)
    plaintext_len = len(plaintext_arr)
    
    for i, l in enumerate(plaintext_arr):
        
        if plaintext_len-1 == i:
            break
        
        if l.isalpha():
            
            unigram[l] = unigram[l] +1 if l in unigram else 1
            
            if plaintext_arr[i].isalpha() and plaintext_arr[i+1].isalpha():
                n_bi = ''.join(plaintext_arr[i] + plaintext_arr[i+1])
                bigram[n_bi] = bigram[n_bi]+1 if n_bi in bigram else 1


            if i < plaintext_len-1:
                if l == plaintext_arr[i+1]:
                    n_digram = ''.join([plaintext_arr[i], plaintext_arr[i+1]])
                    digram[n_digram] =  digram[n_digram] +1 if n_digram in digram else 1
            
            if plaintext_len-2 != i:
                if plaintext_arr[i].isalpha() and plaintext_arr[i+1].isalpha() and plaintext_arr[i+2].isalpha():
                    n_tri = ''.join(plaintext_arr[i:i+3])
                    trigram[n_tri] = trigram[n_tri]+1 if n_tri in trigram else 1

    unigram = sorted(unigram.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
    digram = sorted(digram.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
    bigram = sorted(bigram.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
    trigram = sorted(trigram.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
        
    if return_format == 'dict':

        unigram_dict, digram_dict, bigram_dict, trigram_dict = {}, {}, {}, {}

        for i, (letter, _) in enumerate(unigram):
            if letter.isalpha():
                unigram_dict[letter] = unigram_freq[i] if i < len(unigram_freq) else ''
        
        for i, (digram_text, _) in enumerate(digram):
            if digram_text.isalpha():
                if i < len(digram_freq):
                    digram_dict[digram_text] = digram_freq[i]
        
        for i, (bigram_text, _) in enumerate(bigram):
            if bigram_text.isalpha():
                if i < len(bigram_freq):
                    bigram_dict[bigram_text] = bigram_freq[i]
        
        for i, (trigram_text, _) in enumerate(trigram):
            if trigram_text.isalpha():
                if i < len(trigram_freq):
                    trigram_dict[trigram_text] = trigram_freq[i]

        return unigram_dict, digram_dict, bigram_dict, trigram_dict
    else:
        return unigram, digram, bigram, trigram




def digram_substitute(plaintext, di_dict):
    
    pt_arr, pt_len = list(plaintext), len(plaintext)
    
    final_text = ''
    
    skip = 0
    for i, char in enumerate(pt_arr):

        if skip == 0:

            if i > pt_len-2:
                # POST-PENULTIMATE
                final_text += char
            else:
                
                current_digram = ''.join(char + pt_arr[i+1])
                
                if char.isalpha() and pt_arr[i+1].isalpha() and char == pt_arr[i+1] and current_digram in di_dict:
                    
                    # IF N-GRAM IN DICT
                    final_text += di_dict[current_digram]
                    skip = 1
                    
                else:
                    final_text += char

        else:
            skip -=1

    return final_text

def bigram_substitute(plaintext, bi_dict):
    
    pt_arr, pt_len = list(plaintext), len(plaintext)
    
    final_text = ''
    
    skip = 0
    for i, char in enumerate(pt_arr):

        if skip == 0:

            if i > pt_len-2:
                final_text += char
            else:
                
                current_bigram = ''.join(char + pt_arr[i+1])
                
                if char.isalpha() and pt_arr[i+1].isalpha() and current_bigram in bi_dict:
                    
                    final_text += bi_dict[current_bigram]
                    skip = 1
                    
                else:
                    final_text += char
                
        else:
            skip -=1

    return final_text

def trigram_substitute(plaintext, tri_dict):
    
    pt_arr, pt_len = list(plaintext), len(plaintext)
    
    final_text = ''
    
    skip = 0
    for i, char in enumerate(pt_arr):
        '''
        -2 and -3
        i and pt_arr diff starting values
        same as pt_arr[-2/-3]
        '''
        if skip == 0:

            if i > pt_len-3:
                # POST-PENULTIMATE
                final_text += char
            else:
                
                current_bigram = ''.join(char + pt_arr[i+1] + pt_arr[i+2])
                
                if char.isalpha() and pt_arr[i+1].isalpha() and pt_arr[i+2].isalpha() and current_bigram in tri_dict:
                    
                    final_text += tri_dict[current_bigram]
                    skip = 2
                    
                else:
                    final_text += char
                
        else:
            skip -=1

    return final_text


def ngram_frequency_scan(ciphertext):
    
    unii, dii, bii, trii = frequency_analysis(ciphertext, return_format='dict')
    
    # perform ngram analysis and subtitution
    uni_dec = substitute(ciphertext, unii)
    di_dec = digram_substitute(ciphertext, dii)
    bi_dec = bigram_substitute(ciphertext, bii)
    tri_dec = trigram_substitute(ciphertext, trii)

    subtitution_frequency = {}

    for char, u, d, b, t in zip(list(ciphertext), uni_dec, di_dec, bi_dec, tri_dec):
        subtitues_list = [u, d, b, t]
        if char.isalpha():
            for s in subtitues_list:
                if char.isalpha() and s.isalpha() and char != s:
                    if char not in subtitution_frequency:
                        subtitution_frequency[char] = {}
                    
                    if s not in subtitution_frequency[char]:
                        subtitution_frequency[char][s] = 1
                    else:
                        subtitution_frequency[char][s] += 1

    for k in subtitution_frequency:
        sorted_items = sorted(subtitution_frequency[k].items(), key=lambda item: item[1])
        subtitution_frequency[k] = dict(sorted_items[::-1])
    
    ngram_scan_output = ''

    for let in list(ciphertext):
        if let.isalpha() and let in subtitution_frequency:
            ngram_scan_output += list(subtitution_frequency[let].keys())[0]
        else:
            ngram_scan_output += let

    return ngram_scan_output
from .ngram import frequency_analysis
import math

def diversity_index(input_text, index='diversity'):
    
    unigram, digram, bigram, trigram = frequency_analysis(input_text.lower(), return_format='count')
    total = 0
    for _, count in unigram:
        total += count
    
    diversity_index = 0
    # freq, proportion, natural log, proportion*nLog
    for char, count in unigram:
        p = count/total
        ln = math.log(p)
        pln = p*ln
        #p_nlog = (count/total) * math.log(count/total)
        #print(char, count, p, ln, pln, '\n')
        diversity_index += pln
    
    if index == 'equitability':
        return diversity_index/math.log(len(unigram))
        
    return diversity_index


def coincidence_index(input_text):
    
    coincidence_index = 0
    char_eq = 0
    total_char = 0
    
    uni, bi, di, tri = frequency_analysis(input_text.lower(), return_format='count')
    
    for char, freq in uni:
        char_eq += freq * (freq - 1)
        total_char += freq
    
    coincidence_index = char_eq / (total_char*total_char-1)
    return coincidence_index
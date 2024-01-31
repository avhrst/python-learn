import string

def remove_punctuation(p_text: string):
    return ''.join([l for l in p_text if l not in string.punctuation])

def convert_to_lowercase(p_text: string):
    return p_text.lower()

def tokenize_text(p_text: string):
    return p_text.split()

def sentence_tokenize(p_text):
    return p_text.split('.')

def word_count(p_text: string):
    return len(tokenize_text(p_text))

def character_count(p_text: string):
    return len(remove_punctuation(p_text))

def unique_words(p_text: string):
    return set(tokenize_text(p_text))

def average_word_length(p_text: string):
    return character_count(p_text) / word_count(p_text)

def find_occurrences(p_text:string, p_keyword: string):
    return p_text.count(p_keyword) 
 
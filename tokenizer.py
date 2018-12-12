# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 17:37:48 2018

@author: Rodolpho Picolo
@email: rodolphopicolo@gmail.com
"""
import re
import sys
def word_order(word):
    return word['text'].upper() + word['text']

class Tokenizer:
    

    def __init__(self, min_word_len=None, max_word_len=None, case_sensitive=False):
        self.texts = []
        self.ignored_words = []
        self.min_word_len = min_word_len
        self.max_word_len = max_word_len
        self.case_sensitive = case_sensitive
        self.tokens = None
        
    def addText(self, text):
        self.texts.append(text)
        
        
    def analyse(self):
        
        ignored_words_dic = {}
        if self.ignored_words != None:
            for word in self.ignored_words:
                if self.case_sensitive == False:
                    ignored_words_dic[word.upper()] = None
                else:
                    ignored_words_dic[word] = None
        
        pattern = '\W'
        reg_exp = re.compile(pattern)
        words = {}
        words_list = []
        for text in self.texts:
            splitted = reg_exp.split(text)
            for word in splitted:
                if word == None or (self.min_word_len != None and len(word) < self.min_word_len):
                    continue
                if self.max_word_len != None and len(word) > self.max_word_len:
                    continue
                if self.case_sensitive == False:
                    word = word.upper()
                    
                if word in ignored_words_dic:
                    continue

                if not word in words:
                    words[word] = {
                        'text':word
                        , 'quantity': 0
                    }
                    words_list.append(words[word])
                words[word]['quantity'] = words[word]['quantity'] + 1
        
        words_list.sort(key=word_order)
        return words_list
        
    def tokenize(self):
        self.tokens = []
        words_list = self.analyse()
        for word in words_list:
            self.tokens.append(word['text'])
        return self.tokens
        
    def encode(self, text):
        print('encode')
        
    def decode(self, array):
        print('decode')

    
        
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('No file name specified')
        exit(0)
        
    file_name = sys.argv[1]
    
    ignored_words_file_name = None
    if len(sys.argv) > 2:
        ignored_words_file_name = sys.argv[2]
    
    ignored_words = []
    if ignored_words_file_name != None:
        ignored_words_file = open(ignored_words_file_name, 'r')
        ignored_words_content = ignored_words_file.read()
        ignored_words = re.split('\W', ignored_words_content)
        ignored_words_file.close()
        
    tokenizer = Tokenizer()    
    
    
    file = open(file_name, 'r')
    for line in file:
        tokenizer.addText(line)
    file.close()
    
    tokenizer.min_word_len = 3
    tokenizer.max_word_len = None
    tokenizer.case_sensitive = False
    tokenizer.ignored_words = ignored_words
    
    words = tokenizer.analyse()
    tokens = tokenizer.tokenize()

    print(ignored_words)
    '''
    for word in words:
        print(word)
    '''        
    for i in range(0, len(tokens)):
        print(tokens[i] + ' => ' + str(i))

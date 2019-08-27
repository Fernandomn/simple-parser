from simpleGrammar import *
from simpleGrammarClasses.simplegrammartoken import *
import os


def pegaPosTabela(word, tabela):
    # global tabela
    if word in tabela:
        line = tabela[word]
    else:
        return '?'
    # line = tabela[tagSetEnum[word]]
    prob = max(line)
    indexPos = line.index(prob)
    return tags_list[indexPos]


def simplePosTest(ref_lines, num_test_cases, tabela):
    print('Testing Naive POS tagger:')
    sentences_count = 0
    word_count = 0
    total_guesses = 0
    right_guesses = 0
    sentences_list = []

    for i in range(num_test_cases):
        tokens_list = []
        line = ref_lines[i]
        for wordpos in line.split():
            word_count += 1
            word = wordpos.split('_')[0]
            pos = pegaPosTabela(word, tabela)
            # parei aqui
            if pos == 'PU' and word == '.':
                sentences_count += 1
            token = SimpleGrammarToken(word, pos)
            if token.pos == wordpos.split('_')[-1]:
                right_guesses += 1
                token.setiscorrect(True)
            total_guesses += 1
            tokens_list.append(token)
        sentences_list.append(tokens_list)
        # print([(a.token, a.pos, 'right' if a.isCorrect else 'wrong') for a in sentences_list[-1]])
    print('Num. of sentences: {0}'.format(len(sentences_list)))
    print('Num of Tokens: {0}'.format(word_count))
    print('Precision: {0}'.format(right_guesses / total_guesses))

def simpleGrammarTest(ref_lines, num_test_cases, tabela):
    print('Testing Naive Grammar:')
    sentences_count = 0
    word_count = 0
    total_guesses = 0
    right_guesses = 0
    sentences_list = []

    for i in range(num_test_cases):
        tokens_list=[]
        line=ref_lines[i]
        # for original_word in line.split():


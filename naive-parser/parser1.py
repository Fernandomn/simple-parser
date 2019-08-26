from simpleGrammar import *
from simpleGrammarClasses.simplegrammartoken import *
import os

tabela = {}


def getFileName(exec_type):
    # completePath = '/home/fernando/Dropbox/ufba/MATE04 - Tópicos em Banco de Dados/atividade2'
    # os.chdir(dirname)
    # os.chdir('macmorpho-v3')
    # filename "../macmorpho-v3/macmorpho-{0}.txt".format( execType)
    # return os.path.join(dirname, 'tagset.txt')
    # PAREI AQUI

    file_name = '../macmorpho-v3/macmorpho-{0}.txt'.format(exec_type)
    dirname = os.path.abspath(file_name)
    return dirname


def pegaPosTabela(word, tabela):
    # global tabela
    line = tabela[word]
    # line = tabela[tagSetEnum[word]]
    prob = max(line)
    indexPos = line.index(prob)
    return tags_list[indexPos]


####################

def test(ref_lines, num_test_cases, tabela):
    sentences_count = 0
    tokens_list = []
    for i in range(num_test_cases):

        line = ref_lines[i]
        for wordpos in line.split():
            word = wordpos.split('_')[0]
            pos = pegaPosTabela(word, tabela)
            # parei aqui
            if pos == 'PU' and word == '.':
                sentences_count += 1
            token = SimpleGrammarToken(word, pos)
            tokens_list.append(token)


def getreflines(exec_type):
    train_set = getFileName(exec_type)

    ref_file = open(train_set, 'r')

    return ref_file.readlines()


def main():
    num_test_cases = 50
    # exec_type = 'dev'
    exec_type = 'train'

    ref_lines = getreflines(exec_type)

    training(ref_lines, num_test_cases, tabela)
    print('checkpoint')
    # procurar, pra cada palavra, a coluna com valor mais alto, e retornar a pos equivalente

    # exec_type = 'test'
    #
    # ref_lines = getreflines(exec_type)
    test(ref_lines, num_test_cases, tabela)


# test(refLines)

if __name__ == '__main__':
    main()

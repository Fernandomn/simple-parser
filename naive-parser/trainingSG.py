from tagSetDef import *
import threading
import csv
import os

pronom_dict = {}


def normalizeTable(tabela):
    # tabela
    for word, columns in tabela.items():
        totalOcurrencies = sum(columns)
        for colIndex in range(len(columns)):
            ocurrencies = tabela[word][colIndex]
            tabela[word][colIndex] = ocurrencies / totalOcurrencies
    return tabela


def imprimeTabela(diretorio, tabela):
    os.chdir(os.getcwd())
    # diretorio = 'simple_grammar'
    if not os.path.exists(diretorio):
        os.mkdir(diretorio)
    os.chdir(diretorio)
    with open(diretorio + '.csv', 'w') as grammar:
        w = csv.writer(grammar)
        # w.writerow(tabela.keys())
        if diretorio == 'simple_grammar':
            w.writerow(['palavra'] + tags_list)
        else:
            w.writerow(['pos'] + tags_list)

        for item in tabela.items():
            w.writerow([item[0]] + item[1])


def simplePosTraining(refLines, numTestCases, tabela):
    for i in range(numTestCases):
        line = refLines[i]
        wordVector = line.split()

        for wordpos in wordVector:
            word = wordpos.split('_')[0]
            POS = wordpos.split('_')[-1].strip()

            if '+' in POS:
                # print('linha: {0} /word: {1} /pos: {2}'.format(i, word, POS))
                pos1 = POS.split('+')[0]
                pos2 = POS.split('+')[-1]
                list_pos = [pos1, pos2]
            else:
                list_pos = [POS]

            if not word in tabela:
                columns = [0 for i in range(len(list(tagSetEnum)))]
                # tabela.update([(word, columns)])
                tabela[word] = columns
            for pos in list_pos:
                tagIndex = tagSetEnum[pos].value - 1
                tabela[word][tagIndex] += 1

    tabela = normalizeTable(tabela)
    # imprimeTabela(tabela)
    threading.Thread(target=imprimeTabela('simple_pos_table', tabela)).start()
    return tabela


def simpleGrammarTraining(refLines, numTestCases, tabela):
    for i in range(numTestCases):
        actual_POS = 'S'
        line = refLines[i]
        wordVector = line.split()

        for word_pos in wordVector:
            word, pos = word_pos.split('_')
            if not actual_POS in tabela:
                columns = [0 for i in range(len(list(tagSetEnum)))]
                tabela[actual_POS] = columns
            tagIndex = tagSetEnum[pos].value - 1
            tabela[actual_POS][tagIndex] += 1
            actual_POS = pos
    tabela = normalizeTable(tabela)
    threading.Thread(target=imprimeTabela('simple_grammar', tabela)).start()

    return tabela

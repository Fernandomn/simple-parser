from trainingSG import *
from testingSG import *
from simpleGrammarClasses.simplegrammartoken import *
import os

# simple pos table
tabelaSP = {}

# simple grammar table
tabelaSG = {}


def getFileName(exec_type):
    file_name = '../macmorpho-v3/macmorpho-{0}.txt'.format(exec_type)
    dirname = os.path.abspath(file_name)
    return dirname


def getreflines(exec_type):
    train_set = getFileName(exec_type)

    ref_file = open(train_set, 'r')

    return ref_file.readlines()


def main():
    num_test_cases = 50
    # exec_type = 'dev'
    exec_type = 'train'

    ref_lines = getreflines(exec_type)

    simplePosTraining(ref_lines, num_test_cases, tabelaSP)
    # tabelaSP = simplePosTraining(ref_lines, num_test_cases, tabelaSP)
    simpleGrammarTraining(ref_lines, num_test_cases, tabelaSG)
    # tabelaSG = simpleGrammarTraining(ref_lines, num_test_cases, tabelaSG)
    # print('checkpoint')
    # procurar, pra cada palavra, a coluna com valor mais alto, e retornar a pos equivalente

    # exec_type = 'test'
    #
    # COLOCAR OPÇÕES DE ENTRADA PARA MODIFICAR OS TESTES

    # ref_lines = getreflines(exec_type)
    simplePosTest(ref_lines, num_test_cases, tabelaSP, tabelaSG)
    # simpleGrammarTest(ref_lines, num_test_cases, tabelaSG)


# test(refLines)

if __name__ == '__main__':
    main()

"""
    Atenção alunos. Deste código apenas a função getSudoku() deve ser utilizada.
    
    A função getSudoku() não recebe parâmetros e retorna uma lista de listas de inteiros que representam 
    um sudoku válido gerado aleatoriamente.
    
    Este código foi alterado por Gabriel Cardoso de Carvalho a partir do código obtido do endereço https://www.techwithtim.net/tutorials/python-programming/sudoku-solver-backtracking/
    
    Último acesso em 16/08/2021.
"""

import random



def shuffle(lista):
    random.shuffle(lista)
    return lista

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    
    for i in shuffle(list(range(1,10))):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

def getSudoku():
    board = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]
    solve(board)
    return board

def main():
    '''
    Modifiquei a main por que o arquivo original estava recebendo uma variavel inexistente, modificada para rodar no cmd
    '''
    board = getSudoku()
    print_board(board)
    print("___________________")
    print_board(board)
    solve(board)
    
if __name__=="__main__":
    main()
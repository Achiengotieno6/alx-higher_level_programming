#!/usr/bin/python3
"""
Solution for N Queens problem
"""


import sys


def solve_nqueens(N):
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [['.'] * N for _ in range(N)]
    solutions = []
    backtrack(board, 0, solutions)
    print_solutions(solutions)


def backtrack(board, col, solutions):
    N = len(board)
    if col == N:
        solutions.append(board_to_string(board))
        return

    for row in range(N):
        if is_safe(board, row, col):
            board[row][col] = 'Q'
            backtrack(board, col + 1, solutions)
            board[row][col] = '.'


def is_safe(board, row, col):
    N = len(board)

    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check if there is a queen in the upper diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check if there is a queen in the lower diagonal
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 'Q':
            return False
        i += 1
        j -= 1

    return True


def board_to_string(board):
    return [''.join(row) for row in board]


def print_solutions(solutions):
    for solution in solutions:
        for row in solution:
            print(row)
        print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)

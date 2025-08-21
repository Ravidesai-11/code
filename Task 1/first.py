from typing import List

def solve_sudoku(board: List[List[str]]) -> None:
    def is_valid(r: int, c: int, ch: str) -> bool:
       
       
        for i in range(9):
            if board[r][i] == ch: return False
            if board[i][c] == ch: return False
            
            if board[3*(r//3) + i//3][3*(c//3) + i%3] == ch:
                return False
        return True

    def solve() -> bool:
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    for num in map(str, range(1, 10)):
                        if is_valid(r, c, num):
                            board[r][c] = num
                            if solve():
                                return True
                            board[r][c] = '.'  
                    return False 
        return True 

    solve()


board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]


solve_sudoku(board)


for row in board:
    print(row)

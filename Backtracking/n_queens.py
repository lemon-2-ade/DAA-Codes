from typing import List

def solve_n_queens(n: int):
    result = []
    col = [-1] * n

    def queens(i: int):
        if i == n:
            result.append(create_board())
            print_board(result[-1])
        else:
            for j in range(n):
                col[i] = j
                if is_safe(i):
                    queens(i + 1)


    def is_safe(i: int):
        for k in range(i):
            if (col[i] == col[k]) or (abs(col[i] - col[k]) == i - k):
                return False
        return True
    
    def create_board():
        board = []

        for i in range(n):
            row = ['.'] * n
            row[col[i]] = 'Q'
            board.append(''.join(row))
        
        return board
    
    def print_board(board: List[List[str]]):
        for row in board:
            print(''.join(row))
        print()

    queens(0)
    return result

if __name__ == "__main__":

    rows = int(input("Enter the numbers of rows: "))
    results = solve_n_queens(rows)
    
    # for result in results:
    #     print("\n".join(result))
    #     print()
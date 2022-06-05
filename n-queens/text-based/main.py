import argparse

def print_queens(arr_queens):
    for row in range(len(arr_queens)):
        for col in range(len(arr_queens)):
            if arr_queens[row][col] > 0:
                print('Q ', end='')
            else:
                print('- ', end='')
        print('')

def fill_attacking_squares(arr_queens, row, col, should_undo):
    multiplier = -1 if should_undo else 1
    
     # fill in attacking squares in same row
    for col_ctr in range(len(arr_queens)):
        arr_queens[row][col_ctr] -= 1 * multiplier
     # fill in attacking squares in same column
    for row_ctr in range(len(arr_queens)):
        arr_queens[row_ctr][col] -= 1  * multiplier
    # diagonals
    diagonal_tuples = []
    
    for val in range(1, len(arr_queens)):
        if row - val >= 0:
            if col - val >= 0:
                diagonal_tuples.append((row - val, col - val))
            if col + val <= len(arr_queens) - 1:
                diagonal_tuples.append((row - val, col + val))
        if row + val <= len(arr_queens) - 1:
            if col - val >= 0:
                diagonal_tuples.append((row + val, col - val))
            if col + val <= len(arr_queens) - 1:
                diagonal_tuples.append((row + val, col + val))
    
    for tuple in diagonal_tuples:
        arr_queens[tuple[0]][tuple[1]] -= 1 * multiplier
    
def solve_helper(arr_queens, queen_ctr):
    #boundary condition
    if (queen_ctr > len(arr_queens)):
        print_queens(arr_queens)
        return
    
    for col in range(len(arr_queens)):
        if (arr_queens[queen_ctr-1][col] == 0):
            # fill neighbors
            fill_attacking_squares(arr_queens, queen_ctr-1, col, False)
            # place queen
            arr_queens[queen_ctr-1][col] = queen_ctr
            
            # place next queen
            solve_helper(arr_queens, queen_ctr + 1)
            
            # undo neighbor fill
            fill_attacking_squares(arr_queens, queen_ctr-1, col, True)

            # undo place queen
            arr_queens[queen_ctr-1][col] = 0


def solve(num_queens):
    """ method to solve n-queens and print successful configurations """
    arr_queens = [[0 for i in range(num_queens)] for j in range(num_queens)]
    solve_helper(arr_queens, 1)


if __name__=="__main__":
    parser = argparse.ArgumentParser("solver")
    parser.add_argument("queens", help="number of queens a.k.a the dimensions of the board", type=int)

    num_queens = parser.parse_args().queens

    if not num_queens:
        raise Exception('Input value for queens should not be empty')
    
    solve(num_queens)
import argparse

def solve(num_queens):
    """ method to solve n-queens and print successful configurations """
    
    # start with text-based approach
    # change to react
    
if __name__=="__main__":
    parser = argparse.ArgumentParser("solver")
    parser.add_argument("queens", help="number of queens a.k.a the dimensions of the board", type=int)

    num_queens = parser.parse_args().queens

    if not num_queens:
        raise Exception('Input value for queens should not be empty')
    
    solve(num_queens)
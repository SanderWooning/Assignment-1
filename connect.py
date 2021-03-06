import typing
import numpy as np


# Codes that we use. DO NOT CHANGE THESE.
RED = 1
BLUE = 2
DRAW = -2
IN_PROGRESS = -1
BLUE_WIN = BLUE
RED_WIN = RED


class ConnectFour:
    def __init__(self, width: int, height: int):
        """
        The ConnectFour object, containing all information and functions required for the assignment

        :param width: The width of the rectangular board
        :param height: The height of the board
        """
        self.width = width
        self.height = height
        assert self.width >= 4 and self.height >= 4, "The width and height should be at least 4"

        self.board = np.zeros((self.height, self.width))

    def print_board(self) -> None:
        """
        Prints the board in human readable format
        """

        raise NotImplementedError()

    
    def place_disc(self, row_idx: int, col_idx: int, player: int) -> None:
        """
        Place a disc of the current player on the given location, assuming that it is a legal move 
        (this legality check should be done in a different function)

        :param row_idx: The row id (0 = top, self.height-1 = bottom)
        :param col_idx: The column id (0 = leftmost, self.width-1 = rightmost)
        :param player: The player to make the move
        """

        raise NotImplementedError()
    

    def get_available_moves(self) -> typing.List[typing.Tuple[int,int]]:
        """
        Returns a list of legal moves   

        :return: The list of move tuples (row id, column id)
        """

        raise NotImplementedError()


    def is_horizontal_win(self, player: int) -> bool:
        """
        Check whether there are 4 connected discs for the given player horizontally

        :param player: The player for which we check whether there is a horizontal win

        :return: True if the player has 4 horizontally connected discs else False
        """

        raise NotImplementedError()

    
    def is_vertical_win(self, player: int) -> bool: 
        """
        Check whether there are 4 connected discs for the given player vertically

        :param player: The player for which we check whether there is a vertical win

        :return: True if the player has 4 vertically connected discs else False
        """

        raise NotImplementedError()
    
    def is_diagonal_win(self, player: int) -> bool:
        """
        Check whether there are 4 connected discs for the given player diagonally

        :param player: The player for which we check whether there is a diagonal win

        :return: True if the player has 4 diagonal connected discs else False
        """
        
        raise NotImplementedError()
        
    
    def has_player_won(self, player: int) -> bool:
        """
        Check whether the given player has won

        :param player: The player for which we check whether there is a win

        :return: True if the player has won else False 
        """

        raise NotImplementedError()

    def get_game_status(self) -> int:
        """
        Returns the status of the game (inprogress, draw, win for blue, win for red)

        :return: one of the following:
                - IN_PROGRESS if the game is in progress
                - DRAW if the game ended in a draw
                - RED_WIN if red won
                - BLUE_WIN if blue won
        """

        raise NotImplementedError()


    def can_player_win(self, player: int) -> bool:
        """
        Recursive function that checks whether the given player (who is also to move) 
        can win from the current board position given by self.board.
        Refer to the assignment text for the exact winning criterion (not the default one!).

        :return: True if the player can win, False otherwise
        """
        
        raise NotImplementedError()

    
    def best_move_greedy(self, player: int) -> typing.Tuple[int, int]:
        """
        OPTIONAL. Design a greedy function to determine the best move to play. This
        algorithm involves enumerating all possible moves, and determining
        which of the moves seems good, without looking further ahead. A logical
        greedy approach would be to the following:
         - if we can win in one move, play that move
         - else, play our opponent's best move (the one maximizing the chain length of the opponent's color) 
        This way, the opponent can hopefully not win, and we win if we can in 1 move. It may be a good idea to formulate 
        new functions that are slight alterations of, e.g., is_horizontal_win, is_vertical_win, and is_diagonal_win.

        :return: The best move according to the function in the form (row_id, col_id)
        """

        raise NotImplementedError()
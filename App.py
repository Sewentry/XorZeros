import TicTacToeBoard

game = TicTacToeBoard.TicTacToeBoard()
game.new_game()
game.get_field()
while(True):
    print("Crosess player's turn")
    game.make_move(1)
    game.get_field()
    if(game.check_field(1)==True):
        print("Crosses win!")
        break
    if(game.is_field_full()==True):
        print("Draw!")
        break
    print("Zeroes player's turn")
    game.make_move(0)
    game.get_field()
    if(game.check_field(0)==True):
        print("Zeros Win!")
        break
    if(game.is_field_full()==True):
        print("Draw!")
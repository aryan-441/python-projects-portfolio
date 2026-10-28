
def tic_tac_toe():
    print("Welcome to tic-tac-toe. The number pad on the right-side of your keyboard forms a board. Therefore, if you want to play the top-left corner, you press 7, for the centre you press 5, and so on,")
    def check_team():
       
        while True:
            player1_marker = input("Enter 'O' for Noughts or 'X' for Crosses: ").upper()
            
            if player1_marker == 'O':
                print("Player 1 is noughts and player 2 is crosses")
                player2_marker = 'X'
                return player1_marker, player2_marker
                break
            elif player1_marker == 'X':
                print("Player 1 is crosses and player 2 is noughts")
                player2_marker = 'O'
                return player1_marker, player2_marker
                break
            else:
                print("Invalid input. Please enter 'O' or 'X'.")

       
                

    
    def display_board(board):
        print('\n'*100)
       
        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')
    test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
   

    def place_marker(board,marker,position):
        board[position] = marker

    def win_check(board, mark):
        # All possible win combinations
        win_combos = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],  # horizontal
            [1, 4, 7], [2, 5, 8], [3, 6, 9],  # vertical
            [1, 5, 9], [3, 5, 7]              # diagonals
        ]
        
        # Use regular for loop for clarity
        for combo in win_combos:
            win = True
            for pos in combo:
                if board[pos] != mark:
                    win = False
                    break
            if win:
                return True
        return False
    def board_full(board):             #checks if the board is full and the game is completed
        # Check each position from 1 to 9
        for i in range(1, 10):
            if board[i] == ' ':
                return False  # Found an empty space
        return True  # No empty spaces found

    
    #Game setup:
    def play_game():
        player1_marker, player2_marker = check_team()
        board = ['#'] + [' '] * 9
        current_marker = player1_marker
        current_player = 1
        game_on = True

        while game_on:
            display_board(board)
            try:
                position = int(input(f"Player{current_player} ({current_marker}), choose your position (1-9)."))
            except ValueError:
                print("Invalid input")
                continue


            if position < 1 or position > 9:
                print("Position must be between 1 and 9.")
                continue
            if board[position] != ' ':
                print("position is already taken. Try again.")
                continue
            place_marker(board,current_marker,position)


            if win_check(board,current_marker):
                display_board(board)
                print(f"Player{current_player} ({current_marker}) wins!")
                game_on = False

            elif board_full(board):
                display_board(board)
                print("It's a tie.")
                game_on = False

            else:
                if current_player == 1:
                    current_player = 2
                    current_marker = player2_marker
                else:
                    current_player = 1
                    current_marker = player1_marker

       

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == 'y':
            play_game()  # Recursively call to restart the game
        else:
            print("Thanks for playing!")
    play_game()

    
    

tic_tac_toe()

        

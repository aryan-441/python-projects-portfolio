''' 
Rock-Paper-Scissor game against bot.
'''
import random
print("The ASCII art for rock, paper, and scissor in that order that will be returned is as follows:")
print("""
      ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
ascii_rock = '''
      ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
# Paper
print("""
      PAPER
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

ascii_paper = """
      PAPER
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
print("""
      SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
ascii_scissor = """
      SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
bot_score = 0
player_score = 0

bot_choices = ['rock','paper','scissor']
play_game = True
while play_game:
    choice = input("Enter R for rock, P for paper, or S for scissors").strip().upper()
    bot_game_choice = random.choice(bot_choices)
    #turns = 0

    if (choice == 'R' and bot_game_choice == 'rock') or (choice == 'P' and bot_game_choice == 'paper') or (choice == 'S' and bot_game_choice == 'scissor'):
        print("Tie!")
        if choice == 'R':
            print(f"Player: {ascii_rock}, Bot: {ascii_rock}")
        elif choice == 'P':
             print(f"Player: {ascii_paper}, Bot: {ascii_paper}")
        elif choice == 'S':
             print(f"Player: {ascii_scissor}, Bot: {ascii_scissor}")
        bot_score += 1
        player_score += 1
        print(f"Bot score: {bot_score}\nPlayer score: {player_score}")
        
    elif choice == 'R' and bot_game_choice == 'paper':
        print("Bot wins!")
        print(f"Player: {ascii_rock}, Bot: {ascii_paper}")
        bot_score += 1
        print(f"Bot score: {bot_score}\nPlayer score: {player_score}")
    elif choice == 'R' and bot_game_choice == 'scissor':
        print("Player wins!")
        print(f"Player: {ascii_rock}, Bot: {ascii_scissor}")
        player_score += 1
        print(f"Bot score: {bot_score}\nPlayer score: {player_score}")
    elif choice == 'P' and bot_game_choice == 'rock':
        print("Player wins!")
        print(f"Player: {ascii_paper}, Bot: {ascii_rock}")
        player_score += 1
        print(f"Bot score: {bot_score}\nPlayer score: {player_score}")
    elif choice == 'P' and bot_game_choice == 'scissor':
        print("Bot wins!")
        print(f"Player: {ascii_paper}, Bot: {ascii_scissor}")
        bot_score += 1
        print(f"Bot score: {bot_score}\nPlayer score: {player_score}")
    elif choice == 'S' and bot_game_choice == 'rock':
        print("Bot wins!")
        print(f"Player: {ascii_scissor}, Bot: {ascii_rock}")
        bot_score += 1
        print(f"Bot score: {bot_score}\nPlayer score: {player_score}")
    elif choice == 'S' and bot_game_choice == 'paper':
        print("Player wins!")
        print(f"Player: {ascii_scissor}, Bot: {ascii_paper}")
        player_score += 1
        print(f"Bot score: {bot_score}\nPlayer score: {player_score}")
    else:
        print("Invalid choice.")
        print(f"Bot score: {bot_score}\nPlayer score: {player_score}")
    if player_score == 3 or bot_score == 3:
   
        if player_score > bot_score:
            print(f"\n\nGame Over!\n\nPlayer Score: {player_score}\nBot score: {bot_score}\nPlayer Wins!")
        elif player_score < bot_score:
            print(f"\n\nGame Over!\n\nPlayer Score: {player_score}\nBot score: {bot_score}\nBot Wins!")
        else:
            pass
        play_game = False
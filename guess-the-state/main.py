import turtle
import pandas
screen = turtle.Screen()
filepath = 'blank_states_img.gif'
screen.title("U.S. States Game")
screen.addshape(filepath)
turtle.shape(filepath)
screen.tracer(0)  

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
guesses = 0

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.goto(-280, 260) 

current_input = ""
game_on = True
def update_ui():
    if not game_on:
        return
    writer.clear()
    writer.goto(-280,260)
    score = len(guessed_states)
    writer.write(f"Guesses: {score}/50 | Guess: {current_input}",align='left', font=("Arial", 18, "bold"))
    screen.update()

def add_letter(char):
    global current_input
    if game_on:
        current_input += char
        update_ui()

def backspace():
    global current_input
    if game_on:

        current_input = current_input[:-1]
        update_ui()
def add_space():
    global current_input
    if game_on:
        current_input += ' '

def submit():
    global current_input,game_on
    if not game_on:
        return
    #global guesses
    
    guess = current_input.strip().title()

    print(f"User submitted: {current_input}")
    if guess in all_states and guess not in guessed_states:
        guessed_states.append(guess)
        
        
        state_data = data[data.state == guess] #row of state data- state,x,y
        state_x = int(state_data.x.item())
        state_y = int(state_data.y.item())

        map_writer = turtle.Turtle()
        map_writer.penup()
        map_writer.hideturtle()
        map_writer.goto(state_x,state_y)
        map_writer.write(guess,align='center',font=('Arial',10,'bold'))
        

    
    current_input = ""
    update_ui()

    if len(guessed_states) == 50:
        game_on = False
        writer.goto(0,0)
        writer.pencolor('green')
        writer.write("YOU WIN! All states have been found!",align='center',font=("Arial",30,'bold'))
        screen.update()


screen.listen()


alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for char in alphabet:
    screen.onkey(lambda letter=char: add_letter(letter), char)

screen.onkey(backspace, "BackSpace")
screen.onkey(submit, "Return")
screen.onkey(add_space, 'space')


update_ui()

screen.mainloop()
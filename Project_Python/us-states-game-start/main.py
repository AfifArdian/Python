import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pandas.read_csv("50_states.csv")
guessed_states = []
# all_states = df.state.tolist()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 State Correct",
                                    prompt="what's another state's name?").title()
    if answer_state == "Exit":
        missing_state = [state for state in df.state if state not in guessed_states]
        data_dict = { "missing_state": missing_state}
        df_missing_state = pandas.DataFrame(data=data_dict)
        df_missing_state.to_csv("states_to_learn.csv")
        break

    for states in range(len(df)):
        if answer_state == df.state[states] and answer_state not in guessed_states:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            state_data = df[df.state == answer_state]
            # version create by me
            x_cor = state_data.x[states]
            y_cor = state_data.y[states]

            # # version 2
            # x_cor = state_data.x.item()
            # y_cor = state_data.y.item()

            t.penup()
            t.hideturtle()
            t.goto(x_cor, y_cor)
            t.write(answer_state)


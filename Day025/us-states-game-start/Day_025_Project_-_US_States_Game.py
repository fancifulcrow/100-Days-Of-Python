import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
# turtle can only read gif
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Get the mouse coordinates
# def get_mouse_click_coordinates(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coordinates)
# turtle.mainloop()

text_writer = turtle.Turtle()
text_writer.penup()
text_writer.hideturtle()


def write_states(x, y, name):
    text_writer.goto(x, y)
    text_writer.pendown()
    text_writer.write(name, align="center", font=("Arial", 9, "normal"))
    text_writer.penup()


data = pandas.read_csv("50_states.csv")
data_states_list = data["state"].to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct",
                                    prompt="What's another state's name").title()

    if answer_state == "Exit":
        missing_states = []
        for state in data_states_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in data_states_list and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = data[data["state"] == answer_state]
        # item() gets the value of the item without the data type bing written as well
        write_states(x=int(state_data.x), y=int(state_data.y), name=state_data.state.item())

screen.exitonclick()

import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = tkinter.Label(text=f"Score: {self.quiz.score}", foreground="white", background=THEME_COLOR, font=("Ariel,", 20, "bold"))
        self.score_label.grid(row=0, column=1)

        self.canvas = tkinter.Canvas(width=300, height=250, background="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Question", fill=THEME_COLOR, font=("Ariel", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = tkinter.PhotoImage(file="images/true.png")
        self.true_button = tkinter.Button(image=true_img, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_img = tkinter.PhotoImage(file="images/false.png")
        self.false_button = tkinter.Button(image=false_img, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
        
        self.score_label.config(text=f"Score: {self.quiz.score}")

        self.window.after(1000, self.get_next_question)
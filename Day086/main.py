from tkinter import *
import random
import time

class TypingSpeedTest:
    def __init__(self, window):
        self.window = window
        self.window.title("Typing Speed Test")

        # A list of sentences to randomly choose from
        self.sentences = [
            "The quick brown fox jumps over the lazy dog.",
            "Python is a powerful and versatile programming language.",
            "Practice makes perfect.",
        ]
        self.current_sentence = ""
        self.typing_start_time = None
        self.typing_finished = False

        self.title_label = Label(window, text="Typing Speed Text", font=("Times New Roman", 24, "bold"), padx=200)
        self.title_label.grid(row=0, column=1)

        # Displaying the random sentences
        self.sentence_label = Label(window, text="", font=("Arial", 16))
        self.sentence_label.grid(row=1, column=1)

        # place for users to type in
        self.entry = Entry(window, font=("Arial", 14))
        self.entry.grid(row=2, column=1)

        # view the results
        self.result_label = Label(window, text="Typing Speed: \nAccuracy:", font=("Arial", 14))
        self.result_label.grid(row=3, column=1)

        # start button
        self.start_button = Button(window, text="Start Typing Test", command=self.start_typing_test, font=("Arial", 14))
        self.start_button.grid(row=4, column=1)

    def start_typing_test(self):
        # start the game
        if not self.typing_finished:
            self.current_sentence = random.choice(self.sentences)
            self.sentence_label.config(text=self.current_sentence)
            self.entry.delete(0, END)
            self.result_label.config(text="Typing Speed: \nAccuracy:")
            self.typing_start_time = time.time()
            self.start_button.config(text="Finish Typing Test")
            self.typing_finished = True
        else:
            # end the game
            typed_text = self.entry.get()
            elapsed_time = time.time() - self.typing_start_time
            words = typed_text.split()
            word_count = len(words)

            # Calculate typing speed in words per minute (WPM)
            wpm = int((word_count / elapsed_time) * 60)

            # Check accuracy
            accuracy = self.calculate_accuracy(typed_text, self.current_sentence)

            # Display the result
            result_text = f"Typing Speed: {wpm} WPM\nAccuracy: {accuracy}%"
            self.result_label.config(text=result_text)

            self.start_button.config(text="Start Again")
            self.typing_finished = False

    def calculate_accuracy(self, typed_text, original_text):
        typed_words = typed_text.split()
        original_words = original_text.split()

        correct_words = 0

        for typed_word, original_word in zip(typed_words, original_words):
            if typed_word == original_word:
                correct_words += 1

        accuracy = (correct_words / len(original_words)) * 100
        return round(accuracy, 2)


root = Tk()
app = TypingSpeedTest(root)
root.mainloop()

from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
HEADING_FONT = ("Arial", 40, "bold")
SUBHEADING_FONT = ("Arial", 30, "bold")
TEXT_FONT = ("Arial", 20, "italic")
CHOICES_FONT = ("Arial", 14, "normal")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # |-------------------------- QUIZ WINDOW --------------------------|
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=50, pady=20)

        self.quizzler = Label(text="Quizzler", fg="white", bg=THEME_COLOR, font=HEADING_FONT)
        self.quizzler.grid(row=0, column=0, columnspan=2)

        self.score = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR, font=SUBHEADING_FONT)
        self.score.grid(row=1, column=0, columnspan=2)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="Question Text", font=TEXT_FONT,
                                                     fill="black", width=280)
        self.canvas.grid(row=2, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.ans_true, bd=0)
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.ans_false, bd=0)
        self.true_button.grid(row=3, column=0)
        self.false_button.grid(row=3, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.buttons_state("active")
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.buttons_state("disabled")

    def ans_true(self):
        self.give_feedback(self.quiz.check_answer("true"))
        self.buttons_state("disabled")

    def ans_false(self):
        self.give_feedback(self.quiz.check_answer("false"))
        self.buttons_state("disabled")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def buttons_state(self, state_):
        self.true_button.config(state=state_)
        self.false_button.config(state=state_)


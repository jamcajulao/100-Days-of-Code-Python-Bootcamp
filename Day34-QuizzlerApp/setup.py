from tkinter import *
from tkinter import ttk

THEME_COLOR = "#375362"
HEADING_FONT = ("Arial", 40, "bold")
SUBHEADING_FONT = ("Arial", 30, "bold")
TEXT_FONT = ("Arial", 20, "italic")
CHOICES_FONT = ("Arial", 14, "normal")


class SetupInterface:

    def __init__(self):
        self.selected_difficulty = ""
        self.selected_category = ""

        self.setup = Tk()
        self.setup.title("Setup")
        self.setup.config(bg=THEME_COLOR, padx=50, pady=20)

        self.setup_label = Label(text="Setup", bg=THEME_COLOR, font=HEADING_FONT)
        self.setup_label.grid(row=0, column=0, pady=20, columnspan=2)

        self.categories_label = Label(text="Select a category: ", bg=THEME_COLOR, font=TEXT_FONT, justify=LEFT)
        self.categories_label.grid(row=1, column=0, pady=10, sticky=W)

        self.category = StringVar()
        self.categories = ttk.Combobox(textvariable=self.category, font=CHOICES_FONT)

        self.categories["values"] = ['General Knowledge', 'Entertainment: Books', 'Entertainment: Film',
                                     'Entertainment: Music', 'Entertainment: Musicals & Theatres',
                                     'Entertainment: Television', 'Entertainment: Video Games',
                                     'Entertainment: Board Games', 'Science & Nature', 'Science: Computers',
                                     'Science: Mathematics', 'Mythology', 'Sports', 'Geography', 'History', 'Politics',
                                     'Art', 'Celebrities', 'Animals', 'Vehicles', 'Entertainment: Comics',
                                     'Science: Gadgets', 'Entertainment: Japanese Anime & Manga',
                                     'Entertainment: Cartoon & Animations']
        self.categories.state(["readonly"])
        self.categories.grid(row=1, column=1, sticky=W)

        self.difficulty_label = Label(text="Select difficulty: ", bg=THEME_COLOR, font=TEXT_FONT)
        self.difficulty_label.grid(row=2, column=0, pady=10, sticky=W)

        self.difficult = StringVar()
        self.difficulty = ttk.Combobox(textvariable=self.difficult, font=CHOICES_FONT)
        self.difficulty["values"] = ["Easy", "Medium", "Hard"]
        self.difficulty.state(["readonly"])
        self.difficulty.grid(row=2, column=1, sticky=W)

        okay_button = Button(text="Start Quiz", highlightbackground=THEME_COLOR,
                             command=self.finish_setup, font=CHOICES_FONT)
        okay_button.grid(row=3, column=0, pady=10, columnspan=2)

        self.setup.mainloop()

    def finish_setup(self):
        category_list = {'General Knowledge': 9, 'Entertainment: Books': 10, 'Entertainment: Film': 11,
                         'Entertainment: Music': 12, 'Entertainment: Musicals & Theatres': 13,
                         'Entertainment: Television': 14, 'Entertainment: Video Games': 15,
                         'Entertainment: Board Games': 16, 'Science & Nature': 17, 'Science: Computers': 18,
                         'Science: Mathematics': 19, 'Mythology': 20, 'Sports': 21, 'Geography': 22, 'History': 23,
                         'Politics': 24, 'Art': 25, 'Celebrities': 26, 'Animals': 27, 'Vehicles': 28,
                         'Entertainment: Comics': 29, 'Science: Gadgets': 30,
                         'Entertainment: Japanese Anime & Manga': 31, 'Entertainment: Cartoon & Animations': 32}

        self.selected_category = category_list[self.categories.get()]
        self.selected_difficulty = self.difficulty.get().lower()

        self.setup.destroy()

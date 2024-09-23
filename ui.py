from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.quiz_b = quiz_brain
        
        # Initialize score label and layout first
        self.lbl = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 12))
        self.lbl.grid(column=1, row=0)

        # Initialize the canvas to display questions
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.cv_text = self.canvas.create_text(150, 125, text="Questions go here", font=("Arial", 20, "italic"), width=280, fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Load button images
        self.true_img = PhotoImage(file="./images/true.png")
        self.false_img = PhotoImage(file="./images/false.png")

        # Create buttons for True and False
        self.true_btn = Button(image=self.true_img, highlightthickness=0, command=self.true_pressed)
        self.true_btn.grid(column=0, row=2)

        self.false_btn = Button(image=self.false_img, highlightthickness=0, command=self.false_pressed)
        self.false_btn.grid(column=1, row=2)

        self.get_nxt_question()
        # Start the window main loop
        self.window.mainloop()

    def get_nxt_question(self):
        self.canvas.config(bg="white")
        if self.quiz_b.still_has_questions():
            q_text = self.quiz_b.next_question()
            self.lbl.config(text=f"Score: {self.quiz_b.score}")
            self.canvas.itemconfig(self.cv_text, text=q_text)
        else:
            self.canvas.itemconfig(self.cv_text, text="You've reached the end of the quiz ")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_pressed(self):
        self.give_fb(self.quiz_b.check_answer("True"))
        self.lbl.config(text=f"Score: ")
        print("True button pressed")
        # Implement functionality for when True button is pressed
    
    def false_pressed(self):
        self.give_fb(self.quiz_b.check_answer("False"))
        self.lbl.config(text=f"Score:")
        # self.canvas.itemconfig(cv_text, text=f"{self.}")
        print("False button pressed")
        # Implement functionality for when False button is pressed

    def give_fb(self,is_right):
        if is_right==True:
            self.canvas.config(bg="green")
        else: 
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_nxt_question)
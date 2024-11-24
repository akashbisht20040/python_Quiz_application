import tkinter as tk
from tkinter import messagebox
import random

# Quiz data embedded directly in the script
quiz_data = [
    {
        "question": "What is the output of 2 ** 3 in Python?",
        "options": ["6", "8", "9", "12"],
        "answer": "8"
    },
    {
        "question": "Which data type is mutable in Python?",
        "options": ["tuple", "list", "string", "int"],
        "answer": "list"
    },
    {
        "question": "What is the keyword to create a class in Python?",
        "options": ["def", "class", "object", "create"],
        "answer": "class"
    }
]

# Shuffle questions for variety
random.shuffle(quiz_data)

# Initialize variables
current_question = 0
score = 0
timer_seconds = 30  # Time per question in seconds
timer_id = None

# Functions
def load_question():
    """Loads the current question and options into the GUI."""
    global timer_seconds, timer_id
    question_label.config(text=f"Q{current_question + 1}/{len(quiz_data)}: {quiz_data[current_question]['question']}")
    for i, option in enumerate(quiz_data[current_question]["options"]):
        options[i].config(text=option, value=option)
    selected_option.set("")
    timer_seconds = 30
    update_timer()

def next_question():
    """Processes the user's answer and moves to the next question."""
    global current_question, score, timer_id
    root.after_cancel(timer_id)  # Stop the timer
    if selected_option.get() == "":
        messagebox.showwarning("Warning", "Please select an answer!")
        return
    if selected_option.get() == quiz_data[current_question]["answer"]:
        messagebox.showinfo("Correct!", "Your answer is correct!")
        score += 1
    else:
        messagebox.showerror("Incorrect", f"Correct answer: {quiz_data[current_question]['answer']}")
    
    current_question += 1
    if current_question < len(quiz_data):
        load_question()
    else:
        show_results()

def show_results():
    """Displays the final results and ends the quiz."""
    global score
    messagebox.showinfo(
        "Quiz Finished",
        f"Your final score is {score}/{len(quiz_data)}.\n\nClick OK to close."
    )
    root.destroy()

def update_timer():
    """Updates the countdown timer."""
    global timer_seconds, timer_id
    if timer_seconds > 0:
        timer_label.config(text=f"Time Left: {timer_seconds} seconds")
        timer_seconds -= 1
        timer_id = root.after(1000, update_timer)
    else:
        messagebox.showwarning("Time's Up!", "You ran out of time for this question.")
        next_question()

# GUI setup
root = tk.Tk()
root.title("Python Quiz App")
root.geometry("600x400")
root.configure(bg="#f7f6f2")

# Header image (optional)
header_frame = tk.Frame(root, bg="#4CAF50")
header_frame.pack(fill="x")
header_label = tk.Label(
    header_frame,
    text="Python Quiz App",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="#4CAF50",
    pady=10
)
header_label.pack()

# Question frame
question_frame = tk.Frame(root, bg="#f7f6f2", padx=10, pady=20)
question_frame.pack(fill="both", expand=True)

question_label = tk.Label(
    question_frame,
    text="",
    font=("Arial", 16),
    bg="#f7f6f2",
    wraplength=550,
    justify="left"
)
question_label.pack(pady=10)

# Timer
timer_label = tk.Label(
    root,
    text=f"Time Left: {timer_seconds} seconds",
    font=("Arial", 12),
    fg="red",
    bg="#f7f6f2"
)
timer_label.pack(pady=5)

# Options (Radio Buttons)
selected_option = tk.StringVar()
options_frame = tk.Frame(root, bg="#f7f6f2")
options_frame.pack()

options = [
    tk.Radiobutton(
        options_frame,
        text="",
        variable=selected_option,
        value="",
        font=("Arial", 12),
        bg="#f7f6f2",
        activebackground="#f7f6f2"
    )
    for _ in range(4)
]
for option in options:
    option.pack(anchor="w", pady=5)

# Buttons frame
buttons_frame = tk.Frame(root, bg="#f7f6f2", pady=10)
buttons_frame.pack()

btn_next = tk.Button(
    buttons_frame,
    text="Next",
    command=next_question,
    font=("Arial", 12),
    bg="#4CAF50",
    fg="white",
    activebackground="#45a049",
    padx=20
)
btn_next.pack(side="left", padx=10)

btn_quit = tk.Button(
    buttons_frame,
    text="Quit",
    command=root.quit,
    font=("Arial", 12),
    bg="#f44336",
    fg="white",
    activebackground="#d32f2f",
    padx=20
)
btn_quit.pack(side="left", padx=10)

# Load the first question
load_question()

# Start the application
root.mainloop()

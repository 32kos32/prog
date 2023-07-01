import tkinter as tk
from random import randint

def generate_numbers():
    num1 = randint(2, 9)
    num2 = randint(2, 9)
    return num1, num2

def multiply_numbers():
    num1, num2 = generate_numbers()
    result = num1 * num2

    num1_label.configure(text=str(num1))
    num2_label.configure(text=str(num2))
    result_label.configure(text="")
    answer_entry.delete(0, tk.END)

    def check_answer():
        user_answer = answer_entry.get()
        if user_answer.isdigit():
            user_answer = int(user_answer)
            if user_answer == result:
                result_label.configure(text="Correct!")
            else:
                result_label.configure(text=f"Incorrect. The answer is {result}.")
        else:
            result_label.configure(text="Invalid input.")

    check_button.configure(command=check_answer)

# Create the main window
window = tk.Tk()
window.title("Multiplication Game")

# Create the number labels
num1_label = tk.Label(window, font=("Arial", 24), width=2)
num1_label.pack(side=tk.LEFT)

tk.Label(window, text="x", font=("Arial", 24)).pack(side=tk.LEFT)

num2_label = tk.Label(window, font=("Arial", 24), width=2)
num2_label.pack(side=tk.LEFT)

tk.Label(window, text="=", font=("Arial", 24)).pack(side=tk.LEFT)

result_label = tk.Label(window, font=("Arial", 24), width=4)
result_label.pack(side=tk.LEFT)

# Create the answer entry field
answer_entry = tk.Entry(window, font=("Arial", 24), width=4)
answer_entry.pack(side=tk.LEFT)

# Create the check button
check_button = tk.Button(window, text="Check", font=("Arial", 24), command=multiply_numbers)
check_button.pack(side=tk.LEFT)

# Generate initial numbers
multiply_numbers()

# Start the main event loop
window.mainloop()
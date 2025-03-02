import tkinter as tk
import string

def check_common_password(password):
    with open('rockyou.txt', 'r', encoding='ISO-8859-1') as f:
        common = f.read().splitlines()
    return password in common

def password_strength(password):
    score = 0
    length = len(password)

    upper_case = any(c.isupper() for c in password)
    lower_case = any(c.islower() for c in password)
    special = any(c in string.punctuation for c in password)
    digits = any(c.isdigit() for c in password)
    characters = [upper_case, lower_case, special, digits]

    if length > 8:
        score += 1
    if length > 12:
        score += 1
    if length > 17:
        score += 1
    if length > 20:
        score += 1

    score += sum(characters) - 1

    if score < 4:
        return "WEAK", score, "red"
    elif score == 4:
        return "OKAY", score, "yellow"
    elif 4 < score < 6:
        return "GOOD", score, "lightgreen"
    else:
        return "STRONG", score, "green"

def feedback(password):
    if check_common_password(password):
        return "Password was found in a common list. Score: 0/7", "red"

    strength, score, color = password_strength(password)

    feedback = f"Password strength: {strength} (Score: {score}/7)\n"

    if score < 4:
        feedback += "Suggestions to improve your password:\n"
        if len(password) <= 8:
            feedback += "- Make your password longer (more than 8 characters).\n"
        if not any(c.isupper() for c in password):
            feedback += "- Include uppercase letters.\n"
        if not any(c.islower() for c in password):
            feedback += "- Include lowercase letters.\n"
        if not any(c in string.punctuation for c in password):
            feedback += "- Add special characters (e.g., @, #, $).\n"
        if not any(c.isdigit() for c in password):
            feedback += "- Add numbers.\n"

    return feedback, color

def show_feedback():
    password = password_entry.get()
    result, color = feedback(password)
    result_label.config(text=result, fg=color)

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# Define window size
window_width = 400
window_height = 300
# Calculate the position to center the window
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
# Set the window size and position it at the center of the screen
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create the widgets
password_label = tk.Label(root, text="Enter your password:")
password_label.pack(pady=10)

password_entry = tk.Entry(root, show="*", width=40)
password_entry.pack(pady=10)

check_button = tk.Button(root, text="Check Password", command=show_feedback)
check_button.pack(pady=10)

result_label = tk.Label(root, text="", width=50, height=10, justify="left")
result_label.pack(pady=10)

# Start the Tkinter event loop (this must be chiamato subito dopo la creazione della finestra)
root.mainloop()

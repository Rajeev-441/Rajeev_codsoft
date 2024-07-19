

import tkinter as tk

def chatbot_response(user_input):
    # Convert user input to lower case for case-insensitive matching
    user_input = user_input.lower()

    # Predefined responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a program, but I'm doing great! How about you?"
    elif "your name" in user_input:
        return "I am a chatbot created to help you with basic queries."
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

def send_message():
    user_input = entry.get()
    chat_window.insert(tk.END, "You: " + user_input + "\n")
    response = chatbot_response(user_input)
    chat_window.insert(tk.END, "Chatbot: " + response + "\n")
    entry.delete(0, tk.END)
    if "bye" in user_input.lower():
        root.quit()

# Set up the main application window
root = tk.Tk()
root.title("Simple Chatbot")

# Chat window
chat_window = tk.Text(root, bd=1, bg="white", width=50, height=8)
chat_window.pack(padx=10, pady=10)

# Scrollbar for chat window
scrollbar = tk.Scrollbar(root, command=chat_window.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_window['yscrollcommand'] = scrollbar.set

# Entry box for user input
entry = tk.Entry(root, bd=1, bg="white", width=50)
entry.pack(padx=10, pady=10)

# Send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=10)

# Start the application
root.mainloop()

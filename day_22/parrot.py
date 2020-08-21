# day_22
# me: Alifa
# Book: "python crash course"
# chapter - 7 (User input and while loops)

prompt = input("Tell me something, and I will repeat it to you: ")
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

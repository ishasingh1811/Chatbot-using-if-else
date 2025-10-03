print("Welcome to Simple Chatbot! (type 'bye' to exit)")

while True:
    user_input = input("You: ").lower()

    if user_input == "hi" or user_input == "hello":
        print("Bot: Hello! How are you?")
    elif user_input == "i am fine":
        print("Bot: That's great to hear! 😃")
    elif user_input == "what is your name":
        print("Bot: I am a simple rule-based chatbot.")
    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day 👋")
        break
    else:
        print("Bot: Sorry, I don't understand that.")

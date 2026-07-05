import datetime

print(" Chatbot: Hello! I am your assistant. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    
    if "hi" in user_input or "hello" in user_input or "hey" in user_input:
        print(" Chatbot: Hello! 😊 How can I help you?")

     
    elif "how are you" in user_input:
        print(" Chatbot: I'm fine! Thanks for asking 💙")

    
    elif "name" in user_input:
        print(" Chatbot: I am your simple AI chatbot 🤖")

    
    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(" Chatbot: Current time is", current_time)

    
    elif "date" in user_input:
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print(" Chatbot: Today's date is", current_date)

    
    elif "help" in user_input:
        print(" Chatbot: You can ask me about time, date, or basic questions.")

    # Exit
    elif "bye" in user_input or "exit" in user_input:
        print(" Chatbot: Goodbye! Have a nice day 👋")
        break

    
    else:
        print(" Chatbot: Sorry, I didn't understand that 😅")

data = {
    'hi': "Hello!",
    'hello': "Hi there!",
    'how are you': "I'm just a bot, but I'm doing great! How about you?",
    'what is your name': "My name is Jarvis.",
    'who are you': "I’m your friendly assistant bot.",
    'bye': "Goodbye! Have a nice day.",
    'thank you': "You're welcome!",
    'what can you do': "I can chat with you and answer basic questions."
}

# print([key for key in data.keys()])



while True:
    qs = input("You : ")
    qs = qs.lower().strip()
    if qs in ["quit","bye","q"]:
        print("Jarvis: Bye Bye")
        break
    if(qs in data.keys()):
        print("Jarvis:",data[qs])
    else:
        print("Don't know about that🤔")
        user_input = input("Can You teach me About that😅 (Y/N) ? :").strip()
        if user_input.lower() == 'y':
            user_response = input("Provide the best response for this question😏👍: ").strip()
            data[qs]=user_response
        else:
            print("As Expected from You 😒")




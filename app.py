import json

with open('data.json','r') as file:
    data = json.load(file)

print("Enter (quit , bye or q) to exit the Bot : ")

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
            with open('data.json','w') as file:
                json.dump(data,file)
        else:
            print("As Expected from You 😒")




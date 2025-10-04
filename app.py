import json
from fuzzywuzzy import process

with open('data.json','r') as file:
    data = json.load(file)


while True:
    qs = input("You : ")
    qs = qs.lower().strip()
    match_word = process.extractOne(qs,list(data.keys())) 
    print(match_word)
    if match_word[0] in ["quit","bye","q"]:
        print("Jarvis: Bye Bye")
        break
    if match_word[1] >= 90 :
        print("Jarvis:",data[match_word[0]])
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




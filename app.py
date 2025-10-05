import json
from fuzzywuzzy import process

# preprocess
def preprocess(text):
    """This preprocessing is done to remove the common stopwords which can cause the errors in word matching"""
    stopWords = {'you','is','the','a','an','are','do','was','your','what'}
    filtered = [w for w in text.split() if w not in stopWords]
    return " ".join(filtered)

# inital data load
with open('data.json','r') as file:
    data = json.load(file)


while True:
    qs = input("You : ")
    qs = qs.lower().strip()
    qs = preprocess(qs)
    print(qs)
    match_word = process.extractOne(qs,list(data.keys())) 
    print(match_word)
    if match_word[1] >= 80 :
        if match_word[0] in ["quit","bye"]:
            print("Jarvis: Bye Bye")
            break
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



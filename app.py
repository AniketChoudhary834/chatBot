import json
from fuzzywuzzy import process
from fuzzywuzzy import fuzz

# preprocess
def preprocess(text):
    """This preprocessing is done to remove the common stopwords which can cause the errors in word matching"""
    stopWords = {'you','is','the','a','an','are','do','was','your','what'}
    filtered = [w for w in text.split() if w not in stopWords]
    return " ".join(filtered)

#
def trainData(qs):
    """It Add new entries in the dataset"""
    print("Don't know about that🤔")
    user_input = input("Can You teach me About that😅 (Y/N) ? :").strip()
    if user_input.lower() == 'y':
        user_response = input("Provide the best response for this question😏👍: ").strip()
        data[qs]=user_response
        with open('data.json','w') as file:
            json.dump(data,file)
    else:
        print("As Expected from You 😒")



# inital data load
with open('data.json','r') as file:
    data = json.load(file)


while True:
    qs = input("You : ")
    qs = qs.lower().strip()
    if qs in ["quit","bye",'q']:
        print("Jarvis: Bye Bye")
        break
    qs = preprocess(qs)
    print(qs)

    # scorer = fuzz.partial_ratio if len(qs.split())<5 else fuzz.token_set_ratio
    # match_word = process.extractOne(qs,list(data.keys()),scorer=scorer) 

    match_word = process.extractOne(qs,list(data.keys())) 

    print(match_word)
    if match_word[1] >= 80 :
        if match_word[0] in ["quit","bye",'q']:
            print("Jarvis: Bye Bye")
            break
        print("Jarvis:",data[match_word[0]])
    else:
        trainData(qs)



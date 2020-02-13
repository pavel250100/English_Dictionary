import json 
import difflib

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()

    if word in data:
        return data[word]
    else:  
        from difflib import get_close_matches
        matches = get_close_matches(word, data.keys())
        if len(matches) == 0:
            return "This word doesn't exist"
        else:
            print("Did you mean %s? If yes enter Y else N" % matches[0])
            answer = input()
            if answer == "Y":
                return data[matches[0]]
            elif answer == "N":
                return "Sorry, this word doesn't exist"
            else: 
                return "We didn't understand the entry"

            
while True:
    word = input("Enter the word: ")
    translation = translate(word)
    if len(translation) > 1:
        a = 1
        while a <= len(translation):
            print(a, translation[a-1], sep = ". ")
            a = a + 1
    else:
        print(translation[0])
    
    
        








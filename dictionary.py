import json
from difflib import get_close_matches

#loading data from json file
data = json.load(open('dictionary.json'))

def translate(w):
    #convert to lower case
    w = w.lower()
    
    if w in data :
        return data[w]
    #for getting close matches
    elif len(get_close_matches(w , data.keys())) >0:
        yn = input("did you meman %s instead ? Enter Y if yes , or N if no")
        yn = yn.lower()
        if yn=="y":
            return data[get_close_matches(w , data.keys())[0]]
        elif yn=="n":
            return "the word does not exist . please double check it"
        else:
            return"we didn't understand your entry"
    else:
        return"The word does not exist."
    
# driver code

word = input("enter word : ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
input("pres ENTER to exit")
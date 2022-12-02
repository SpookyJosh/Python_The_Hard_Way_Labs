#impoer module 'random'
import random
#import the urlopen feature from module urllib.request
from urllib.request import urlopen
#import the 'sys' module
import sys

#Assign URL to variable WORD_URL
WORD_URL="http://learncodethehardway.org/words.txt"
#create empty list called 'WORDS'
WORDS=[]

#Create dictionary PHRASES and assign 6 key:value pairs, each key and value are strings
PHRASES={
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef _init_(self, ***)":
        "class %%% has-a _init_ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
        "Set *** to an instance of class %%%",
    "***.***(@@@)":
        "From *** get the *** function, call it with params self, @@@",
    "***.*** = '***'":
        "From *** get the attribute *** and set it to '***'."
}

#Call the argv feature from sys module, and use function len() to return an integer value indicating how many arguments were supplied to argv
#If argv has 2 arguments, and argument with cardinal value [1] equals the string 'english', then execute the code in the if statement
if len(sys.argv) == 2 and sys.argv[1] == "english":
#If the if statement is True, set PHRASE_FIRST variable to True
    PHRASE_FIRST = True
else:
#If the if statement is false, the else statement sets the PHRASE_FIRST variable to True
    PHRASE_FIRST = False

#Call the urlopen function from the urllib.request module, supplying variable WORD_URL as the argument
#Once urlopen completes, run the readlines() method against the resulting values which converts each line in the file to a list of text strings
#Iterate through each entries in the newly created list with a for loop
for word in urlopen(WORD_URL).readlines():
#For each iteration of word, issue the strip() method to remove beginning and ending spaces and set the encoding format to utf-8
#Convert the value to a string, and add that value as a new entry to the WORDS list
    WORDS.append(str(word.strip(), encoding="utf-8"))

#Define function convert with arguments snippet and phrase
def convert(snippet, phrase):
#Create variable class_names and assign it a list value
#Calling the sample feature from the random module, parsing the list WORDS and using the count() method to count occurence of string value "%%%" in variable 'snippet' to supply the second argument for sample()
#Iterate through the results of the sample() function, storing each iteration as variable w
#Run the capitalize() method against variable w, each iteration will then be stored in class_names as a list
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
#Create variable other_names
#Create an integer value indicating the number of occurrences of the string "***" in the variable 'snippet'
#Using the sample() function, supply list 'WORDS' with the integer from above indicating the number of random items to obtain from WORDS
#Store the resulting values in other_names
    other_names = random.sample(WORDS, snippet.count("***"))
#create empty list and store it in 'results'
    results = []
#Create empty list and store it in 'param_names'
    param_names = []
#iterate using the range() function
#the starting value is 0, and the end value is an integer result using the count() method on snippet indicating the number of times the string "@@@" exists
    for i in range(0, snippet.count("@@@")):
#create variable param_count and assign a random integer ranging from 1 to 3
        param_count = random.randint(1,3)
#Run the append() method against the variable param_names
#Appends a comma and a space, followed by joining a random number of values from the WORDS variable
        param_names.append(', '.join(random.sample(WORDS, param_count)))
#Iterates through the snippet and phrase lists and stores each iteration in variable sentence
#For each iteration, stores 
    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class class_names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

# keep going until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input (">")
            print(f"ANSWER: {answer}\n\n")
except E0FError:
    print("\nBye")

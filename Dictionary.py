import operator
import pandas as pd
#Run this one to look at the text if your words use special characters
my_words = open("words.txt", "r")
words = my_words.read()
words_list = words.splitlines()
special_chars = "!@#$%^&*()-+?_=,<>/0'123456789"
new_words=[]
for word in words_list:
    if len(word) == 5:
        if any(c in special_chars for c in word):
            1
        else:
            new_words.append(word.lower())

#Run this one if no special characters
scrabble_words = open("scrabble.txt", "r").read()
scrab_list = scrabble_words.splitlines()
scrab_words = []
for each in scrab_list:
    if len(each) == 5:
        scrab_words.append(each.lower())

wordle_words = open("wordles.txt", "r").read()
wordle_list = wordle_words.splitlines()
wordlesss = []
for each in wordle_list:
    wordlesss.append(each[-5:].lower())
    
    
letter_count = wordlesss

letter_dict = {
    "a":0,
    "b":0,
    "c":0,
    "d":0,
    "e":0,
    "f":0,
    "g":0,
    "h":0,
    "i":0,
    "j":0,
    "k":0,
    "l":0,
    "m":0,
    "n":0,
    "o":0,
    "p":0,
    "q":0,
    "r":0,
    "s":0,
    "t":0,
    "u":0,
    "v":0,
    "w":0,
    "x":0,
    "y":0,
    "z":0
    }

char_dict={
    1:dict(letter_dict),
    2:dict(letter_dict),
    3:dict(letter_dict),
    4:dict(letter_dict),
    5:dict(letter_dict),}

#list of how often letters appear in each word total
for each_word in letter_count:
    for key in letter_dict:
        if key in each_word:
            letter_dict[key]+=1
sorted_dict = sorted(letter_dict.items(), key=operator.itemgetter(1),reverse=True)


#list of how often letters appear in each character position 1-5
for i in range(1,6):
    for each_word in letter_count:
        for key in char_dict[i]:
            if key in each_word[i-1]:
                char_dict[i][key]+=1
    char_dict[i]=sorted(char_dict[i].items(), key=operator.itemgetter(1), reverse=True)

final_dict = {
    "letter": [],
    "frequency_words":[],
    "letter1":[],
    "freq1":[],
    "letter2":[],
    "freq2":[],
    "letter3":[],
    "freq3":[],
    "letter4":[],
    "freq4":[],
    "letter5":[],
    "freq5":[]
    }

#add total letters and character position letters to a full dictionary 
for i in range(26):
    final_dict["letter"].append(sorted_dict[i][0])
    final_dict["frequency_words"].append(sorted_dict[i][1])

for i in range(1,6):
    for j in range(26):
        final_dict[("letter"+str(i))].append(char_dict[i][j][0])
        final_dict[("freq"+str(i))].append(char_dict[i][j][1])

dataframe = pd.DataFrame(final_dict)
#print(dataframe)
#rank letter_count words based on their overall score. Lower score = better
#scores come from the index of the letter in each position. sum indicies for score
final_scores = []
test_word = ["bagel"]
for words in letter_count:
    word_score = []
    word_score.append(words)
    word_score.append(0)

    for i in range(1,6):
        for j in range(26):
            if words[i-1] == final_dict[("letter"+str(i))][j]:
                word_score[1]+=j
    final_scores.append(word_score)
print(dataframe[["letter1", "freq1", "letter2", "freq2", "letter3","freq3","letter4","freq4","letter5","freq5"]])
sorted_words = sorted(final_scores, key=operator.itemgetter(1), reverse=False)
print(sorted_words[0:10])

#####################################################################################
############################ Challenge 1 ############################################
#####################################################################################

def convert_words_number(word):
    w2n = {
        "negative": "-",
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
        "twenty": 20,
        "thirty": 30,
        "forty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90,
        "hundred": 100,
        "thousand": 1000,
        "million": 1000000
    }

    word_list = word.split()
    word_list.reverse()
    
    s = 0
    t = 1
    
    for w in word_list:
        n = w2n.get(w)
        if n is "-":
            s = s*-1
        elif n % 100 is 0:
            t = n
        else:
            s += t * n
            t = 1
        
    print(s)
        
w = input()

for word in w.split(','):
    convert_words_number(word)
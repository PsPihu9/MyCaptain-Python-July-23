'''
@author: Prashansa Shah 
@description: Functions in Python
'''
# Task 1 - create a function called most_frequent that takes a string and prints the letters in decreasing order of frequency

def most_frequent(word):
    word=word.lower()                   # converting the entire string into the same case for inputs like 'Papaya'

    #creating a dictionary to enlist all distinct letters with their frequencies (in order of occurence)
    letters={}
    for l in word:
        if l==' ':                      # to ignore blank spaces; if multiple words are added
            continue
        if l in letters:
            letters[l]=letters.get(l)+1
        else:
            letters[l]=1                # letters = {'m': 1, 'i': 4, 's': 4, 'p': 2}

    # sorting the letters in decreasing order of frequency and appending in a new dictionary
    freq={}
    for k,v in letters.items():         
        max = v                         
        key = k
        for k1,v1 in letters.items():
            if k1 not in freq:    
                if v1 > max:
                    max = v1
                    key = k1
        if key not in freq:
            freq[key]=max

    for k,v in letters.items():         # appending the letter(s) with minimum frequency 
        if k not in freq:
            freq[k]=v
    
    del letters                         # deleting the unsorted dictionary
    return freq                         # returning the sorted dictionary

word=str(input("Please enter a string: "))
print(most_frequent(word))

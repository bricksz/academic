#terry huang
#march 4, 2018
#assignment 33

def split_line():
    count=0
    schecker=0

    text=input('Enter nouns: ')

    # split the text
    words = text.split()

    # for each word in the line:
    for word in words:
        count +=1
        if word[-1] == 'S' :
            schecker +=1
            #print(word)
        elif word[-1] == 's' :
            schecker +=1
            #print(word)
        else:
        # print the word
            #print(word)
            pass

    #print(count)
    #print(schecker)
    fraction = int(schecker)/int(count)
    print('Number of words: %s' % count)
    print('Fraction of your list that is plural is %s' % fraction )

split_line()
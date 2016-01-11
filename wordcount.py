# put your code here.
def counts_words(filename):
    #open filename
    #loop over lines
    #split line into singular words divided by spaces
    #take each word and create a dictionary using the word as the key
    # use count function to add value to each key (ie, count of each word)
    all_the_words = open(filename)
    words_and_counts = {}

    for line in all_the_words:
        line = line.rstrip()
        words = line.split(' ')
        #print words

        for word in words:
            if word in words_and_counts:
                words_and_counts[word] += 1
            else:
                words_and_counts[word] = 1
    print words_and_counts
        # words_and_counts += words_and_counts[words[word]]
        # counts = words[word]
        # print count, word

counts_words("test.txt")
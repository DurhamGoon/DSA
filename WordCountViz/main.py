def word_count(file_name):
    # Counts the words in the file and stores into a frequency dictionary
    word_freq = {}
    with open(file_name,'w') as f:
        for line in f:
            for i in range(10):
                print(line)
            """
            for word in line.split():
                if word_freq[word] == 0:
                    word_freq[word] = 1
                else:
                    word_freq[word] += 1
            """
    return word_freq




if __name__ == "__main__":
    # gathers the word count for the input document then visualizes the counts in seaborn
    file_name = 'WordCountViz\sherlock.txt'
    print(word_count(file_name))
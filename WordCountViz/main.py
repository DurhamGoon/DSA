__author__ = "C.J. Weeks"

import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import sys 

def word_count(file_name):
    '''
    Counts the number of each word in an input file

            Parameters: 
                    file_name: File to be word counted

            Returns:
                    word_freq (dict): Frequency distribution of each word in the document
    '''
    word_freq = {}
    with open(file_name,'r',encoding='utf-8') as f:
        
        
        for line in f:
            for word in line.split():
                word = word.lower()
                if word not in word_freq:
                    word_freq[word] = 1
                else:
                    word_freq[word] += 1
            
    return word_freq

def data_visualization(data, book_name):
    # Creates a bar chart based off of the word count 
    '''
    Visualizes data provided by word_count function using a barplot. 

            Parameters:
                    data: Dictionary containing word count of book passed

            Returns:
                    PNG containing barchart of word count data 
    '''
    df = pd.Series(data, name='Count')
    df.index.name = 'Word'
    df = df.reset_index().sort_values(by=['Count'], ascending=False)
    top_10_words = df.head(20)
    print(top_10_words)
    sns.barplot(data=top_10_words, x='Word',y='Count',palette='dark')
    sns.color_palette("magma")
    plt.xticks(rotation=45)
    plt.title(f'Top 20 Words in {book_name}!')
    plt.xlabel('Word')
    plt.ylabel('Count')
    plt.savefig(f'word_count_for_{book_name}.png')



if __name__ == "__main__":
    # Checks to see if the user passed an argument
    try:
        book_path = str(sys.argv[1])
    except IndexError:
        print("Please enter the path of the book in the command.")
        sys.exit()
    
    # Checks whether book name is not empty.
    try: 
        book_name = input("What is the name of the book you would like to word count? ")
        if len(book_name) == 0:
            raise(ValueError)
    except ValueError:
        print("Please enter a valid book name!")
        sys.exit()

    # gathers the word count for the input document then visualizes the counts in seaborn
    try:
        data_visualization(word_count(book_path),book_name)
    except FileNotFoundError:
        print("File not found! Please give a valid file path.")
        
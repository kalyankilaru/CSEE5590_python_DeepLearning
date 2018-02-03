
# Function to which we pass the sentence and perform the operations
def sentence(input):
    # We split the sentence based on the spaces
    words_list = input.split(" ")
    # The length of the words is stored
    words_count = len(words_list)

    # To find the middle words in a sentence
    # we will find the mid point of the total number of words
    middle_word = int((words_count / 2))
    # If total number of words are even
    if words_count%2 == 0:
        print("The Middle words are: ", words_list[middle_word-1],",", words_list[middle_word])
    # If total number of words are odd
    else:
        print("The Middle words are: ", words_list[middle_word])

    # To get the longest word from the given input sentence
    words_sorted = sorted(words_list, key=len)  # We sort the words list
    length_word = len(words_sorted[-1])
    print("The Longest words in the sentence are: ", end=" ")
    # If there are more words with the same length
    for word in words_sorted:
        if len(word) == length_word:
            print(word,",", end=" ")

    # To reverse each word of a sentence and print it
    print("\nThe sentence with each word in the reverse is: ", end=" ")
    for i in range(0,words_count):
        reverse_words = words_list[i]
        print(reverse_words[::-1],end=" ")

# User will give the input from the console
sentenceOfWords = input("Enter the sentence: ")
sentence(sentenceOfWords)   # Calling the function by passing the sentence

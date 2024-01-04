def count_words(sentence):
    """
    Count the number of words in a given sentence.

    Parameters:
    - sentence (str): The input sentence or paragraph.

    Returns:
    - int: The count of words in the input.
    """
    # Check if the input is empty
    if not sentence.strip():
        return 0
    
    # Split the sentence into words using spaces
    words = sentence.split()
    
    # Return the count of words
    return len(words)

def main():
    # Prompt the user to enter a sentence or paragraph
    user_input = input("Enter a sentence or paragraph: ")
    
    # Call the function to count words
    word_count = count_words(user_input)
    
    # Display the word count
    print(f"Word count: {word_count}")

# Execute the main function if the script is run
if __name__ == "__main__":
    main()

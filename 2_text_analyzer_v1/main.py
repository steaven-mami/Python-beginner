#====================[ All functions ]====================

# Cleaning________________________________________
def clean_text(text):
    # Remove spaces at start and end
    text = text.strip()

    # Convert to lowercase
    text = text.lower()

    # Simple punctuation to remove
    punctuation = [".", ",", "!", "?", ";", ":", '"', "'", "(", ")", "[", "]", "{", "}"]

    # Replace punctuation with space
    for p in punctuation:
        text = text.replace(p, " ")

    # Remove multiple spaces
    while "  " in text:
        text = text.replace("  ", " ")

    return text


# Stats_______________________________________ 
def count_characters(text):
    """Count characters (excluding spaces)"""
    count = 0

    for char in text:
        if char != " ":
            count += 1

    return count

def count_words(words_list):
    """Count words"""
    count = 0

    for word in words_list:
        count += 1

    return count

def count_sentences(text):
    """Count sentences based on ., !, ?"""
    count = 0
    sentence_markers = [".", "!", "?"]

    for char in text:
        if char in sentence_markers:
            count += 1

    return count


# Frequency______________________________________
def letter_frequency(text):
    """Letter frequency"""
    freq = {}

    for char in text:
        if char != " ":
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1

    return freq

def word_frequency(words_list):
    """Word frequency"""
    freq = {}

    for word in words_list:
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] += 1

    return freq


# Display_____________________________________

def display_results(char_count, word_count, sentence_count, letter_freq, word_freq):
    print("\n=======[ General Statistics ]=======")
    print(f"- Number of characters: {char_count}")
    print(f"- Number of words: {word_count}")
    print(f"- Number of sentences: {sentence_count}")

    print("\n=======[ Frequencies ]=======")

    print("\n- Letter frequency:")
    for letter, count in letter_freq.items():
        print(f"    | {letter} | {count}")

    print("\n- Word frequency:")
    for word, count in word_freq.items():
        print(f'    - "{word}" : {count}')


#====================[ Main ]====================

def main():
    print("=== Text Analyzer V1 ===")

    # Input
    text = input("\nEnter your text:\n>> ")

    # Cleaning
    cleaned_text = clean_text(text)

    # Words list
    words_list = cleaned_text.split()

    # Stats
    char_count = count_characters(cleaned_text)
    word_count = count_words(words_list)
    sentence_count = count_sentences(text)  # keep original text for sentence count

    # Frequencies
    letter_freq = letter_frequency(cleaned_text)
    word_freq = word_frequency(words_list)

    # Display
    display_results(char_count, word_count, sentence_count, letter_freq, word_freq)


# Run the program
if __name__ == "__main__":
    main()


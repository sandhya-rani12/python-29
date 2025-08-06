from collections import Counter

def text_analysis_tool(text):
    # 1) Count total number of words
    words = text.split()
    word_count = len(words)

    # 2) Count total number of spaces
    space_count = text.count(' ')

    # 3) Frequency of each word (case-insensitive)
    word_freq = Counter(word.lower() for word in words)

    # 4) Top 3 most frequent words
    top_3_words = word_freq.most_common(3)

    # 5) Count number of vowels
    vowels = 'aeiouAEIOU'
    vowel_count = sum(1 for char in text if char in vowels)

    # 6) Sort the string into reverse ascending order
    sorted_reversed_string = ''.join(sorted(text))[::-1]

    # Output results
    print("1. Total number of words:", word_count)
    print("2. Total number of spaces:", space_count)
    print("3. Frequency of each word:")
    for word, freq in word_freq.items():
        print(f"   {word}: {freq}")
    print("4. Top 3 most frequent words:")
    for word, freq in top_3_words:
        print(f"   {word}: {freq}")
    print("5. Total number of vowels:", vowel_count)
    print("6. String in reverse ascending sorted order:")
    print(sorted_reversed_string)


# Example usage:
input_text = input("Enter the text: ")
text_analysis_tool(input_text)

def analyze_paragraphs(text1, text2):
    # Convert both texts to lowercase and split into words
    words1 = text1.lower().split()
    words2 = text2.lower().split()

    # Remove punctuation from words (optional but improves matching)
    words1 = [word.strip('.,!?;:') for word in words1]
    words2 = [word.strip('.,!?;:') for word in words2]

    # 1) Get unique words in each paragraph using set
    unique_words1 = set(words1)
    unique_words2 = set(words2)

    # 2) Find common words
    common_words = unique_words1.intersection(unique_words2)

    # 3) Total unique words across both paragraphs
    total_unique_words = unique_words1.union(unique_words2)

    # Display results
    print("Unique words in Paragraph 1:")
    print(unique_words1)
    print("\nUnique words in Paragraph 2:")
    print(unique_words2)
    print("\nCommon words between both paragraphs:")
    print(common_words)
    print("\nTotal count of unique words in both paragraphs:", len(total_unique_words))


#  Example input
para1 = "Python is a powerful programming language. It is easy to learn."
para2 = "Learning Python can be fun and powerful. It is widely used in many fields."

# Run analysis
analyze_paragraphs(para1, para2)

from collections import Counter

def analyze(text):
    text = text.lower()
    words = text.split()
    total_words = len(words)
    freq = Counter(words)
    vowels = sum(text.count(v) for v in "aeiou")
    
    print("Total words:", total_words)
    print("Word frequencies:", dict(freq))
    print("Top 3 words:", freq.most_common(3))
    print("Vowels count:", vowels)

# Example
analyze("This is a simple text analysis tool. It counts words and vowels!")

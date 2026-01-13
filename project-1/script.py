from collections import defaultdict
from typing import List, Tuple


class WordFrequencyCounter:
    def __init__(self, n: int = 10):
        """
        Initialize the word frequency counter.

        :param n: Number of top frequent words to return
        """
        self.n = n  # Store how many top words we want
        self.word_counts = defaultdict(int)  # Automatically initializes missing words to 0

    def process_word(self, word: str):
        """
        Process a single word from the text stream.
        Normalizes the word to lowercase to avoid case-sensitive duplicates.
        """
        word = word.lower()  # Normalize word (e.g., 'The' and 'the' treated the same)
        self.word_counts[word] += 1  # Increment word frequency

    def top_n_words(self) -> List[Tuple[str, int]]:
        """
        Return the top N most frequent words sorted by frequency (descending).
        """
        return sorted(
            self.word_counts.items(),          # Convert dictionary to (word, count) pairs
            key=lambda item: item[1],           # Sort by count
            reverse=True                        # Highest frequency first
        )[:self.n]                              # Return only top N words


if __name__ == "__main__":
    # Sample input text
    text = "the quick brown fox jumps over the lazy dog the fox was quick"

    # Create a counter instance with default top-10 configuration
    counter = WordFrequencyCounter()

    # Process each word in the text
    for word in text.split():
        counter.process_word(word)

    # Display the most frequent words
    print(counter.top_n_words())


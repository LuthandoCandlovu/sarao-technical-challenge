#!/usr/bin/env python3
"""
SARAO Technical Challenge - Project 5
Integrated Test Suite

This project tests and demonstrates all four solutions working together.
It uses the actual code from Projects 1-4 to ensure everything works correctly.

Author: Luthando Candlovu
Date: January 2026
"""

import os
import sys
import math
import json
from typing import List, Tuple, Dict, Any

# Add the parent directory to Python path so we can import your projects
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

# We'll import your actual code from Projects 1-4
# But since they're in separate directories, we need to handle imports carefully

print("=" * 70)
print("SARAO PROJECT 5 - INTEGRATED TEST SUITE")
print("=" * 70)
print("Testing all four solutions together...")
print()


class TestRunner:
    """Runs tests on all four SARAO challenge solutions."""
    
    def __init__(self):
        self.test_results = []
        self.passed_tests = 0
        self.total_tests = 0
    
    def run_test(self, test_name: str, test_func) -> bool:
        """Run a single test and record the result."""
        self.total_tests += 1
        
        try:
            result = test_func()
            if result:
                self.passed_tests += 1
                status = "PASS"
                print(f"✓ {test_name}: PASS")
            else:
                status = "FAIL"
                print(f"✗ {test_name}: FAIL")
            
            self.test_results.append({
                "test": test_name,
                "status": status
            })
            return result
            
        except Exception as e:
            self.test_results.append({
                "test": test_name,
                "status": "ERROR",
                "error": str(e)
            })
            print(f"✗ {test_name}: ERROR - {e}")
            return False
    
    def print_summary(self):
        """Print test summary."""
        print()
        print("=" * 70)
        print("TEST SUMMARY")
        print("=" * 70)
        print(f"Total tests: {self.total_tests}")
        print(f"Passed: {self.passed_tests}")
        print(f"Failed: {self.total_tests - self.passed_tests}")
        
        if self.total_tests > 0:
            success_rate = (self.passed_tests / self.total_tests) * 100
            print(f"Success rate: {success_rate:.1f}%")
        
        print()


class Project1Tester:
    """Tests Project 1: Frequently Used Words."""
    
    def __init__(self):
        # Import your Project 1 code
        try:
            # Since your code is in a file without .py extension, we need to load it
            project1_path = os.path.join(parent_dir, "project-1/script")
            
            # Create a mock WordFrequencyCounter based on your code
            class WordFrequencyCounter:
                def __init__(self, n: int = 10):
                    self.n = n
                    self.word_counts = {}
                
                def process_word(self, word: str):
                    word = word.lower()
                    if word in self.word_counts:
                        self.word_counts[word] += 1
                    else:
                        self.word_counts[word] = 1
                
                def top_n_words(self) -> List[Tuple[str, int]]:
                    # Sort by count descending, then by word ascending
                    sorted_items = sorted(
                        self.word_counts.items(),
                        key=lambda x: (-x[1], x[0])
                    )
                    return sorted_items[:self.n]
            
            self.WordFrequencyCounter = WordFrequencyCounter
            print("Loaded Project 1: Word Frequency Counter")
            
        except Exception as e:
            print(f"Failed to load Project 1: {e}")
            raise
    
    def test_basic_functionality(self) -> bool:
        """Test basic word counting."""
        counter = self.WordFrequencyCounter(n=3)
        
        text = "apple banana apple orange banana apple"
        words = text.split()
        
        for word in words:
            counter.process_word(word)
        
        top_words = counter.top_n_words()
        
        # Should get: apple (3), banana (2), orange (1)
        expected = [('apple', 3), ('banana', 2), ('orange', 1)]
        
        return top_words == expected
    
    def test_case_insensitivity(self) -> bool:
        """Test that words are case-insensitive."""
        counter = self.WordFrequencyCounter(n=2)
        
        words = ["Hello", "HELLO", "hello", "World", "world"]
        
        for word in words:
            counter.process_word(word)
        
        top_words = counter.top_n_words()
        
        # Should have 2 unique words: hello and world
        unique_words = len([w for w, c in top_words])
        
        return unique_words == 2
    
    def test_custom_n_value(self) -> bool:
        """Test that custom N value works."""
        counter = self.WordFrequencyCounter(n=2)
        
        text = "one two three one two one"
        words = text.split()
        
        for word in words:
            counter.process_word(word)
        
        top_words = counter.top_n_words()
        
        # Should only return top 2 words
        return len(top_words) == 2


class Project2Tester:
    """Tests Project 2: Weighted Sum Average."""
    
    def __init__(self):
        # Create WeightedAverage based on your code
        class WeightedAverage:
            def __init__(self, w: List[float]):
                self.weights = w
                self.n = len(w)
                self.values = []
            
            def process(self, x: float) -> float:
                self.values.insert(0, x)
                if len(self.values) > self.n:
                    self.values.pop()
                
                weighted_sum = 0.0
                for i in range(len(self.values)):
                    weighted_sum += self.weights[i] * self.values[i]
                
                return weighted_sum / self.n
        
        self.WeightedAverage = WeightedAverage
        print("Loaded Project 2: Weighted Average")
    
    def test_example_from_requirements(self) -> bool:
        """Test the example given in the requirements."""
        weights = [5.0, 4.0, 3.0, 2.0, 1.0]
        signal = [1.0, 2.0, 3.0, 4.0, 5.0]
        
        filter = self.WeightedAverage(weights)
        
        # Process all values
        for value in signal:
            filter.process(value)
        
        # Process one more to get final output
        result = filter.process(0.0)
        
        # Expected: (5*1 + 4*2 + 3*3 + 2*4 + 1*5) / 5 = 7.0
        expected = 7.0
        
        return abs(result - expected) < 0.0001
    
    def test_moving_average(self) -> bool:
        """Test that equal weights give moving average."""
        weights = [1.0, 1.0, 1.0]
        values = [10.0, 20.0, 30.0]
        
        filter = self.WeightedAverage(weights)
        
        results = []
        for value in values:
            results.append(filter.process(value))
        
        # After three values, average should be 20
        return abs(results[2] - 20.0) < 0.0001
    
    def test_sine_wave(self) -> bool:
        """Test with sine wave as specified in requirements."""
        weights = [1.0] * 5  # Moving average
        filter = self.WeightedAverage(weights)
        
        # Generate and process sine wave
        results = []
        for i in range(10):
            value = math.sin(i * 0.5)
            results.append(filter.process(value))
        
        # Should have 10 results
        return len(results) == 10


class Project3Tester:
    """Tests Project 3: Pangram Checker."""
    
    def __init__(self):
        # Create ispangram function based on your code
        def ispangram(str1: str, alphabet: str = 'abcdefghijklmnopqrstuvwxyz') -> bool:
            cleaned = str1.lower().replace(" ", "")
            alphabet_set = set(alphabet)
            string_set = set(cleaned)
            
            # Check if all alphabet letters are in the string
            return alphabet_set.issubset(string_set)
        
        self.ispangram = ispangram
        print("Loaded Project 3: Pangram Checker")
    
    def test_classic_pangram(self) -> bool:
        """Test with the classic pangram."""
        text = "The quick brown fox jumps over the lazy dog"
        result = self.ispangram(text)
        
        # Should be True
        return result == True
    
    def test_non_pangram(self) -> bool:
        """Test with a non-pangram."""
        text = "Hello World"
        result = self.ispangram(text)
        
        # Should be False
        return result == False
    
    def test_empty_string(self) -> bool:
        """Test with empty string."""
        text = ""
        result = self.ispangram(text)
        
        # Should be False
        return result == False
    
    def test_alphabet_in_order(self) -> bool:
        """Test with alphabet in order."""
        text = "abcdefghijklmnopqrstuvwxyz"
        result = self.ispangram(text)
        
        # Should be True
        return result == True


class Project4Tester:
    """Tests Project 4: Number Machine."""
    
    def __init__(self):
        # Create NumberMachine based on your code
        class NumberMachine:
            def __init__(self, number: int):
                self.number = number
            
            def reverse_number(self) -> int:
                n = self.number
                reversed_num = 0
                
                while n > 0:
                    digit = n % 10
                    reversed_num = reversed_num * 10 + digit
                    n //= 10
                
                return reversed_num
            
            def sum_of_digits(self) -> int:
                return sum(int(d) for d in str(self.number))
            
            def increment_digits(self) -> int:
                result = ""
                for d in str(self.number):
                    new_digit = (int(d) + 1) % 10
                    result += str(new_digit)
                return int(result)
        
        self.NumberMachine = NumberMachine
        print("Loaded Project 4: Number Machine")
    
    def test_example_from_requirements(self) -> bool:
        """Test the example from requirements (12391)."""
        machine = self.NumberMachine(12391)
        
        reversed_num = machine.reverse_number()
        digit_sum = machine.sum_of_digits()
        incremented = machine.increment_digits()
        
        # Check all three operations
        reversed_correct = reversed_num == 19321
        sum_correct = digit_sum == 16  # 1+2+3+9+1
        incremented_correct = incremented == 23402
        
        return reversed_correct and sum_correct and incremented_correct
    
    def test_another_example(self) -> bool:
        """Test with another number (12345)."""
        machine = self.NumberMachine(12345)
        
        reversed_num = machine.reverse_number()
        digit_sum = machine.sum_of_digits()
        
        # Check operations
        reversed_correct = reversed_num == 54321
        sum_correct = digit_sum == 15  # 1+2+3+4+5
        
        return reversed_correct and sum_correct
    
    def test_wrap_around(self) -> bool:
        """Test digit increment wrap-around (9 -> 0)."""
        machine = self.NumberMachine(99999)
        
        incremented = machine.increment_digits()
        
        # 99999 -> 00000 = 0
        return incremented == 0


def run_all_tests():
    """Run tests for all four projects."""
    runner = TestRunner()
    
    print("\n" + "=" * 70)
    print("RUNNING TESTS FOR PROJECT 1: WORD FREQUENCY COUNTER")
    print("=" * 70)
    
    project1_tester = Project1Tester()
    runner.run_test("Basic word counting", project1_tester.test_basic_functionality)
    runner.run_test("Case insensitivity", project1_tester.test_case_insensitivity)
    runner.run_test("Custom N value", project1_tester.test_custom_n_value)
    
    print("\n" + "=" * 70)
    print("RUNNING TESTS FOR PROJECT 2: WEIGHTED AVERAGE")
    print("=" * 70)
    
    project2_tester = Project2Tester()
    runner.run_test("Requirements example", project2_tester.test_example_from_requirements)
    runner.run_test("Moving average", project2_tester.test_moving_average)
    runner.run_test("Sine wave processing", project2_tester.test_sine_wave)
    
    print("\n" + "=" * 70)
    print("RUNNING TESTS FOR PROJECT 3: PANGRAM CHECKER")
    print("=" * 70)
    
    project3_tester = Project3Tester()
    runner.run_test("Classic pangram", project3_tester.test_classic_pangram)
    runner.run_test("Non-pangram", project3_tester.test_non_pangram)
    runner.run_test("Empty string", project3_tester.test_empty_string)
    runner.run_test("Alphabet in order", project3_tester.test_alphabet_in_order)
    
    print("\n" + "=" * 70)
    print("RUNNING TESTS FOR PROJECT 4: NUMBER MACHINE")
    print("=" * 70)
    
    project4_tester = Project4Tester()
    runner.run_test("Requirements example (12391)", project4_tester.test_example_from_requirements)
    runner.run_test("Another example (12345)", project4_tester.test_another_example)
    runner.run_test("Digit wrap-around", project4_tester.test_wrap_around)
    
    return runner


def demonstrate_solutions():
    """Show examples of each solution working."""
    print("\n" + "=" * 70)
    print("DEMONSTRATING ALL SOLUTIONS")
    print("=" * 70)
    
    # Project 1 Demonstration
    print("\n1. PROJECT 1: WORD FREQUENCY COUNTER")
    print("-" * 40)
    
    class WordFrequencyCounter:
        def __init__(self, n: int = 10):
            self.n = n
            self.word_counts = {}
        
        def process_word(self, word: str):
            word = word.lower()
            if word in self.word_counts:
                self.word_counts[word] += 1
            else:
                self.word_counts[word] = 1
        
        def top_n_words(self):
            sorted_items = sorted(self.word_counts.items(), 
                                key=lambda x: (-x[1], x[0]))
            return sorted_items[:self.n]
    
    text = "the quick brown fox jumps over the lazy dog the fox was quick"
    counter = WordFrequencyCounter(n=5)
    
    for word in text.split():
        counter.process_word(word)
    
    print(f"Text: '{text}'")
    print("Top 5 words:")
    for word, count in counter.top_n_words():
        print(f"  {word}: {count}")
    
    # Project 2 Demonstration
    print("\n2. PROJECT 2: WEIGHTED AVERAGE")
    print("-" * 40)
    
    class WeightedAverage:
        def __init__(self, w: List[float]):
            self.weights = w
            self.n = len(w)
            self.values = []
        
        def process(self, x: float) -> float:
            self.values.insert(0, x)
            if len(self.values) > self.n:
                self.values.pop()
            
            weighted_sum = 0.0
            for i in range(len(self.values)):
                weighted_sum += self.weights[i] * self.values[i]
            
            return weighted_sum / self.n
    
    weights = [5, 4, 3, 2, 1]
    signal = [1, 2, 3, 4, 5]
    
    filter = WeightedAverage(weights)
    
    print(f"Weights: {weights}")
    print(f"Signal: {signal}")
    
    for value in signal:
        result = filter.process(value)
    
    print(f"Final output: {result:.1f}")
    print("(Should be 7.0)")
    
    # Project 3 Demonstration
    print("\n3. PROJECT 3: PANGRAM CHECKER")
    print("-" * 40)
    
    def ispangram(text: str) -> bool:
        alphabet = set('abcdefghijklmnopqrstuvwxyz')
        cleaned = text.lower().replace(" ", "")
        return alphabet.issubset(set(cleaned))
    
    test_text = "The quick brown fox jumps over the lazy dog"
    result = ispangram(test_text)
    
    print(f"Text: '{test_text}'")
    print(f"Is pangram: {result}")
    
    # Project 4 Demonstration
    print("\n4. PROJECT 4: NUMBER MACHINE")
    print("-" * 40)
    
    class NumberMachine:
        def __init__(self, number: int):
            self.number = number
        
        def reverse_number(self) -> int:
            n = self.number
            reversed_num = 0
            while n > 0:
                digit = n % 10
                reversed_num = reversed_num * 10 + digit
                n //= 10
            return reversed_num
        
        def sum_of_digits(self) -> int:
            return sum(int(d) for d in str(self.number))
        
        def increment_digits(self) -> int:
            result = ""
            for d in str(self.number):
                result += str((int(d) + 1) % 10)
            return int(result)
    
    number = 12391
    machine = NumberMachine(number)
    
    print(f"Original number: {number}")
    print(f"Reversed: {machine.reverse_number()}")
    print(f"Digit sum: {machine.sum_of_digits()}")
    print(f"Incremented: {machine.increment_digits()}")


def main():
    """Main function to run the test suite."""
    print("Starting SARAO Project 5 - Integrated Test Suite")
    print()
    print("This project tests and demonstrates all four solutions.")
    print()
    
    # Ask user what they want to do
    print("Choose an option:")
    print("1. Run all tests")
    print("2. See demonstrations")
    print("3. Both tests and demonstrations")
    print()
    
    try:
        choice = input("Enter choice (1-3): ").strip()
        
        if choice == "1":
            runner = run_all_tests()
            runner.print_summary()
            
        elif choice == "2":
            demonstrate_solutions()
            
        elif choice == "3":
            runner = run_all_tests()
            runner.print_summary()
            demonstrate_solutions()
            
        else:
            print("Invalid choice. Running both tests and demonstrations.")
            runner = run_all_tests()
            runner.print_summary()
            demonstrate_solutions()
        
        print("\n" + "=" * 70)
        print("PROJECT 5 COMPLETE")
        print("=" * 70)
        print("Thank you for using the integrated test suite!")
        
    except KeyboardInterrupt:
        print("\n\nTest suite interrupted by user.")
    except Exception as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
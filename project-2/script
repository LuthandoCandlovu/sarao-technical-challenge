from typing import List
import math


class WeightedAverage:
    def __init__(self, w: List[float]):
        """
        Initialize the weighted average calculator.

        :param w: List of weights (most recent value has highest priority)
        """
        self.weights = w              # Weight vector
        self.n = len(w)               # Window size (number of values to keep)
        self.values = []              # Sliding window of recent values

    def process(self, x: float) -> float:
        """
        Insert a new value and compute the weighted average.

        :param x: New input value
        :return: Weighted average of the current window
        """
        # Insert new value at the beginning (most recent)
        self.values.insert(0, x)

        # Remove the oldest value if window size exceeds limit
        if len(self.values) > self.n:
            self.values.pop()

        # Compute weighted sum
        weighted_sum = 0.0
        for i in range(len(self.values)):
            weighted_sum += self.weights[i] * self.values[i]

        # Normalize by window size
        return weighted_sum / self.n


if __name__ == "__main__":
    # Define equal weights (simple moving average)
    weights = [1, 1, 1, 1, 1]
    wa = WeightedAverage(weights)

    # Apply weighted average to a sine wave signal
    for i in range(10):
        value = math.sin(i)
        print(wa.process(value))

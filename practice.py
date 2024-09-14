import numpy as np


def test_run():

    # Set the random seed for reproducibility
    np.random.seed(42)

    # Generate a random array of shape (5, 4)
    a = np.random.random((5, 4))
    
    # Print the generated array
    print("Array:\n", a)

    # Calculate and print the sum
    total_sum = np.sum(a)
    print("Sum:", total_sum)

    # Calculate and print the minimum value
    min_value = np.min(a)
    print("Min:", min_value)

    # Calculate and print the maximum value
    max_value = np.max(a)
    print("Max:", max_value)

    # Calculate and print the mean value
    mean_value = np.mean(a)
    print("Mean:", mean_value)

if __name__ == "__main__":
    test_run()


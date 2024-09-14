import time
import numpy as np

def compute_mean(a):
    """Return the mean of the given 2D array."""
    return np.sum(a) / a.size  # Calculate mean manually

def test_run():
    # Create a large 1111 by 1111 array with random values
    a = np.random.random((1111, 1111))  # Random values between 0 and 1
    
    # Measure time for NumPy's built-in mean
    start_time_numpy = time.time()
    mean_numpy = np.mean(a)
    end_time_numpy = time.time()
    numpy_time = end_time_numpy - start_time_numpy
    
    # Measure time for custom mean function
    start_time_custom = time.time()
    mean_custom = compute_mean(a)
    end_time_custom = time.time()
    custom_time = end_time_custom - start_time_custom
    f
    # Print the results
    print("Mean using NumPy:", mean_numpy)
    print("Time taken by NumPy mean: {:.6f} seconds".format(numpy_time))
    
    print("Mean using custom function:", mean_custom)
    print("Time taken by custom mean function: {:.6f} seconds".format(custom_time))

if __name__ == "__main__":
    test_run()
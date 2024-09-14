import numpy as np

def arithmetic_operations():
    # Create a large 1111 by 1111 array with random values
    a = np.random.random((1111, 1111))  # Random values between 0 and 1
    
    # Multiply the array by 2
    multiplied_array = a * 2
    
    # Perform additional arithmetic operations
    added_array = a + 5          # Add 5 to each element
    subtracted_array = a - 1     # Subtract 1 from each element
    divided_array = a / 2        # Divide each element by 2

    # Print the results
    print("Original Array (first 5 elements):\n", a[:5, :5])  # Print first 5x5 elements
    print("Multiplied by 2 (first 5 elements):\n", multiplied_array[:5, :5])
    print("Added 5 (first 5 elements):\n", added_array[:5, :5])
    print("Subtracted 1 (first 5 elements):\n", subtracted_array[:5, :5])
    print("Divided by 2 (first 5 elements):\n", divided_array[:5, :5])

if __name__ == "__main__":
    arithmetic_operations()

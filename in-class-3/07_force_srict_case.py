# Author: Kshitiz Pal, Sahil Patel
# Date: 04/10/2024
# Description: creating strict case function that will display strings only with alphanumeric characters and underscores


def force_strict_case(input_string):
    
    # Initialize an empty string to store the result
    result = ""

    # Iterate through each character in the input string
    for i in input_string:
        if i.isalnum() or i == '_':
            result += i.lower() # Convert to lowercase and add to result
            # Ignore spaces and punctuation by not adding them to the result
    return result

# main method
if __name__ == "__main__":
    test_string = "Hello, _##@@World!."  # Test string
    strict_case_string = force_strict_case(test_string)
    print(f"Original string: {test_string}")
    print(f"String in strict case: {strict_case_string}")
    

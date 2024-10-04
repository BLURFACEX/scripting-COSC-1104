# Author: Kshitiz Pal, Sahil Patel
# Date: 2024/10/04
# Description: creating function strip_vowels which returns string without vowels.



def strip_vowels(string):
    vowels = 'aeiouAEIOU' # Define vowels (both lowercase and uppercase)
    result = "" # Initialize an empty string to store the result

    # Remove vowels from the string
    for i in string:
        if i not in vowels: # Check if the character is not a vowel
            result += i  # Add non-vowel characters to the result string

    return result # Return the final string without vowels

# main method
if __name__ == "__main__":

    string_value="sahil"  # Test string to strip vowels from
    result=strip_vowels(string_value)
    print(f"Original string: {string_value}")
    print(f"String without vowels: {result}")
    

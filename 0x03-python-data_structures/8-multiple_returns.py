#!/usr/bin/python3

# Function to return the length and first character of a string
def multiple_returns(sentence):

    # initiate condition to check if string is empty and return values
    return ((0, None) if (len(sentence) == 0)
            else (len(sentence), sentence[0]))


# Stop script from CLI
if __name__ == "__main__":
    multiple_returns()

#!/usr/bin/python3

# Function returns key with the biggest integer value
def best_score(a_dictionary):

    # iterate & compare dict.items(), & return key with the max value
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    cp_key = list(a_dictionary.keys())[0]
    max_value = a_dictionary[cp_key]
    for key, value in a_dictionary.items():
        if value > max_value:
            max_value = value
            cp_key = key
    return (cp_key)

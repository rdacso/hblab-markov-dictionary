from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    # Opens file and reads it line by line. Turns it into a string.
    content = open(file_path).read()


    return content

def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}


    words = text_string.split()
    # for item in the length of words - 2  
    for i in range(len(words) - 2): 
        # conditional to check to see if tuple pair is not in chains dictionary
        if (words[i], words[i + 1]) not in chains:
            # assign the key value to an empty list
            chains[words[i], words[i + 1]] = []
        # appends value to the list of values in the dictionary
        chains[(words[i], words[i + 1])].append(words[i + 2])

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    # empty string to store results
    text = ""
    # variable to store randomly generated key
    random_key = choice(chains.keys())
    # while loop to iterate through dictionary until condiiton is met
    while random_key in chains:
        # add the random key generated to the text string
        text += random_key[0] + " " + random_key[1] + " "
        # generate a random value based off of random key
        value = choice(chains.get(random_key))
        # combine second key value with random word for new key pair
        random_key = (random_key[1], value)
    # add the last word to the text string
    text += random_key[1]

    return text



input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)


#Produce random text
random_text = make_text(chains)

print random_text

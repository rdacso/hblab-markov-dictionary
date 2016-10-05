from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    content = open(file_path).read()
    words = content.split()
    text = ""
    for word in words:
        text += word + " "

    # print text

    return text
    #"This should be a variable that contains your file text as one long string"

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

    # your code goes here

    words = text_string.split()
    # for item in the length of words - 2  
    for i in range(len(words) - 2):
        # adding the words 1 and 2 to the dictionary as keys 
        # and the third word as a value
        # conditional for whether this tuple already exists in chain
    
        if (words[i], words[i + 1]) in chains:
            # this is true
            value = chains[(words[i], words[i + 1])]
            value.append(words[i + 2])

        else:
            chains[words[i], words[i + 1]] = [words[i + 2]]
    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""
    random_key = choice(chains.keys())
    # if the random key generated exists in the dictionary:
    while random_key in chains:
        # add the random key generated to the text string
        text += random_key[0] + " " + random_key[1]
        # generate a random value based off of random key
        value = choice(chains.get(random_key))
        # combine second key value with random word for new key pair
        new_random = random_key[1] + value

    return text



input_path = "green-eggs.txt"
# print input_path
# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)
# print input_text
# Get a Markov chain
chains = make_chains(input_text)
# print chains

#Produce random text
random_text = make_text(chains)

print random_text

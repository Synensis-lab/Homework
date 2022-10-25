"""
Create required phrase.
----------------------

You are given a string of available characters and a string representing a word or a phrase that you need to generate.
Write a function that checks if you can generate required word/phrase using the characters provided.
If you can, then please return True, otherwise return False.

NOTES:
    You can only generate the phrase if the frequency of unique characters in the characters string is equal or greater
    than frequency in the document string.

FOR EXAMPLE:

    characters = "cbacba"
    phrase = "aabbccc"

    In this case you CANNOT create required phrase, because you are 1 character short!

IMPORTANT:
    The phrase you need to create can contain any characters including special characters, capital letter, numbers
    and spaces.

    You can always generate an empty string.

"""


def generate_phrase(characters, phrase):
    # compare length of characters and phrase - if phrase length > characters =  return false
    if len(phrase) > len(characters):
        return False
    else:
        # create a list append values from characters.
        mirror_phrase = []
        # iterate through phrase searching for each value in characters, if it is present remove from characters
        # and add to mirror_phrase list
        characters = list(characters)
        for value in phrase:
            if value in characters:
                characters.remove(value)
                mirror_phrase.append(value)
        # Turn mirror_phrase list back to string
        mirror_phrase = ''.join(mirror_phrase)
        # check if matches
        if mirror_phrase == phrase:
            return True
        else:
            return False

# example calling function
# print(generate_phrase("cbacba","aabbccc"))
print(generate_phrase("helodooooddddllll3451234!!!!! ","hello1234!!!! "))

#
#






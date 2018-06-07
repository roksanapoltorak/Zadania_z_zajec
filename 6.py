""""
Napisać funkcję filter_non_alphabetic(text), która dla danego
łańcucha znaków zwróci łańcuch powstały przez pominięcie z niego
wszystkich znaków nie będących znakami alfanumerycznymi
"""

def filter_non_alphabetic(text):
    new_text = ''

    for i in text:
        if i.isalnum():
            new_text += i
    return new_text

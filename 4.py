"""
Napisać program tworzący listę słów z podanego łańcucha znaków.
Przez słowo rozumiemy dowolny podłańcuch, zawierający jedynie
znaki alfanumeryczne.
"""

a = "Spam&eggs+-/bar baz"

start = 0
list = []

for current, char in enumerate(a):
    if not char.isalnum():
        list.append(a[start:current])
        start = current + 1

list.append(a[start:])

print(list)
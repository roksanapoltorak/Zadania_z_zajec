"""
Napisać program wypisujący daną listę słów w kolejności
od najkrótszego do najdłuższego.
"""

list = ["abcdef", "abcd", "abcdefgh", "abc", "a", "xbdefghijkl", "c1befghijkl", "abdefghi555"]

last_list = []
hist = {}

for i in list:
    a = len(i)
    hist[i] = [a]

for j in sorted(hist):
    last_list.append(j)

print(last_list)
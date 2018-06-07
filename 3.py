""""
Napisać program znajdujący wszystkie najdłuższe łańcuchy znaków
na danej liście i wypisujący je w kolejności alfabetycznej.
"""

list = ["abcdef", "abcd", "abcdefgh", "abc", "a", "xbdefghijkl", "c1befghijkl", "abdefghi555"]

len_list = []
max_list = []
last_list = []

for i in list:
    a = len(i)
    len_list.append(a)

for j in len_list:
    if j is max(len_list):
        c = max_list.append(i)

for k in list:
    if len(k) == j:
        last_list.append(k)

print(sorted(last_list))


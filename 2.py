""""
Napisać program znajdujący najdłuższy łańcuch znaków na liście.
W razie, gdyby na liście znajdował się więcej niż jeden taki łańcuch,
wynikiem może być dowolny z nich.
"""

list = ["abcdef", "abcd", "abcdefgh", "abc", "abcdefghijklmnoprstuw", "abdefghijkl"]

len_list = []

for i in list:
    a = len(i)
    len_list.append(a)

for j in len_list:
    if j is max(len_list):
        b = len_list.index(j)

print("Najdłuższy łańcuch znaków to : ", list[b])


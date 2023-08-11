from random import randint

with open('my_txt.txt', 'r') as file:
    seq = [x for x in file.readlines()]
    res = seq[randint(0, len(seq) - 1)]

var = 'xx'
print(seq)
print(res)
print(any(map(lambda x: var in x, seq)))

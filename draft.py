with open('try.txt', ) as file:
    pass

# with open('try.txt','r') as rfile:
#     for i in rfile.readlines():
#         print(i, end='')

with open('try.txt', 'r') as mfile:
    res = mfile.readlines()
    print([x for x in res])

with open('try.txt', 'r') as rfile:
    res = [x for x in rfile]
    print('aaa' in res)

# with open('try.txt','r') as file:
#     for i in file.readlines():
#         print(i)

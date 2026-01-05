"""
Problem: Stupid Password Generator
Write a program that enters two integers n and l and generates, in alphabetical order, all possible "stupid” passwords" that consist of the following 5 characters:

Character 1: a digit from 1 to n.
Character 2: a digit from 1 to n.
Character 3: a small letter from the first l letters of the Latin alphabet.
Character 4: a small letter from the first l letters of the Latin alphabet.
Character 5: a digit from 1 to n, greater than the first 2 digits.
Input Data
The input is read as arguments and consists of two integers: n and l within the range [1 … 9].Screenshot 2025-10-07 at 10.53.33 AM.png

Output Data
Return a list of all "stupid" passwords in alphabetical order.
"""
def stupidPassword(n: int, l: int):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    passwords= []

    for c1 in range(1,n):
        for c2 in range(1,n):
            for c3 in range(l):
                letter1=alphabet[c3]
                for c4 in range(l):
                    letter2=alphabet[c4]
                    for c5 in range(1,n+1):
                        if c5 > c1 and c5 > c2:
                            password = str(c1) + str(c2) + letter1 + letter2 + str(c5)
                            passwords.append(password)

    return passwords









#
#     res=[]
#     a = ord('a')
#
#     for c1 in range (1, n):
#         for c2 in range (1,n):
#             for c3 in range (0,l):
#                 for c4 in range (0,l):
#                     c5min =  max(c1, c2)+1
#                     for c5 in range (c5min,n+1):
#                         # print(c1, c2, chr(97+c3), chr(97+c4), c5)
#                         password=f"{c1}{c2}{chr(a+c3)}{chr(a+c4)}{c5}"
#                         print(password)
#                         res.append(password)
#
#     return res
#
# print(stupidPassword(2,4))
#
#

# for x in range (1,n):
#     cht1 = (1, n)
#     cht2 = (1, n)
#     l1 = l
#     l2 = l
#     cht3 = (1, n + 1)
#     cht3 > cht1
#     cht3 > cht2
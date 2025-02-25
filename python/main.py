# Начиная с версии Python 3.11, был введён лимит на количество цифр в строковом представлении целых чисел для предотвращения DoS-атак с использованием больших вычислений.
#import sys
#sys.set_int_max_str_digits(1000000)

'''
S = "Spam"
print(S)
print(S[2:3])
print(S[1:])
S = 'z' + S[1:]
print(S)
'''

'''
S = 'shrubbery'
L = list(S)
print(S, L)

L[1] = 'c'
resulr = ''.join(L)
L2 = list(resulr)
print(resulr, L2 )
'''

'''
B = bytearray(b'spam')
B.extend(b'eggs')
print(B)
result = B.decode()
print(result)

abc = bytearray(b'tit')
abc.extend(b'ki')
print(abc)
result = abc.decode()
print(result)
'''

'''
S = "Spam"
result = S.find('pa')
print(result)
result =  S.replace('pa', 'xyz')
print(result)
'''

line = 'aaa,bbb,ccc,ddd'
result = line.split(',')
print(result)

S = 'Spam'
print(S)
result = S.upper()
print(result)

result = S.isalpha() 
print(result)
result = S.isdigit()
print(result)

line = 'aaa,bbb,ccc,ddd\n'
result = line.rstrip()
print(result)

result = line.rstrip().split(',')
print(result)


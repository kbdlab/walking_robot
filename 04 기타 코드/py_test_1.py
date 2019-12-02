from random import randint as rrr

def generate(n):
    return [str(rrr(0,100)) for i in range(n)]

print(generate(10))

def strToInt(s):
    result = 0
    
    for index, number in enumerate(s[::-1]):
        if number == '-':
            result *= -1
        else:
            result += (ord(number)-48) * (10 ** index)
    
    return result

for i in generate(10):
    print(strToInt(i), int(i))
    
    



str1 = '40'
str2 = '85'
num1 = int(str1, 16)
num2 = int(str2, 16)

ss = ((hex(num1 ^ num2))[2:])
print(type(ss))
print(ss)
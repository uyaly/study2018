base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'),ord('A')+6)]

print(base)
string_num = 15
# dec2bin
# 十进制 to 二进制: bin()
def dec2bin(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num, rem = divmod(num, 2)
        mid.append(base[rem])
    print(''.join([str(x) for x in mid[::-1]]))
    return ''.join([str(x) for x in mid[::-1]])

if __name__ == "__main__":
    str = '100000000010101'
    ll = dec2bin(str)
    print(ll)
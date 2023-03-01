import re

def is_integer(i):
    regex = r'([0-9]|[1-9][0-9]*|[0-7]+|0[xX][0-9a-fA-F]+)(i64|I64|u|U|l|L)?'
    return bool(re.match(regex, i))

if __name__ == "__main__":
    integers = ['28', '4000000024u', '2000000022l', '024', '04000000024u', '02000000022l', '0x2a', '0x4a44000000000020I64', '0x8a44000000000040Ui64']
    for integer in integers: 
        print(integer, is_integer(integer))
import re

def is_integer(i):
    regex = r'[1-9][0-9]*[ul]?|0[0-7]*[ul]?|0x[0-9a-f]+(i64|Ui64)'
    return bool(re.match(regex, i))

if __name__ == "__main__":
    integers = ['28', '4000000024u', '2000000022l', '024', '04000000024u', '02000000022l', '0x2a', '0x4a44000000000020I64', '0x8a44000000000040Ui64']
    for integer in integers: 
        print(integer, is_integer(integer))
import re

def is_float(f):
    regex = r'[+-]?([0-9]*\.[0-9]+|[0-9]+\.)([eE][+-]?[0-9]+)?[fFlL]?|[+-]?[0-9]+[eE][+-]?[0-9]+[fFlL]?'
    return bool(re.match(regex, f))

if __name__ == "__main__":
    floats = ['15.75L', '1.575E1', '1575e-2', '-2.5e-3F', '25E-4']
    for float in floats: 
        print(float, is_float(float))
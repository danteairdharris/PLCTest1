import re

def is_valid(s):
    pattern = r'^/\*[^*/]*\*/$'
    return bool(re.match(pattern, s))


if __name__ == "__main__":
    s = input('Type in the string you want to match. \n')
    print(s, is_valid(s))
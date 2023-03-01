import re 


if __name__ == "__main__":
    pattern1 = r'(a*ba*ba*)*(a*ba*)(c|d)*'
    pattern2 = r'(b*ab*ab*)*(c|d)*'
    pattern3 = r'(cbadcbad)*'
    s = input('Type in a string you want to match. \n')
    if (re.match(pattern1, s) and re.match(pattern2, s)) or re.match(pattern3, s):
        print(s + " True")
    else:
        print(s + " False")
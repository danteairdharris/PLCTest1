import re

def is_valid(s):

    var_pattern = r'^[a-zA-Z_$][a-zA-Z0-9_$]*$'
    class_pattern = r'[A-Z_$][a-zA-Z0-9_$]*'
    method_pattern = r'[a-z_$][a-zA-Z0-9_$]*'
   
    if re.match(var_pattern, s):
        print('The string ' + s + ' matches the pattern for a variable name in Java.')
    else: 
        print('The string ' + s + ' does not match the pattern for a variable name in Java.')
    
    if re.match(class_pattern, s):
        print('The string ' + s + ' matches the pattern for a class name in Java.')
    else: 
        print('The string ' + s + ' does not match the pattern for a class name in Java.')

    if re.match(method_pattern, s):
        print('The string ' + s + ' matches the pattern for a method name in Java.')
    else: 
        print('The string ' + s + ' does not match the pattern for a method name in Java.')

    return

if __name__ == "__main__":
     s = input('Type in the string you would like to match. \n')
     is_valid(s)
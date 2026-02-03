import re

keywords = {'if', 'else', 'while', 'for', 'int', 'float', 'return'}
operators = {'+', '-', '*', '/', '=', '>', '<', '=='}
separators = {'(', ')', '{', '}', ';', ','}

def lexical_analyzer(code):
    tokens = []
    words = re.findall(r'\w+|==|!=|<=|>=|[^\s\w]', code)

    for word in words:
        if word in keywords:
            tokens.append((word, "KEYWORD"))
        elif word in operators:
            tokens.append((word, "OPERATOR"))
        elif word in separators:
            tokens.append((word, "SEPARATOR"))
        elif word.isdigit():
            tokens.append((word, "NUMBER"))
        elif re.match(r'[a-zA-Z_]\w*', word):
            tokens.append((word, "IDENTIFIER"))
        else:
            tokens.append((word, "UNKNOWN"))

    return tokens

with open("input.txt", "r") as file:
    code = file.read()

result = lexical_analyzer(code)

with open("output.txt", "w") as file:
    for token in result:
        file.write(f"{token[0]} : {token[1]}\n")

print("Lexical analysis completed.")

from typing import List


def evalRPN(tokens: List[str]) -> int:
    num_stack = list()
    for token in tokens:
        if token == "+":
            a = num_stack.pop()
            b = num_stack.pop()
            num_stack.append(b + a)
        elif token == "-":
            a = num_stack.pop()
            b = num_stack.pop()
            num_stack.append(b - a)
        elif token == "*":
            a = num_stack.pop()
            b = num_stack.pop()
            num_stack.append(b * a)
        elif token == "/":
            a = num_stack.pop()
            b = num_stack.pop()
            num_stack.append(int(b / a))
        else:
            num_stack.append(int(token))
    return num_stack[0]


if __name__ == '__main__':
    result = evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
    print(result)

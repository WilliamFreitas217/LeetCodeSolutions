def valid_parentheses(s):
    closer_dict = {"(": ")",
                   "{": "}",
                   "[": "]",
                   }
    if s[0] in closer_dict.values():
        return False

    openers = [s[0]]
    for char in s[1:]:
        if char in closer_dict.keys():
            openers.append(char)
        elif (openers and closer_dict[openers[-1]] != char) or (not openers and char in closer_dict.values()):
            return False
        elif openers:
            openers.pop()

    return not openers

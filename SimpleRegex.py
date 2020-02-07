"""
Implement regular expression matching with the following special characters:
    . (period) which matches any single character
    * (asterisk) which matches zero or more of the preceding element
That is, implement a function that takes in a string and a valid regular
expression and returns whether or not the string matches the regular
expression.
"""
word = "Regex"
expression = "R.*x"


def matches(char1, char2):
    if char1 == "." or char2 == ".":
        return True
    if char1 == char2:
        return True
    return False


def regex(string, exp, sp=0, ep=0):
    if exp[0] == "*":
        return False

    while True:
        if sp >= len(string) and ep >= len(exp):
            return True
        if sp >= len(string) or ep >= len(exp):
            return False

        if ep + 1 < len(exp):
            if exp[ep + 1] == "*":
                ep += 1
                continue
        if exp[ep] == "*":
            if regex(string, exp, sp, ep + 1):
                return True
            while matches(string[sp], exp[ep - 1]):
                print("Comparing: " + exp[ep - 1] + " and " + string[sp])
                sp += 1
                if sp >= len(string) and ep + 1 < len(exp):
                    return False
                if regex(string, exp, sp, ep + 1):
                    return True

        if matches(string[sp], exp[ep]):
            print("Comparing: " + exp[ep] + " and " + string[sp])
            sp += 1
            ep += 1
        else:
            return False


def main():
    result = regex(word, expression)
    print()
    if result:
        print(word, "matches", expression)
    else:
        print(word, "does not match", expression)


if __name__ == "__main__":
    main()

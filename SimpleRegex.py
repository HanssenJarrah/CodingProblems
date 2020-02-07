"""
Implement regular expression matching with the following special characters:
    . (period) which matches any single character
    * (asterisk) which matches zero or more of the preceding element
That is, implement a function that takes in a string and a valid regular
expression and returns whether or not the string matches the regular
expression.
"""
word = "Regexp"
expression = "R.*p"


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
        # Tests if the end of the strings has been reached so regex can stop
        if sp >= len(string) and ep >= len(exp):
            return True
        if sp >= len(string) or ep >= len(exp):
            return False

        # Skips to the next character of the regular expression if the following one is '*', as they can
        # be valued to have a length of 0
        if ep + 1 < len(exp):
            if exp[ep + 1] == "*":
                ep += 1
                continue

        # Recursively calls regex() responsible for functionality of the '*' symbol
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

        # Checks if the compared letters are the same (or '.') each iteration
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

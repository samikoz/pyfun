def squash_consecutive(string):
    """returns a list of tuples (char, repetitions) from a given string. functional."""

    def accumulate_recursively(s, current_char=None, accumulated=()):
        if s == '':
            return accumulated

        return accumulate_recursively(
            s[1:],
            s[0],
            (*accumulated[:-1], (current_char, accumulated[-1][1] + 1)) if s[0] == current_char
            else (*accumulated, (s[0], 1))
        )

    return accumulate_recursively(string)

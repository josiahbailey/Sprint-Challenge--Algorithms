'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    try:
        word[0]
    except IndexError:
        return 0
    else:
        if word[0] == 't':
            try:
                word[1]
            except IndexError:
                return 0
            else:
                if word[1] == 'h':
                    return 1 + count_th(word[1:])
        return count_th(word[1:])


print(count_th("othouth"))

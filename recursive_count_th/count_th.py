'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    result = 0
    if len(word) < 2:
        return 0
    # if the first and second index of a word are t or h
    # increment the result
    if word[0] == 't' and word[1] == 'h':
        result += 1
    # add both the result and count of the word togethere in order to get final outcome
    return result + count_th(word[1:])


def palindrome(word):
    '''
    Checks if passed argument is a palindrome
    Argument: word
    '''
    if word == word[::-1]:
        return True
    else:
        return False
        
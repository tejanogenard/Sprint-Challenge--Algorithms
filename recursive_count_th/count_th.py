'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.

P: a single word string 
R: returning the function and returning the number of times "th" appears 
E: 
    input: "thegoodthboyth"

        returns: 3 

P:  
    # we want to check if our word is valid length
        if length of word < 2 
            return 0 
    # we want to check the index @ 0 = 't' and 1 = 'h' 
        if length of word > 2 
                return 1 + count_th(word[1:]) "we're updating our word length and a count"
        else:
            return 1 "just return one count
    # elif index @  0 = 't' and 1 = 'h'  is false 
        return count_th(word[1:])


'''
def count_th(word):
    if len(word) < 2:
        return 0

    elif word[0:2] == 'th':
        return 1 + count_th(word[1:])
    
    else: 
        return count_th(word[1:])



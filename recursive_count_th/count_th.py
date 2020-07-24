'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # create an index to keep track of which letter we're on inside the word 
    # we want to how many times we find the substring "th"
    # increment the index and recursivelt call until we're at the end of the string
    index = 0
    print()
    print(index)
    if index < len(word):
        print(word.count("th"))
        print(index)
        index = index + 1
        print(index)
        return count_th(word) 
   

    


count_th("thegoththodboy")
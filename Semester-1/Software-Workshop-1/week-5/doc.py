def word_count(text):
    """
    str -> Dict[str, int]
    Count the frequency of each word in the provided text. 
    Consider words as case-insensitive and ignore common punctuation.
    >>> word_count('Hello, hello world!')
    {'hello': 2, 'world': 1}
    >>> word_count('A rose is a rose.')
    {'a': 2, 'rose': 2, 'is': 1}
    """
    text = text.lower()
    
    # Replace punctuation with spaces
    for char in '.,!?;':
        text = text.replace(char, ' ')
    
    words = text.split()
    result = {}
    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
            
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
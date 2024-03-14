def clean_tweets():
    f = open("ReviewingTheWeeks/tweets_to_clean.txt", 'r')
    tweets = f.read()
    words = tweets.split()
    print(words)
    return words


def tweet_cleaning(words):
    elements_to_remove = {"@", "#", "-", "—", "–", "&", "%"}
    cleaned_words = []
    valid = 'True'
    for word in words:
        if word.startswith('http') or \
                word.startswith('www.') or \
                word.startswith('...') or \
                word.endswith('...'):
            valid = 'False'
        if any(char.isdigit() for char in word):
            valid = 'False'
        for each_char in word:
            if each_char in elements_to_remove:
                valid = 'False'
        # Append the cleaned word to the result
        if valid == 'True':
            cleaned_words.append(word)
        valid = 'True'
    print(cleaned_words)
    return cleaned_words


def remove_duplicate_words(words):
    """
    make use of the cleaned words list from tweet_cleaning() - change the method accordingly - and
    get rid of any duplicate words in the list
    :return: the non-duplicated list
    """
    elements_to_remove = {"@", "#", "-", "—", "–", "&", "%"}
    cleaned_words = []
    valid = 'True'
    for word in words:
        if word.startswith('http') or \
                word.startswith('www.') or \
                word.startswith('...') or \
                word.endswith('...'):
            valid = 'False'
        if any(char.isdigit() for char in word):
            valid = 'False'
        for each_char in word:
            if each_char in elements_to_remove:
                valid = 'False'
        # Append the cleaned word to the result
        if valid == 'True':
            if word not in cleaned_words:
                cleaned_words.append(word)
        valid = 'True'
    print(cleaned_words)


def main():
    words_to_clean = clean_tweets()
    tweet_cleaning(words_to_clean)
    remove_duplicate_words(words_to_clean)

if __name__ == "__main__":
    main()
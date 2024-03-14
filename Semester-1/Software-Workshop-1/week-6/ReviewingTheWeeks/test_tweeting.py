import pytest
import tweeting

def test_tweet_cleaning():
    words = ['@what', 'is', 'happening', 'this', 'week&^end?', 'lets', 'hope', 'that', 'the', 'foo%tball', '5takes', 'pla9ce', 'th@ere', '@is', 'a', 'storm', '@looming', 'in', 'Sc#otland,', 'th-ere', 'may', 'be', 'flooding...', 'http://www.make/it/up', '...Hello', 'where', 'is', 'that', 'flooding', 'ta-king', 'place?', '@', 'how', 'are', 'you', 'doing?', 'are', 'you', 'going', 'to', 'the', 'city', 'today?']
    assert tweeting.tweet_cleaning(words) == ['is', 'happening', 'this', 'lets', 'hope', 'that', 'the', 'a', 'storm', 'in', 'may', 'be', 'where', 'is', 'that', 'flooding', 'place?', 'how', 'are', 'you', 'doing?', 'are', 'you', 'going', 'to', 'the', 'city', 'today?']
from challenges.repeated_words.repeated_words import Node,LinkedList,repeated_word

def test_empety_srting():
    em_str = ''
    assert repeated_word(em_str) == 'there is no repeated word in this paragraph'

def test_string_without_repeating_words():
    paragraph = 'i love python'
    assert repeated_word(paragraph) == 'there is no repeated word in this paragraph'

def test_easy_pargraph_with_dot():
    pargraph = "Once upon a time, there was a brave princess who..."
    assert repeated_word(pargraph) == 'a'

def test_pargraph_with_dot_and_some_is_capitalize():
    pargraph = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    assert repeated_word(pargraph) == 'it'

def test_pargraph_with_dot_and_comma():
    pargraph = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    assert repeated_word(pargraph) == 'summer'
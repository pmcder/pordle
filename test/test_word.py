from words import Word


def test_is_not_valid():

    test = Word.Words.is_valid("xabje")
    assert test == False

def test_is_valid():

    test = Word.Words.is_valid("table")
    assert test == True

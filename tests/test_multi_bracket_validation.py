from data_structures_and_algorithms_401.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation


"""
Test Cases:
    1. {}	TRUE
    2. {}(){}	TRUE
    3. ()[[Extra Characters]]	TRUE
    4. (){}[[]]	TRUE
    5. {}{Code}[Fellows](())	TRUE
    6. [({}]	FALSE
    7. (](	FALSE
    8. {(})	FALSE
"""

def test_1():
    assert multi_bracket_validation("{}") == True

def test_2():
    assert multi_bracket_validation("{}(){}") == True

def test_3():
    assert multi_bracket_validation("()[[Extra Characters]]") == True

def test_4():
    assert multi_bracket_validation("(){}[[]]") == True

def test_5():
    assert multi_bracket_validation("{}{Code}[Fellows](())") == True

def test_6():
    assert multi_bracket_validation("[({}]") == False

def test_7():
    assert multi_bracket_validation("(](") == False

def test_8():
    assert multi_bracket_validation("{(})") == False
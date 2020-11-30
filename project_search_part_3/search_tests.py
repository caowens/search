from search import title_to_info, keyword_to_titles, search, article_info, article_length, title_timestamp, favorite_author, multiple_keywords, display_result
from search_tests_helper import print_basic, print_advanced, print_advanced_option, get_print
from wiki import article_metadata, title_to_info_map, keyword_to_titles_map
from unittest.mock import patch
from copy import deepcopy

# List of all available article titles for this search engine
# The benefit of using this is faster code - these functions will execute
# every time it gets called, but if the return value of it gets stored it into
# a variable, the function will not need to run every time the list of available
# articles is needed.
METADATA = article_metadata()
TITLE_TO_INFO = title_to_info_map()
KEYWORD_TO_TITLES = keyword_to_titles_map()

# Storing into a variable so don't need to copy and paste long list every time
DOG = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog']

TRAVEL = ['Time travel']

MUSIC = ['List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', 'Kevin Cadogan', '2009 in music', 'Rock music', 'Lights (musician)', 'Tim Arnold (musician)', 'Old-time music', 'Arabic music', 'Joe Becker (musician)', 'Richard Wright (musician)', 'Voice classification in non-classical music', '1936 in music', '1962 in country music', 'List of dystopian music, TV programs, and games', 'Steve Perry (musician)', 'David Gray (musician)', 'Alex Turner (musician)', 'List of gospel musicians', 'Indian classical music', '1996 in music', 'Traditional Thai musical instruments', '2006 in music', 'Tony Kaye (musician)', 'Texture (music)', '2007 in music', '2008 in music']

PROGRAMMING = ['C Sharp (programming language)', 'Python (programming language)', 'Lua (programming language)', 'Covariance and contravariance (computer science)', 'Personal computer', 'Ruby (programming language)']

SOCCER = ['Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)']

PHOTO = ['Digital photography']

SCHOOL = ['Edogawa, Tokyo', 'Fisk University', 'Annie (musical)', 'Alex Turner (musician)']

PLACE = ['2009 in music', 'List of dystopian music, TV programs, and games', '2006 in music', '2007 in music', '2008 in music']

DANCE = ['List of Canadian musicians', '2009 in music', 'Old-time music', '1936 in music', 'Indian classical music']

def test_example_title_to_info_tests():
    ''' Tests for title_to_info(), function #1. '''
    # Example tests, these do not count as your tests
    assert title_to_info(METADATA) == TITLE_TO_INFO

    # Create fake metadata to test
    fake_metadata = [['an article title', 'andrea', 1234567890, 103, ['some', 'words', 'that', 'make', 'up', 'sentence']],
                     ['another article title', 'helloworld', 987123456, 8029, ['more', 'words', 'could', 'make', 'sentences']]]

    # Expected value of title_to_info with fake_metadata
    expected = {'an article title': {'author': 'andrea', 'timestamp': 1234567890, 'length': 103}, 
                'another article title': {'author': 'helloworld', 'timestamp': 987123456, 'length': 8029}}
    assert title_to_info(deepcopy(fake_metadata)) == expected

def test_title_to_info():
    fake_metadata_1 = [['Anakin Vader Moment', 'George', 9876543210, 105, ['It', 'is', 'over', 'Anakin']],
                     ['Obi-Wan High Ground Moment', 'Lucas', 1234567890, 3000, ['I', 'have', 'the', 'high', 'ground']]]
    fake_metadata_1_expected = {'Anakin Vader Moment': {'author': 'George', 'timestamp': 9876543210, 'length': 105}, 'Obi-Wan High Ground Moment': {'author': 'Lucas', 'timestamp': 1234567890, 'length': 3000}}
    assert title_to_info(fake_metadata_1) == fake_metadata_1_expected
    
    fake_metadata_2 = [[' ', ' ', 0, 0, [' ', ' ', ' ', ' ']],
                     [' ', ' ', 0, 0, [' ', ' ', ' ', ' ', ' ']]]
    fake_metadata_2_expected = {' ': {'author': ' ', 'timestamp': 0, 'length': 0}}
    assert title_to_info(fake_metadata_2) == fake_metadata_2_expected
    
    fake_metadata_3 = [[0, 0, ' ', ' ', [0, 0, 0, 0]],
                     [0, 0, ' ', ' ', [0, 0, 0, 0, 0]]]
    fake_metadata_3_expected = {0: {'author': 0, 'timestamp': ' ', 'length': ' '}}
    assert title_to_info(fake_metadata_3) == fake_metadata_3_expected

def test_example_keyword_to_titles_tests():
    ''' Tests for keyword_to_titles(), function #2. '''
    # Function #2
    assert keyword_to_titles(METADATA) == KEYWORD_TO_TITLES

    # Create fake metadata to test
    fake_metadata = [['an article title', 'andrea', 1234567890, 103, ['some', 'words', 'that', 'make', 'up', 'sentence']],
                     ['another article title', 'helloworld', 987123456, 8029, ['more', 'words', 'could', 'make', 'sentences']]]

    # Expected value of keyword_to_titles with fake_metadata
    expected = {'some': ['an article title'], 'words': ['an article title', 'another article title'], 'that': ['an article title'], 'make': ['an article title', 'another article title'], 'up': ['an article title'], 'sentence': ['an article title'], 'more': ['another article title'], 'could': ['another article title'], 'sentences': ['another article title']}

    assert keyword_to_titles(deepcopy(fake_metadata)) == expected

def test_keyword_to_titles():
    fake_metadata_1 = [['Anakin Vader Moment', 'George', 9876543210, 105, ['It', 'is', 'over', 'Anakin']],
                     ['Obi-Wan High Ground Moment', 'Lucas', 1234567890, 3000, ['I', 'have', 'the', 'high', 'ground']]]
    fake_metadata_1_expected = {'It': ['Anakin Vader Moment'], 'is': ['Anakin Vader Moment'], 'over': ['Anakin Vader Moment'], 'Anakin': ['Anakin Vader Moment'], 'I': ['Obi-Wan High Ground Moment'], 'have': ['Obi-Wan High Ground Moment'], 'the': ['Obi-Wan High Ground Moment'], 'high': ['Obi-Wan High Ground Moment'], 'ground': ['Obi-Wan High Ground Moment']}
    assert keyword_to_titles(fake_metadata_1) == fake_metadata_1_expected
    
    fake_metadata_2 = [[' ', ' ', 0, 0, [' ', ' ', ' ', ' ']],
                     [' ', ' ', 0, 0, [' ', ' ', ' ', ' ', ' ']]]
    fake_metadata_2_expected = {' ': [' ', ' ']}
    assert keyword_to_titles(fake_metadata_2) == fake_metadata_2_expected
    
    fake_metadata_3 = [[0, 0, ' ', ' ', [0, 0, 0, 0]],
                     [0, 0, ' ', ' ', [0, 0, 0, 0, 0]]]
    fake_metadata_3_expected = {0: [0, 0]}
    assert keyword_to_titles(fake_metadata_3) == fake_metadata_3_expected

def test_example_unit_tests():
    # Example tests, these do not count as your tests

    # Basic search, function #3
    assert search('dog', keyword_to_titles_map()) == DOG

    # Advanced search option 1, function #4
    expected = {'Black dog (ghost)': {'author': 'SmackBot', 'timestamp': 1220471117, 'length': 14746}, 'Mexican dog-faced bat': {'author': 'AnomieBOT', 'timestamp': 1255316429, 'length': 1138}, 'Dalmatian (dog)': {'author': 'J. Spencer', 'timestamp': 1207793294, 'length': 26582}, 'Guide dog': {'author': 'Sarranduin', 'timestamp': 1165601603, 'length': 7339}, 'Sun dog': {'author': 'Hellbus', 'timestamp': 1208969289, 'length': 18050}}
    assert article_info(deepcopy(DOG), TITLE_TO_INFO) == expected

    # Advanced search option 2, function #5
    expected = ['Mexican dog-faced bat', 'Guide dog']
    assert article_length(8000, deepcopy(DOG), TITLE_TO_INFO) == expected

    # Advanced search option 3, function #6
    expected = {'Black dog (ghost)': 1220471117, 'Mexican dog-faced bat': 1255316429, 'Dalmatian (dog)': 1207793294, 'Guide dog': 1165601603, 'Sun dog': 1208969289}
    assert title_timestamp(deepcopy(DOG), TITLE_TO_INFO) == expected

    # Advanced search option 4, function #7
    assert favorite_author('J. Spencer', deepcopy(DOG), TITLE_TO_INFO) == True
    assert favorite_author('Andrea', deepcopy(DOG), TITLE_TO_INFO) == False

    # Advanced search option 5, function #8
    expected = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog', 'Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)']
    assert multiple_keywords('soccer', deepcopy(DOG)) == expected

def test_search():
    soccer_expected = ['Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)']
    assert search('soccer', keyword_to_titles_map()) == soccer_expected
    
    assert search('nature', keyword_to_titles_map()) == []
    
    assert search('', keyword_to_titles_map()) == []

def test_article_info():
    photo_expected = {'Digital photography': {'author': 'Mintleaf', 'timestamp': 1095727840, 'length': 18093}}
    assert article_info(search('photo', keyword_to_titles_map()), title_to_info(article_metadata())) == photo_expected
    
    assert article_info(search('nature', keyword_to_titles_map()), title_to_info(article_metadata())) == {}
    
    assert article_info(search('', keyword_to_titles_map()), title_to_info(article_metadata())) == {}

def test_article_length():
    programming_8000_expected = ['Lua (programming language)', 'Covariance and contravariance (computer science)']
    assert article_length(8000, search('programming', keyword_to_titles_map()), title_to_info(article_metadata())) == programming_8000_expected
    
    travel_1000_expected = []
    assert article_length(1000, search('travel', keyword_to_titles_map()), title_to_info(article_metadata())) == travel_1000_expected
    
    happy_8000_expected = []
    assert article_length(8000, search('happy', keyword_to_titles_map()), title_to_info(article_metadata())) == happy_8000_expected
    
    photo_0_expected = []
    assert article_length(0, search('photo', keyword_to_titles_map()), title_to_info(article_metadata())) == photo_0_expected

def test_title_timestamp():
    school_expected = {'Edogawa, Tokyo': 1222607041, 'Fisk University': 1263393671, 'Annie (musical)': 1223619626, 'Alex Turner (musician)': 1187010135}
    assert title_timestamp(search('school', keyword_to_titles_map()), title_to_info(article_metadata())) == school_expected
    
    nature_expected = {}
    assert title_timestamp(search('nature', keyword_to_titles_map()), title_to_info(article_metadata())) == nature_expected
    
    empty_string_expected = {}
    assert title_timestamp(search('', keyword_to_titles_map()), title_to_info(article_metadata())) == empty_string_expected

def test_favorite_author():
    assert favorite_author('J. Spencer', search('dog', keyword_to_titles_map()), title_to_info(article_metadata())) == True
    assert favorite_author('Brandon Sanderson', search('programming', keyword_to_titles_map()), title_to_info(article_metadata())) == False
    assert favorite_author('William Shakespeare', search('nature', keyword_to_titles_map()), title_to_info(article_metadata())) == False

def test_multiple_keywords():
    photo_travel_expected = ['Time travel', 'Digital photography']
    assert multiple_keywords('photo', search('travel', keyword_to_titles_map())) == photo_travel_expected
    
    nature_dance_expected = ['List of Canadian musicians', '2009 in music', 'Old-time music', '1936 in music', 'Indian classical music']
    assert multiple_keywords('nature', search('dance', keyword_to_titles_map())) == nature_dance_expected
    
    empty_strings_expected = []
    assert multiple_keywords('', search('', keyword_to_titles_map())) == empty_strings_expected

# For all integration test functions, remember to put in patch so input() gets mocked out
@patch('builtins.input')
def test_example_integration_test(input_mock):
    keyword = 'dog'
    advanced_option = 2
    advanced_response = 8000

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])

    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Mexican dog-faced bat', 'Guide dog']\n"

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected

# TODO Write tests below this line. Do not remove.
@patch('builtins.input')
def test_article_length_integration_test(input_mock):
    keyword = 'programming'
    advanced_option = 2
    advanced_response = 8000

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])

    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Lua (programming language)', 'Covariance and contravariance (computer science)']\n"

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected

@patch('builtins.input')
def test_title_timestamp_integration_test(input_mock):
    keyword = 'school'
    advanced_option = 3

    # Output of calling display_results() with given user input
    output = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\n\nHere are your articles: {'Edogawa, Tokyo': 1222607041, 'Fisk University': 1263393671, 'Annie (musical)': 1223619626, 'Alex Turner (musician)': 1187010135}"

    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\n\nHere are your articles: {'Edogawa, Tokyo': 1222607041, 'Fisk University': 1263393671, 'Annie (musical)': 1223619626, 'Alex Turner (musician)': 1187010135}"

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected
    
# Write tests above this line. Do not remove.

# This automatically gets called when this file runs - this is how Python works.
# To make all tests run, call all test functions inside the if statement.
if __name__ == "__main__":
    # TODO Call all your test functions here
    # Follow the correct indentation as these two examples
    # As you're done with each function, uncomment the example test functions
    # and make sure they pass
    test_example_title_to_info_tests()
    test_example_keyword_to_titles_tests()
    test_example_unit_tests()
    test_example_integration_test()
    test_title_to_info()
    test_keyword_to_titles()
    test_search()
    test_article_info()
    test_article_length()
    test_title_timestamp()
    test_multiple_keywords()
    test_article_length_integration_test()
    test_title_timestamp_integration_test()
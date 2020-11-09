from search import search, article_length, article_count, random_article, favorite_author, title_author, multiple_keywords, display_result
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_metadata
from unittest.mock import patch

# List of all available article titles for this search engine
# The benefit of using this is faster code - article_metadata() will execute
# every time it gets called, but if the return value of it gets stored it into
# a variable, the function will not need to run every time the list of available
# articles is needed.
METADATA = article_metadata()

# Storing into a variable so don't need to copy and paste long list every time
# All given examples of metadata
# Pass a copy of any of these lists when passing as an argument into a function, 
# otherwise the original list (ie the one stored in the variable) is going to be
# mutated. To make a copy, you may use the .copy() function for the variable holding
# your search result (ie pass DOG.copy() into the function you want to use DOG)
DOG = [['Black dog (ghost)', 'SmackBot', 1220471117, 14746], ['Mexican dog-faced bat', 'AnomieBOT', 1255316429, 1138], ['Dalmatian (dog)', 'J. Spencer', 1207793294, 26582], ['Guide dog', 'Sarranduin', 1165601603, 7339], ['Sun dog', 'Hellbus', 1208969289, 18050]]

TRAVEL = [['Time travel', 'Thug outlaw69', 1140826049, 35170]]

MUSIC = [['List of Canadian musicians', 'Bearcat', 1181623340, 21023], ['French pop music', 'Brandon', 1172208041, 5569], ['Noise (music)', 'Epbr123', 1194207604, 15641], ['1922 in music', 'Jafeluv', 1242717698, 11576], ['1986 in music', 'Michael', 1048918054, 6632], ['Kevin Cadogan', 'Renesis', 1144136316, 3917], ['2009 in music', 'SE KinG', 1235133583, 69451], ['Rock music', 'Sabrebd', 1258069053, 119498], ['Lights (musician)', 'Espo3699', 1213914297, 5898], ['Tim Arnold (musician)', 'Sohohobo', 1181480380, 4551], ['Old-time music', 'Badagnani', 1124771619, 12755], ['Arabic music', 'Badagnani', 1209417864, 25114], ['Joe Becker (musician)', 'Gary King', 1203234507, 5842], ['Richard Wright (musician)', 'Bdubiscool', 1189536295, 16185], ['Voice classification in non-classical music', 'Iridescent', 1198092852, 11280], ['1936 in music', 'JohnRogers', 1243745950, 23417], ['1962 in country music', 'Briguy52748', 1249862464, 7954], ['List of dystopian music, TV programs, and games', 'Notinasnaid', 1165317338, 13458], ['Steve Perry (musician)', 'Woohookitty', 1254812045, 22204], ['David Gray (musician)', 'RattleandHum', 1159841492, 7203], ['Alex Turner (musician)', 'CambridgeBayWeather', 1187010135, 9718], ['List of gospel musicians', 'Absolon', 1197658845, 3805], ['Indian classical music', 'Davydog', 1222543238, 9503], ['1996 in music', 'Kharker', 1148585201, 21688], ['Traditional Thai musical instruments', 'Badagnani', 1191830919, 6775], ['2006 in music', 'Suduser85', 1171547747, 105280], ['Tony Kaye (musician)', 'Bondegezou', 1141489894, 8419], ['Texture (music)', 'J Lorraine', 1161070178, 3626], ['2007 in music', 'Squilly', 1169248845, 45652], ['2008 in music', 'Ba11innnn', 1217641857, 107605]]

PROGRAMMING = [['C Sharp (programming language)', 'Eaglizard', 1232492672, 52364], ['Python (programming language)', 'Lulu of the Lotus-Eaters', 1137530195, 41571], ['Lua (programming language)', 'Makkuro', 1113957128, 0], ['Covariance and contravariance (computer science)', 'Wakapop', 1167547364, 7453], ['Personal computer', 'Darklock', 1220391790, 45663], ['Ruby (programming language)', 'Hervegirod', 1193928035, 30284]]

SOCCER = [['Spain national beach soccer team', 'Pegship', 1233458894, 1526], ['Will Johnson (soccer)', 'Mayumashu', 1218489712, 3562], ['Steven Cohen (soccer)', 'Scouselad10', 1237669593, 2117]]

PHOTOGRAPHY = [['Digital photography', 'Mintleaf', 1095727840, 18093]]

SCHOOL = [['Edogawa, Tokyo', 'Ciphers', 1222607041, 4526], ['Fisk University', 'NerdyScienceDude', 1263393671, 16246], ['Annie (musical)', 'Piano non troppo', 1223619626, 27558], ['Alex Turner (musician)', 'CambridgeBayWeather', 1187010135, 9718]]

PLACE = [['2009 in music', 'SE KinG', 1235133583, 69451], ['List of dystopian music, TV programs, and games', 'Notinasnaid', 1165317338, 13458], ['2006 in music', 'Suduser85', 1171547747, 105280], ['2007 in music', 'Squilly', 1169248845, 45652], ['2008 in music', 'Ba11innnn', 1217641857, 107605]]

def test_example_unit_tests():
    # Example tests, these do not count as your tests

    # Basic search, function #1
    assert search('dog') == DOG 
    
    # Advanced search option 1, function #2
    expected = [['Mexican dog-faced bat', 'AnomieBOT', 1255316429, 1138], ['Guide dog', 'Sarranduin', 1165601603, 7339]]
    assert article_length(8000, 'dog') == expected

    # Advanced search option 2, function #3
    expected = [['Black dog (ghost)', 'SmackBot', 1220471117, 14746], ['Mexican dog-faced bat', 'AnomieBOT', 1255316429, 1138], ['Dalmatian (dog)', 'J. Spencer', 1207793294, 26582]] 
    assert article_count(3, 'dog') == expected

    # Advanced search option 3, function #4
    expected = ['Guide dog', 'Sarranduin', 1165601603, 7339]
    assert random_article(3, 'dog') == expected
    
    # Advanced search option 4, function #5
    assert favorite_author('J. Spencer', 'dog') == True

    # Advanced search option 5, function #6
    expected = [['Black dog (ghost)', 'SmackBot'], ['Mexican dog-faced bat', 'AnomieBOT'], ['Dalmatian (dog)', 'J. Spencer'], ['Guide dog', 'Sarranduin'], ['Sun dog', 'Hellbus']]
    assert title_author('dog') == expected

    # Advanced search option 6, function #7
    expected = [['Black dog (ghost)', 'SmackBot', 1220471117, 14746], ['Mexican dog-faced bat', 'AnomieBOT', 1255316429, 1138], ['Dalmatian (dog)', 'J. Spencer', 1207793294, 26582], ['Guide dog', 'Sarranduin', 1165601603, 7339], ['Sun dog', 'Hellbus', 1208969289, 18050], ['Spain national beach soccer team', 'Pegship', 1233458894, 1526], ['Will Johnson (soccer)', 'Mayumashu', 1218489712, 3562], ['Steven Cohen (soccer)', 'Scouselad10', 1237669593, 2117]]
    assert multiple_keywords('soccer', 'dog') == expected

def test_search():
    assert search('photo') == [['Digital photography', 'Mintleaf', 1095727840, 18093]] 
    assert search('place') == PLACE
    assert search('programming') == PROGRAMMING

def test_article_length():
    assert article_length(8000, 'programming') == [['Lua (programming language)', 'Makkuro', 1113957128, 0], ['Covariance and contravariance (computer science)', 'Wakapop', 1167547364, 7453]]
    assert article_length(10000, 'travel') == []
    assert article_length(70000, 'place') == [['2009 in music', 'SE KinG', 1235133583, 69451], ['List of dystopian music, TV programs, and games', 'Notinasnaid', 1165317338, 13458], ['2007 in music', 'Squilly', 1169248845, 45652]]

def test_article_count():
    assert article_count(5, 'travel') == [['Time travel', 'Thug outlaw69', 1140826049, 35170]]
    assert article_count(0, 'place') == []
    assert article_count(2, 'soccer') == [['Spain national beach soccer team', 'Pegship', 1233458894, 1526], ['Will Johnson (soccer)', 'Mayumashu', 1218489712, 3562]]

def test_random_article():
    assert random_article(3, 'music') == ['1922 in music', 'Jafeluv', 1242717698, 11576]
    assert random_article(4, 'programming') == ['Personal computer', 'Darklock', 1220391790, 45663]
    assert random_article(1, 'school') == ['Fisk University', 'NerdyScienceDude', 1263393671, 16246]

def test_favorite_author():
    assert favorite_author('Thug outlaw69', 'travel') == True
    assert favorite_author('Johnny', 'music') == False
    assert favorite_author('Susan', 'photography') == False

def test_title_author():
    assert title_author('photo') == [['Digital photography', 'Mintleaf']]
    assert title_author('nature') == []
    assert title_author('dance') == [['List of Canadian musicians', 'Bearcat'], ['2009 in music', 'SE KinG'], ['Old-time music', 'Badagnani'], ['1936 in music', 'JohnRogers'], ['Indian classical music', 'Davydog']]

def test_multiple_keywords():
    assert multiple_keywords('photo', 'dance') == [['Digital photography', 'Mintleaf', 1095727840, 18093], ['List of Canadian musicians', 'Bearcat', 1181623340, 21023], ['2009 in music', 'SE KinG', 1235133583, 69451], ['Old-time music', 'Badagnani', 1124771619, 12755], ['1936 in music', 'JohnRogers', 1243745950, 23417], ['Indian classical music', 'Davydog', 1222543238, 9503]]
    assert multiple_keywords('school', ' ') == [['Edogawa, Tokyo', 'Ciphers', 1222607041, 4526], ['Fisk University', 'NerdyScienceDude', 1263393671, 16246], ['Annie (musical)', 'Piano non troppo', 1223619626, 27558], ['Alex Turner (musician)', 'CambridgeBayWeather', 1187010135, 9718]]
    assert multiple_keywords(' ', ' ') == []

# For all integration test functions, remember to put in patch so input() gets mocked out
@patch('builtins.input')
def test_example_integration_test(input_mock):
    keyword = 'dog'
    advanced_option = 1 
    advanced_response = 8000

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])

    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: [['Mexican dog-faced bat', 'AnomieBOT', 1255316429, 1138], ['Guide dog', 'Sarranduin', 1165601603, 7339]]\n"

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected

# TODO Write tests below this line. Do not remove.
@patch('builtins.input')
def test_random_programming(input_mock):
    keyword = 'programming'
    advanced_option = 3 
    advanced_response = 1

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])

    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Python(programming language)', 'Lulu of the Lotus-Eaters', 1137530195, 41571]\n"

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected
# Write tests above this line. Do not remove.

# This automatically gets called when this file runs - this is how Python works.
# To actually make all your tests run, call all of your test functions here.
if __name__ == "__main__":
    # TODO Call all your test functions here
    # Follow the correct indentation as these two examples
    test_example_unit_tests()
    test_example_integration_test()
    test_search()
    test_article_length()
    test_article_count()
    test_random_article()
    test_favorite_author()
    test_title_author()
    test_multiple_keywords()
    test_random_programming()

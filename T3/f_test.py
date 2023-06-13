
import pytest


from f import add
@pytest.mark.parametrize(
    ('input_n', 'input_m', 'expected'),
    (
        (5, 10, 15),
        (10, 10, 20),
    )
)

def test_add(input_n, input_m, expected):
    assert add(input_n,input_m) == expected
    
    
from f import num_rounds
def test_num():
    assert isinstance(num_rounds, int)
    
from f import user_wins
def test_win():
    assert isinstance(user_wins, int)
    
from f import computer_wins
def test_cwin():
    assert isinstance(computer_wins, int)
    
from f import play_again
def test_playagain():
    assert isinstance(play_again, str)
    
from f import a
def test_a():
    assert a >= 0
    
from f import a
def test_a():
    assert isinstance(a, int)

from f import user

# @pytest.mark.skip()
def test_user():
    user() == str
    pass


def test_alpha():
    assert"hello".isalpha() == True
    assert"123".isalpha() == False
    assert"hello world".isalpha() == False
    







# from p import winner

# import pytest

# @pytest.mark.parametrize(
#     ('input_n', 'input_m', 'expected'),
#     (
#         (rock, rock, tie),
#         (rock, scissors, user),
#     )
# )

# def test_winner(input_n, input_m, expected):
#     assert winner(input_n,input_m) == expected
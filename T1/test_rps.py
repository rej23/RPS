from tt import add

import pytest

@pytest.mark.parametrize(
    ('input_n', 'input_m', 'expected'),
    (
        (5, 10, 15),
        (10, 10, 20),
    )
)

def test_add(input_n, input_m, expected):
    assert add(input_n,input_m) == expected





    

   
from tt import ll




def test_ll():
    assert ll() == (2, 10, 12)
    
    
from tt import a     

def test_a():
    assert a  == 444
    


from tt import lol

def test_lol(monkeypatch):
    monkeypatch.setattr()
    
    assert lol() == 2
    









# import random 

# from tt import lol
    
    
# import pytest

# @pytest.mark.parametrize(
#     ('input_n1', 'input_nn', 'expected'),
#     (
#         (5, 5, 10),
#         (10, 4, 14),
#     )
# )

# def test_lol(input_n, input_m, expected):
#     assert lol() == expected
    


    

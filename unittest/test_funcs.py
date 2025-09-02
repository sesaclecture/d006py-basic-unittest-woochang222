# TODO: 사용자 모듈 import
from funcs import is_even, average, max_in_list, min_in_list

# TODO: 아래의 코드를 삭제하고 unittest를 작성하세요.
def test_is_even():
    assert True == is_even(2)
    assert False == is_even(3)
def test_average():
    assert 2 == average([1, 2, 3])
    
def test_max_in_list():
    assert 3 == max_in_list([1, 2, 3])

def test_min_in_list():
    assert 1 == min_in_list([1, 2, 3])



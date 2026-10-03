import pytest
from app.calculator import sum_number
#данные для теста
@pytest.fixture(params=[
    ((2,3), 5),
    ((10,-5,3), 8),
    ((0,5,0,10), 15),
])
def num_data(request):
    return request.param
#проверяем результат
def test_sum_num(num_data):
    numbers, expected = num_data
    assert sum_number(*numbers) == expected
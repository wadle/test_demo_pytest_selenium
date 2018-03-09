import pytest

data = [
    {
        "test_case_id": "TC1",
        "test_input": "3+5",
        "expected" : 8
    },
    {
        "test_case_id": "TC2",
        "test_input": "2+4",
        "expected": 6
    },
    {
        "test_case_id": "TC3",
        "test_input": "6*9",
        "expected": 42
    },
    {
        "test_case_id": "TC4",
        "test_input": "3+4",
        "expected": 7
    },
]
ids = [item['test_case_id'] for item in data]


@pytest.mark.parametrize("data_", data, ids=ids)
def test_param(data_):
    print(data_, '\n')
    assert eval(data_['test_input']) == data_['expected']



#
# @pytest.mark.parametrize("test_input,expected",[
#     ("3+5", 8),
#     ("2+4", 6),
#     ("6*9", 42),
# ])
# def test_eval(test_input, expected):
#     assert eval(test_input) == expected


import pytest

@pytest.fixture
def short_data_other():
    return [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}]

@pytest.fixture
def short_data_canceled():
    return [{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}]
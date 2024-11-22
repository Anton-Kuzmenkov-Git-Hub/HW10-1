import pytest

@pytest.fixture
def short_data_other():
    return [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}]

@pytest.fixture
def short_data_canceled():
    return [{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}]

@pytest.fixture
def example_data():
    return [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

@pytest.fixture
def answer():
    return [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
]

@pytest.fixture
def answer_rev_falls():
    return [
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
]

@pytest.fixture
def same_data():
    return [
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-10-14T21:27:25.241689'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-10-14T02:08:58.425572'},
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2018-10-14T18:35:29.512364'},
]

@pytest.fixture
def same_data_answer():
    return [
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-10-14T21:27:25.241689'},
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2018-10-14T18:35:29.512364'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-10-14T02:08:58.425572'}
]

@pytest.fixture
def data_error():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-.419441"}
]

import pytest
import requests
from endpoints.create_challenger import CreateChallenger
from endpoints.get_challengers import GetCallenges

@pytest.fixture()
def create_chellenger():
    return CreateChallenger()

@pytest.fixture()
def get_all_challenger():
    return GetCallenges()

@pytest.fixture()
def create_x_challeger(create_chellenger):
    response = requests.post('https://apichallenges.eviltester.com/challenger')
    assert 'X-CHALLENGER'  in response.headers
    header = response.headers['X-CHALLENGER']
    return header

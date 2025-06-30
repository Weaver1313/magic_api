import requests
from endpoints.create_challenger import CreateChallenger


def test_create_challenger(create_chellenger):
    create_chellenger.create_x_challenger()
    create_chellenger.check_response_status_is_ok()
    create_chellenger.check_x_challenger_in_header()

def test_get_all_chellengers(create_x_challeger, get_all_chellenger):
    get_all_chellenger.get_all_challenges(create_x_challeger)
    get_all_chellenger.check_status_code_ok()
    get_all_chellenger.check_res_challenger()
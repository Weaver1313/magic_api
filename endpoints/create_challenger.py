import requests

class CreateChallenger:
    status = None
    value_challenger = None
    key_challenger = None

    def create_x_challenger(self):
        response = requests.post(
        'https://apichallenges.eviltester.com/challenger',
        headers={"Content-Type": "application/json"})
        
        self.status = response.status_code
        self.value_challenger = response.headers['X-CHALLENGER']
        self.key_challenger = response.headers
        
        return self.value_challenger, self.status
    
    def check_response_status_is_ok(self):
        assert self.status == 201
    
    def check_x_challenger_in_header(self):
        print(self.key_challenger)
        assert 'X-CHALLENGER'  in self.key_challenger
    
    def create_x_value_challenger(self):
        pass
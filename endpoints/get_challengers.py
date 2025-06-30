import requests

class GetCallenges():
    status = None
    res_body = None

    def get_all_challenges(self, challenger):
        response = requests.get('https://apichallenges.eviltester.com/challenges',
                                headers={
                                    'X-CHALLENGER': challenger
                                })
        self.status = response.status_code
        self.res_body = response.json()

    def check_status_code_ok(self):
        assert self.status == 200

    def check_res_challenger(self):
        assert "challenges" in self.res_body
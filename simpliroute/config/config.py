from dataclasses import dataclass

class Config:
    base_url:str = 'https://api.simpliroute.com/v1'

    @property
    def headers(self):
        raise NotImplementedError("You need to subclass this to get a valid header")

    def get_endpoint(self, endpoint:str):
        return f'{self.base_url}/{endpoint}'
    
@dataclass
class ConfigV1(Config):
    token:str = None

    @property
    def headers(self):
       return {
        "content-type": "application/json",
        "authorization": f"Token {self.token}",
    }



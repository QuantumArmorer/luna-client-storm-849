import requests
from datetime import datetime

class LunaClient:
    def __init__(self, base_url='https://api.example.com/luna'):
        self.base_url = base_url

    def get_luna_data(self):
        try:
            response = requests.get(self.base_url)
            if response.status_code == 200:
                return response.json()
            else:
                print(f'Failed to retrieve data: {response.status_code}')
        except Exception as e:
            print(f'An error occurred: {e}')

    def print_luna_info(self):
        data = self.get_luna_data()
        if data:
            print('Luna Client Data')
            print('------------------')
            print(f'Timestamp: {datetime.now()}')
            print(f'Data: {data}')
        else:
            print('No data available')

if __name__ == '__main__':
    client = LunaClient()
    client.print_luna_info()
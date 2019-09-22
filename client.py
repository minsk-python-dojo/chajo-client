import requests
from typing import List


class BaseClient:
    
    def __init__(self, server_address):
        self.server_address = server_address
        self.userlist = None
        self.nickname = None

    def launch(self) -> bool:
        try:
            ping_resp = requests.get(f'{self.server_address}/ping')
            ping_resp_json = ping_resp.json()

            if not ping_resp_json:
                return False
            
            server_status = ping_resp_json.get('status') == 'OK'
            return server_status

        except Exception as exc:
            print('exception occurred:', exc)

        return False

    def get_userlist(self) -> List[str]:
        pass

    def print_message(self, text: str):
        pass

    def send_message(self, text: str):
        pass

    def exit(self):
        pass

    def print_userlist(self):
        print('Users in the chat:')
        
        for user in self.userlist:
            print(f'- {user}')

def main():
    client = BaseClient(
        server_address='http://127.0.0.1'
    )

    if not client.launch():
        print('Client launch failed! Aborting.')
        return

    nickname = input('Enter nickname: ')
    client.nickname = nickname
    print(client.nickname)

    #user_list = client_obj.get_userlist()




if __name__ == '__main__':
    main()

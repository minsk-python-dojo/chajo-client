from typing import List

class BaseClient:
    
    def __init__(self):
        pass

    def launch(self):
        pass
        
    def set_nickname(self, nickname: str):
        pass

    def get_userlist(self) -> List[str]:
        pass

    def print_message(self, text: str):
        pass

    def send_message(self, text: str):
        pass

    def exit(self):
        pass


def main():
    pass

if __name__ == '__main__':
    main()

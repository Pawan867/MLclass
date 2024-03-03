from abc import ABC, abstractmethod


class BankingApp(ABC):

    def database(self):
        print(f"Connectes to database successfully.")

    def security(self):
        print("Security of Moileapp")


class MobileApp(BankingApp):
    def login_app(self):
        print(f"Login to mobile app successfully")


if __name__ == "__main__":
    # bank = BankingApp()
    # bank.database()
    mobile_app = MobileApp()
    print(mobile_app)

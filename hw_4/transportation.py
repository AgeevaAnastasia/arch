from abc import ABC, abstractmethod
from datetime import datetime


class User:
    def __init__(self, user_id: int, name: str, hash_password: int, card_number: int):
        self.user_id = user_id
        self.name = name
        self.hash_password = hash_password
        self.card_number = card_number


class UserRepo(ABC):
    @abstractmethod
    def create_user(self, user: User):
        pass

    @abstractmethod
    def get_user(self, name: str):
        pass

    @abstractmethod
    def delete_user(self, user: User):
        pass


class UserRepository(UserRepo):
    def __init__(self):
        self.repo = [User]

    def create_user(self, name: str):
        pass

    def get_user(self, name: str):
        pass

    def delete_user(self, user: User):
        pass


class UserProvider:
    def __init__(self):
        self.user_repo = UserRepository()

    def get_user(self, name: str):
        return self.user_repo.get_user(name)


class Carrier:
    def __init__(self, carrier_id: int, name: str, places: int, card_number: int):
        self.carrier_id = carrier_id
        self.name = name
        self.places = places
        self.free_places = places
        self.card_number = card_number
        

class CarrierRepo(ABC):
    @abstractmethod
    def add_carrier(self, user: Carrier):
        pass

    @abstractmethod
    def get_carrier(self, name: str):
        pass

    @abstractmethod
    def delete_carrier(self, carrier: Carrier):
        pass


class CarrierRepository(CarrierRepo):
    def __init__(self):
        self.repo = [Carrier]

    def add_carrier(self, name: str):
        pass

    def get_carrier(self, name: str):
        pass

    def delete_carrier(self, carrier: Carrier):
        pass


class CarrierProvider:
    def __init__(self):
        self.carrier_repo = CarrierRepository()

    def add_carrier(self, carrier: Carrier):
        if self.carrier_repo.add_carrier(carrier):
            return True
        return False


class Ticket:
    def __init__(self, id: int, price: float, place: int, date_time: datetime, carrier: Carrier):
        self.id = id
        self.price = price
        self.date_time = date_time
        self.carrier = carrier
        self.status = True


class TicketRepo(ABC):
    @abstractmethod
    def create_ticket(self, ticket: Ticket):
        pass

    @abstractmethod
    def get_ticket(self, date_time: datetime, city: str):
        pass

    @abstractmethod
    def delete_ticket(self, ticket: Ticket):
        pass


class TicketRepository(TicketRepo, ABC):
    def __init__(self):
        self.repo = [Ticket]

    def create_ticket(self, ticket: Ticket):
        pass

    def get_ticket(self, date_time: datetime, city: str):
        pass

    def delete_ticket(self, ticket: Ticket):
        pass


class TicketProvider:
    def __init__(self):
        self.ticket_repo = TicketRepository()

    def find_tickets(self, place: int):
        return self.ticket_repo.get_ticket(place)


class BankAccount:
    def __init__(self, card_number: int):
        self.card_number = card_number
        self.balance = 0


class BankAccountRepo(ABC):
    @abstractmethod
    def increase_balance(self, cash: BankAccount, value: float):
        pass

    @abstractmethod
    def decrease_balance(self, cash: BankAccount, value: float):
        pass


class BankAccountRepository(BankAccountRepo):
    def __init__(self):
        self.repo = [BankAccount]

    def increase_balance(self, cash: BankAccount, value: float):
        pass

    def decrease_balance(self, cash: BankAccount, value: float):
        pass


class BankAccountProvider:
    def __init__(self):
        self.bank_account_repo = BankAccountRepository()

    def check_balance(self, user: User, value: float):
        for cash in self.bank_account_repo.repo:
            if cash.card_number == user.card_number:
                return cash.balance >= value
        return False

    def decrease_money(self, user: User | Carrier, value: float):
        for cash in self.bank_account_repo.repo:
            if cash.card_number == user.card_number:
                cash.balance -= value
                return True
        return False

    def increase_money(self, carrier: Carrier | User, value: float):
        for cash in self.bank_account_repo.repo:
            if cash.card_number == carrier.card_number:
                cash.balance += value
                return True
        return False


class Customer:
    def __init__(self, user: User):
        self.user = user
        self.user_provider = UserProvider()
        self.bank_account_provider = BankAccountProvider()
        self.ticket_provider = TicketProvider()
        self.carrier_provider = CarrierProvider()
        self.tickets = []

    def buy_ticket(self, ticket: Ticket, count: int) -> bool:
        self.tickets.extend(self.ticket_provider.find_tickets(ticket, count))
        value = ticket.price * count
        return True

    def get_tickets(self, date_time: datetime, city: str):
        return self.ticket_provider.find_tickets(date_time, city)


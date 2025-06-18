from abc import ABC, abstractmethod

class Approver(ABC):
    def __init__(self, name):
        self.name = name
        self.next_approver = None

    def set_next(self, approver):
        self.next_approver = approver
        return approver

    def handle_request(self, amount):
        pass


class TeamLeader(Approver):
    def handle_request(self, amount):
        if amount <= 1000:
            print(f"Team Leader {self.name} approved the request of ${amount}")
        else:
            super().handle_request(amount)


class DepartmentHead(Approver):
    def handle_request(self, amount):
        if amount <= 10000:
            print(f"Department Head {self.name} approved the request of ${amount}")
        else:
            super().handle_request(amount)


class FinanceDirector(Approver):
    def handle_request(self, amount):
        if amount <= 25000:
            print(f"Finance Director {self.name} approved the request of ${amount}")
        else:
            super().handle_request(amount)


class CEO(Approver):
    def handle_request(self, amount):
        print(f"CEO {self.name} approved the request of ${amount}")

team_leader = TeamLeader("Mher")
department_head = DepartmentHead("Bob")
finance_director = FinanceDirector("Malvina")
ceo = CEO("Panayotus Dmitrius")

team_leader.set_next(department_head).set_next(finance_director).set_next(ceo)

team_leader.handle_request(500)
team_leader.handle_request(7500)
team_leader.handle_request(20000)
team_leader.handle_request(50000)
team_leader.handle_request(1000000)

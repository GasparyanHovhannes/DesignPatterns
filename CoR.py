from abc import ABC, abstractmethod

class Approver(ABC):
    def __init__(self, name):
        self.name = name
        self.next_approver = None

    def set_next(self, approver):
        self.next_approver = approver
        return approver

    def pass_to_next(self, amount):
        if self.next_approver:
            self.next_approver.handle_request(amount)
        else:
            print("Request cannot be approved.")

    @abstractmethod
    def handle_request(self, amount):
        pass

class TeamLeader(Approver):
    def handle_request(self, amount):
        if amount <= 1000:
            print(f"Team Leader {self.name} approved ${amount}")
        else:
            self.pass_to_next(amount)


class DepartmentHead(Approver):
    def handle_request(self, amount):
        if amount <= 10000:
            print(f"Department Head {self.name} approved ${amount}")
        else:
            self.pass_to_next(amount)


class FinanceDirector(Approver):
    def handle_request(self, amount):
        if amount <= 25000:
            print(f"Finance Director {self.name} approved ${amount}")
        else:
            self.pass_to_next(amount)


class CEO(Approver):
    def handle_request(self, amount):
        print(f"CEO {self.name} approved ${amount}")

team_leader = TeamLeader("Alice")
department_head = DepartmentHead("Bob")
finance_director = FinanceDirector("Carol")
ceo = CEO("Diana")

team_leader.set_next(department_head).set_next(finance_director).set_next(ceo)

team_leader.handle_request(500)
team_leader.handle_request(12000)
team_leader.handle_request(50000)
team_leader.handle_request(999999)

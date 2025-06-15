class ThirdPartyPayment:
    def make_payment(self, value):
        return f"Processed payment of ${value} through ThirdPartyPayment."

class PaymentProcessor:
    def pay(self, amount):
        pass

class PaymentAdapter(PaymentProcessor):
    def __init__(self, third_party):
        self.third_party = third_party

    def pay(self, amount):
        return self.third_party.make_payment(amount)

third_party_system = ThirdPartyPayment()
adapter = PaymentAdapter(third_party_system)

print(adapter.pay(100))
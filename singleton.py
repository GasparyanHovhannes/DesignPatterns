class CentralBank:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CentralBank, cls).__new__(cls)
            cls._instance.name = "National Reserve Bank"
        return cls._instance

# Usage
bank1 = CentralBank()
bank2 = CentralBank()

print(bank1.name)  # National Reserve Bank
print(bank1 is bank2)  # True, both are the same instance
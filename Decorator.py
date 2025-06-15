class Jersey:
    def cost(self):
        return 30

class JerseyDecorator(Jersey):
    def __init__(self, jersey):
        self._jersey = jersey

    def cost(self):
        return self._jersey.cost()

class NamePrintDecorator(JerseyDecorator):
    def cost(self):
        return self._jersey.cost() + 10

class SponsorLogoDecorator(JerseyDecorator):
    def cost(self):
        return self._jersey.cost() + 20

class PremiumFabricDecorator(JerseyDecorator):
    def cost(self):
        return self._jersey.cost() + 40

basic_jersey = Jersey()
jersey_with_name = NamePrintDecorator(basic_jersey)
jersey_with_name_and_logo = SponsorLogoDecorator(jersey_with_name)
custom_jersey = PremiumFabricDecorator(jersey_with_name_and_logo)

print("Total cost: ", custom_jersey.cost())

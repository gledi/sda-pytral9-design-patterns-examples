class RoyalMail:
    cost = 15.0
    duration = 3

    def __init__(self, package):
        self.package = package

    def ship(self):
        print(
            (
                f"Shipping {self.package} in {self.duration} days "
                f"for {self.cost} via {self.__class__.__name__}"
            )
        )


class ShadyCourier:
    cost = 1.0
    duration = 30

    def __init__(self, package):
        self.package = package

    def ship(self):
        print(
            (
                f"Shipping {self.package} in {self.duration} days "
                f"for {self.cost} via {self.__class__.__name__}"
            )
        )


class OnlineStore:
    _companies = {"RoyalMail": RoyalMail, "ShadyCourier": ShadyCourier}

    def proces_shipment(self, package, company="RoyalMail"):
        return self._companies[company](package)


if __name__ == "__main__":
    store = OnlineStore()
    fast_shipment = store.proces_shipment("Vase")
    fast_shipment.ship()

    slow_shipment = store.proces_shipment("Flamingo", "ShadyCourier")
    slow_shipment.ship()

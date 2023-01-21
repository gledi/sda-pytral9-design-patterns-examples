from typing import Protocol


class SupportsNotification(Protocol):
    def notify(self, name: str, qty: int) -> None:
        ...


class WarehouseWatcher:
    def notify(self, name: str, qty: int) -> None:
        print(f"Prepare to store {qty} {name}")


class MarketingWatcher:
    def notify(self, name, qty):
        print(f"We can run our ads about {name}")


class WebsiteWatcher:
    def notify(self, name, qty):
        print(f"We have {qty} {name} available")


class Shop:
    def __init__(self):
        self.products = {}
        self.watchers = {}

    def add_watchers(self, product, *watchers):
        if product not in self.watchers:
            self.watchers[product] = []
        for watcher in watchers:
            self.watchers[product].append(watcher)

    def add_product(self, name, qty):
        in_stock = self.products.get(name, 0)
        if in_stock == 0:
            for watcher in self.watchers.get(name, []):
                watcher.notify(name, qty)
        self.products[name] = qty + in_stock

    def buy(self, name, qty):
        in_stock = self.products.get(name, 0)
        if qty > in_stock:
            raise ValueError("Not enough items in stock")
        self.products[name] = in_stock - qty


if __name__ == "__main__":
    shop = Shop()
    shop.add_watchers("laptop", WarehouseWatcher(), WebsiteWatcher())
    shop.add_watchers("iphone", MarketingWatcher())
    shop.add_watchers("cookies", WebsiteWatcher())

    shop.add_product("vehicle", 5)
    shop.add_product("laptop", 10)
    shop.add_product("laptop", 2)
    shop.buy("laptop", 1)
    shop.buy("laptop", 9)
    shop.add_product("laptop", 5)

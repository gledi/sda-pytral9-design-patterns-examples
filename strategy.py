from typing import Protocol
import random


class Stock:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.history = []

    def __str__(self):
        return self.name

    def change(self, delta):
        self.history.append(self.price)
        self.price += delta


class StockExchange:
    def __init__(self):
        self.stocks = []

    def add_stock(self, stock):
        self.stocks.append(stock)


class SupportsTrade(Protocol):
    def trade(self):
        pass


class AggresiveTradeBot:
    def __init__(self, se: StockExchange):
        self.se = se

    def trade(self):
        for stock in self.se.stocks:
            try:
                last_price = stock.history[-1]
            except IndexError:
                continue

            if stock.price > last_price:
                print(f"Buying {stock} at {stock.price}")


class AfraidTradeBot:
    def __init__(self, se):
        self.se = se

    def trade(self):
        for stock in self.se.stocks:
            try:
                last_price = stock.history[-1]
            except IndexError:
                continue

            if stock.price < last_price:
                print(f"Selling {stock} at {stock.price}")


class IndifferentBot:
    def __init__(self, se):
        self.se = se

    def trade(self):
        print("Whatever ...")


class SuperAggresiveBot:
    def __init__(self, se: StockExchange):
        self.se = se

    def trade(self):
        for stock in self.se.stocks:
            try:
                last_price = stock.history[-1]
            except IndexError:
                continue

            if stock.price > 2 * last_price:
                print(f"Buying {stock} at {stock.price} as it is rising fast")


class HftFirm:
    def __init__(self, name: str, strategy: SupportsTrade):
        self.name = name
        self.strategy = strategy

    def work(self):
        print(f" --- {self.name} ---")
        self.strategy.trade()


if __name__ == "__main__":
    se = StockExchange()
    apple = Stock("AAPL", 567)
    msft = Stock("MSFT", 230)
    tesla = Stock("TSLA", 345)
    bp = Stock("BP", 345)
    for i in range(20):
        apple.change(random.randrange(-20, 20))
        msft.change(random.randrange(-20, 20))
        tesla.change(random.randrange(-20, 20))
        bp.change(random.randrange(-20, 20))

    se.add_stock(msft)
    se.add_stock(apple)
    se.add_stock(bp)
    se.add_stock(tesla)

    goldman = HftFirm("Goldman Sacks", AggresiveTradeBot(se))
    jpm = HftFirm("JP Morgan", SuperAggresiveBot(se))
    boa = HftFirm("Bank of America", AfraidTradeBot(se))

    for i in range(32):
        goldman.work()
        jpm.work()
        boa.work()

        apple.change(random.randrange(-20, 20))
        msft.change(random.randrange(-20, 20))
        tesla.change(random.randrange(-20, 20))
        bp.change(random.randrange(-20, 20))

        print(f"----------- {i} ----------")

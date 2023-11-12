# 合計金額を算出するOrderクラス


class Order:
    tax = 1.1

    def __init__(self, price, count):
        self.price = price
        self.count = count

    def total_price(self):
        total = self.price * self.count * Order.tax
        print(total)
        # return total


# order1 = Order(100, 10)
# order1.total_price()
# order2 = Order(138, 22)
# order2.total_price()

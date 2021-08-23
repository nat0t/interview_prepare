"""
Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве аргумента в дочерний класс.
Выполнить перегрузку методов конструктора дочернего класса (метод init, в который должна передаваться переменная —
скидка), и перегрузку метода str дочернего класса. В этом методе должна пересчитываться цена и возвращаться результат —
цена товара со скидкой. Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы
(вторая и третья строка после объявления дочернего класса).
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.__discount = discount

    @property
    def discount(self):
        return self.__discount

    def __str__(self):
        return f'Total price: {self.price * (1 - self.discount / 100)}'
    
    def get_parent_data(self):
        return f'Name: {self.name}, price: {self.price}'


if __name__ == '__main__':
    product = ItemDiscountReport('Notebook', 2000, 15)
    print(product.get_parent_data())

    product.price = 2100
    print(product.get_parent_data())
    print(product)

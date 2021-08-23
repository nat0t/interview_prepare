"""
Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс ItemDiscountReport на два класса.
Инициализировать классы необязательно. Внутри каждого поместить функцию get_info, которая в первом классе будет отвечать
за вывод названия товара, а вторая — его цены. Далее реализовать выполнение каждой из функции тремя способами.
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

    def get_info(self):
        raise NotImplementedError()


class ItemDiscountReportName(ItemDiscount):
    def get_info(self):
        return self.name


class ItemDiscountReportPrice(ItemDiscount):
    def get_info(self):
        return self.price


if __name__ == '__main__':
    product_name = ItemDiscountReportName('Notebook', 2000)
    product_price = ItemDiscountReportPrice('Notebook', 2000)

    print(product_name.get_info())
    print(ItemDiscountReportName.get_info(product_name))
    print(getattr(ItemDiscountReportName, 'get_info')(product_name))

    print(product_price.get_info())
    print(ItemDiscountReportPrice.get_info(product_price))
    print(getattr(ItemDiscountReportPrice, 'get_info')(product_price))

"""
Инкапсулировать оба параметра (название и цену) товара родительского класса. Убедиться, что при сохранении текущей
логики работы программы будет сгенерирована ошибка выполнения.
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'Name: {self.__name}, price: {self.__price}'


if __name__ == '__main__':
    product = ItemDiscountReport('Notebook', 2000)
    try:
        print(product.get_parent_data())
    except AttributeError as error:
        print(error)

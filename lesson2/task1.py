"""
Проверить механизм наследования в Python. Для этого создать два класса. Первый — родительский (ItemDiscount), должен
содержать статическую информацию о товаре: название и цену. Второй — дочерний (ItemDiscountReport), должен содержать
функцию (get_parent_data), отвечающую за отображение информации о товаре в одной строке. Проверить работу программы,
создав экземпляр (объект) родительского класса.
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'Name: {self.name}, price: {self.price}'


if __name__ == '__main__':
    product = ItemDiscountReport('Notebook', 2000)
    print(product.get_parent_data())

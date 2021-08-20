"""
Усовершенствовать программу «Банковский депозит». Третьим аргументом в функцию должна передаваться фиксированная
ежемесячная сумма пополнения вклада. Необходимо в главной функции реализовать вложенную функцию подсчета процентов для
пополняемой суммы. Примем, что клиент вносит средства в последний день каждого месяца, кроме первого и последнего.
Например, при сроке вклада в 6 месяцев пополнение происходит в течение 4 месяцев. Вложенная функция возвращает сумму
дополнительно внесенных средств (с процентами), а главная функция — общую сумму по вкладу на конец периода.
"""
from typing import Optional


def bank_deposit(amount: float, term: int, replenishment: float) -> Optional[float]:
    deposits = (
        {'begin_sum': 0.0, 'end_sum': 0, 6: 5, 12: 6, 24: 5},
        {'begin_sum': 0.0, 'end_sum': 0, 6: 6, 12: 7, 24: 6.5},
        {'begin_sum': 0.0, 'end_sum': 0, 6: 7, 12: 8, 24: 7.5},
    )
    if 1000 <= amount < 10000:
        deposit = deposits[0]
    elif 10000 <= amount < 100000:
        deposit = deposits[1]
    elif 100000 <= amount <= 1000000:
        deposit = deposits[2]
    else:
        return

    def calc_replenishment() -> float:
        return replenishment * (1 + deposit[term] / 100)

    deposit['begin_sum'] = amount
    deposit['end_sum'] += amount * deposit[term] / 100 * term / 12 + calc_replenishment() * (term - 2)

    return deposit['begin_sum'] + deposit['end_sum']


if __name__ == '__main__':
    investment = bank_deposit(100000, 12, 1000)
    print(investment) if investment else print('The bank cannot accept this deposit.')

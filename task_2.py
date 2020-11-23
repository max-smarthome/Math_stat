#В результате 10 независимых измерений некоторой величины X, выполненных с одинаковой точностью,
# получены опытные данные: 6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1
# Предполагая, что результаты измерений подчинены нормальному закону распределения вероятностей,
# оценить истинное значение величины X при помощи доверительного интервала,
# покрывающего это значение с доверительной вероятностью 0,95.

from numpy import std
from scipy.stats import t


list_x = [6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1]
sigma_x = std(list_x, ddof= 1)
aver = sum(list_x)/len(list_x)


def interv_t(x, sigma, n, alpha):
    return  [(x -(t(df = n-1).ppf(alpha) * sigma / (n ** (1/2)))), (x +(t(df = n-1).ppf(alpha) * sigma / (n ** (1/2))))]


print(f'sigma = {sigma_x}')
print(f'Talpha/2 = {t(df = len(list_x)-1).ppf(0.975)}')
print(interv_t(aver, sigma_x, len(list_x), 0.975))
'''
sigma = 0.4508017549014448
Talpha/2 = 2.2621571627409915
[6.267515851415712, 6.912484148584286]
тогда mu генеральной совокупности должна лежать в данном отрезке
'''

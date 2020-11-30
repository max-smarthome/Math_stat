#Измерены значения IQ выборки студентов,
# обучающихся в местных технических вузах:
# 131, 125, 115, 122, 131, 115, 107, 99, 125, 111.
# Известно, что в генеральной совокупности IQ распределен нормально.
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.

from numpy import std
from scipy.stats import t


list_x = [131, 125, 115, 122, 131, 115, 107, 99, 125, 111]
sigma_x = std(list_x, ddof= 1)
aver = sum(list_x)/len(list_x)


def interv_t(x, sigma, n, alpha):
    return  [(x -(t(df = n-1).ppf(alpha) * sigma / (n ** (1/2)))), (x +(t(df = n-1).ppf(alpha) * sigma / (n ** (1/2))))]


print(f'sigma = {sigma_x}')
print(f'Talpha/2 = {t(df = len(list_x)-1).ppf(0.975)}')
print(interv_t(aver, sigma_x, len(list_x), 0.975))
'''
sigma = 10.54566788359614
Talpha/2 = 2.2621571627409915
[110.55608365158724, 125.64391634841274]
'''

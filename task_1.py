#1) Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks):
#zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
#ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
#Найдите ковариацию этих двух величин с помощью элементарных действий, а затем с помощью функции cov из numpy
#Полученные значения должны быть равны.
#Найдите коэффициент корреляции Пирсона с помощью ковариации и среднеквадратичных отклонений двух признаков,
#а затем с использованием функций из библиотек numpy и pandas.

import numpy as np

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

#напишем функцию для среднего, дисперсии и среднего квадратичного отклонения:
def average(n):
    return sum(n) / len(n)

def variance(n, offset = True):
    avr = average(n)
    if offset:
        return sum([(i-avr) ** 2 for i in n]) / len(n)
    else:
        return sum([(i - avr) ** 2 for i in n]) / (len(n)-1)


def std_new(n, offset = True):
    return variance(n, offset) ** (1/2)


#напишем две функции для ковариации, одна будет на основе самописной функции, другая на основе функции mean
def cov_1(X, Y):
    return average([X[i] * Y[i] for i in range(len(X))]) - average(X)*average(Y)


def cov_1(X, Y):
    return average([X[i] * Y[i] for i in range(len(X))]) - average(X)*average(Y)


def cov_2(X, Y):
    return np.mean(X*Y) - np.mean(X) * np.mean(Y)

#будем везде считать смещенную ковариацию
print(f'ковариация самописная 1: {cov_1(zp, ks)}')
print(f'ковариация самописная 2: {cov_2(zp, ks)}')
print(f'ковариация np: {np.cov(zp, ks, ddof = 0)}')


'''
ковариация самописная 1: 9157.839999999997
ковариация самописная 2: 9157.839999999997
ковариация np: [[ 3494.64  9157.84]
 [ 9157.84 30468.89]]
 '''

#напишем функции для вычисления коэфф. кореляции. Первая будет с использованием модуля numpy, вторая полностью самописная
def r_1(X, Y, offset = True):
    if not offset:
        return cov_2(X, Y) / (np.std(X, ddof=1) * np.std(Y, ddof=1))
    else:
        return cov_2(X, Y) / (np.std(X) * np.std(Y))

def r_2(X,Y, offset = True):
    return cov_1(X, Y) / (std_new(X, offset) * std_new(Y, offset))


def r_3(X,Y):
    return np.cov(X, Y,ddof=0)[1][0] / (np.std(X) * np.std(Y))


print(f'Корреляция самописная 1: {r_1(zp, ks, offset = True)}')
print(f'Корреляция самописная 2: {r_2(zp, ks, offset = True)}')
print(f'Корреляция самописная 3: {r_3(zp, ks)}')
print(f'Корреляция numpy: {np.corrcoef(zp, ks)}')

'''
Корреляция самописная 1: 0.8874900920739158
Корреляция самописная 2: 0.8874900920739158
Корреляция самописная 3: 0.8874900920739163
Корреляция numpy: [[1.         0.88749009]
 [0.88749009 1.        ]]]
'''
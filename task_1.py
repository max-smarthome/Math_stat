# Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24,
# 57, 55, 70, 75, 65, 84, 90, 150. Посчитать (желательно без использования статистических методов
# наподобие std, var, mean) среднее арифметическое,
# среднее квадратичное отклонение, смещенную и несмещенную оценки дисперсий для данной выборки.
inp_list = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]
import numpy

# функция для среднего арифметического
def average(n):
    return sum(n) / len(n)


# функция для дисперсии
def variance(n, offset = True):
    avr = average(n)
    if offset:
        return sum([(i-avr) ** 2 for i in n]) / len(n)
    else:
        return sum([(i - avr) ** 2 for i in n]) / (len(n)-1)

#функция для стандартного отклонения
def std_new(n, offset = True):
    return variance(n, offset) ** (1/2)


print(average(inp_list))#65.3
print(variance(inp_list))#950.11 смещенная
print(variance(inp_list, offset=False))#1000.1157894736842 без смещения
print(std_new(inp_list))#30.823854398825596 смещенная
print(std_new(inp_list, offset=False))#31.624607341019814 без смещения


# для сравнения стандартные функции
print(numpy.std(inp_list))#30.823854398825596
print(numpy.mean(inp_list))#65.3
print(numpy.var(inp_list))#950.11
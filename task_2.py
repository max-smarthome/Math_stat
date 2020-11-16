#	Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004.
#	В жилом комплексе после ремонта в один день включили 5000 новых лампочек.
#	Какова вероятность, что ни одна из них не перегорит в первый день? Какова вероятность, что перегорят ровно две?


# так как проводится большое количество испытаний n и
# при этом вероятность p появления события A в отдельном испытании мала, то будем пользоваться распределдением Пуассона
from math import factorial, exp

#напишем функцию для вычисления распрееления пуассона
def puasson(p, m, n):
    lamb = p * n #формула для средней вероятности
    return (lamb**m)/factorial(m) * exp(-lamb)

print(puasson(0.0004, 0, 5000))#вероятность перегореть одной лампе 0.1353352832366127
print(puasson(0.0004, 2, 5000))#вероятность перегореть двум лампам 0.2706705664732254



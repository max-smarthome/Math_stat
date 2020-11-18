#	В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12 мячей, из которых 5 белых.
#	Из первого ящика вытаскивают случайным образом два мяча, из второго - 4.
#	Какова вероятность того, что 3 мяча белые


from math import factorial


# напишем функцию для сочетания
def combination(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

# подходят следующие случаи:
# 1)из первого 2 белых, из второго 1 белый и 3 черных;
# 2)из первого 1 белый и 1 черный, из второго 2 белых и 2 черных
# 3)и из первого все черные, из второго 3 белых и 1 черный


# 1
p1 = (combination(5,2) * combination(3,0)/combination(8, 2)) * (combination(5,1)*combination(7,3)/combination(12,4))

# 2
p2 = (combination(5,1) * combination(3,1)/combination(8, 2)) * (combination(5,2) * combination(7,2)/combination(12,4))

# 3
p3 = (combination(5,0) * combination(3,2)/combination(8, 2)) * (combination(5,3) * combination(7,1)/combination(12,4))


print(p1+p2+p3)#0.3686868686868687
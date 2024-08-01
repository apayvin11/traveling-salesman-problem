import numpy as np
import random

# функция отбора
# принимает популяцию, оценки приспособленности особей и размер популяции, до которого ее нужно ограничить
def selection(P, fitness, population_size):
    P1 = []
    fitness1 = []
    # переносим значения приспособленности в отрицательную область
    max_fitness = max(fitness)
    for i in range(len(fitness)):
        fitness[i] -= max_fitness
    # Отбираем 3 элиты
    e = 3
    for i in range(e):
        min_fit = min(fitness)
        min_index = fitness.index(min_fit)
        P1.append(P[min_index].copy())
        fitness1.append(min_fit)
        P.pop(min_index)
        fitness.pop(min_index)

    D = fitness / sum(fitness) # Determine selection probability
    E = np.cumsum(D) # Determine cumulative probability
    N = random.random()
    index_candidate = 0 # индекс кандидата на отбор из исходной популяции
    counter = e # счетчик количества особей
    while counter < population_size:
        if N <= E[index_candidate]:
            P1.append(P[index_candidate].copy())
            fitness1.append(fitness[index_candidate].copy())
            N = random.random()
            counter +=1
            index_candidate = 0
        else:
            index_candidate += 1

    # возвращаем на место, так как для вычислений переводили значения в отрицательную область
    for i in range(len(fitness1)):
        fitness1[i] += max_fitness
    return P1, fitness1